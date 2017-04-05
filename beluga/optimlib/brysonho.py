"""
Computes the necessary conditions of optimality using Bryson & Ho's method

[1] Bryson, Arthur Earl. Applied optimal control: optimization, estimation and control. CRC Press, 1975.
"""

import functools as ft
import itertools
import re as _re
import simplepipe as sp
import sympy
import pystache
import imp

from beluga.utils import sympify2, get_root
from beluga.problem import SymbolicVariable
from beluga.bvpsol import BVP

def total_derivative(expr, var, dependent_vars=None):
    """
    Take derivative taking pre-defined quantities into consideration

    dependent_variables: Dictionary containing dependent variables as keys and
                         their expressions as values
    """
    if dependent_vars is None:
        dependent_vars = {}

    dep_var_names = dependent_vars.keys()
    dep_var_expr = [(expr) for (_,expr) in dependent_vars.items()]

    dFdq = [sympy.diff(expr, dep_var).subs(dependent_vars.items()) for dep_var in dep_var_names]
    dqdx = [sympy.diff(qexpr, var) for qexpr in dep_var_expr]

    # Chain rule + total derivative
    out = sum(d1*d2 for d1,d2 in zip(dFdq, dqdx)) + sympy.diff(expr, var)
    return out

def process_quantities(quantities):
    """Performs preprocessing on quantity definitions. Creates a new total
    derivative operator that takes considers these definitions.
    """
    # logging.info('Processing quantity expressions')

    # TODO: Sanitize quantity expressions
    # TODO: Check for circular references in quantity expressions

    # Trivial case when no quantities are defined
    if len(quantities) == 0:
        yield []
        yield []
        yield total_derivative

    quantity_subs = [(q.name, q.val) for q in quantities]
    quantity_sym, quantity_expr = zip(*quantity_subs)
    quantity_expr = [qty_expr.subs(quantity_subs) for qty_expr in quantity_expr]

    # Use substituted expressions to recreate quantity expressions
    quantity_subs = [(str(qty_var),qty_expr) for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]
    # Dictionary for substitution
    quantity_vars = dict(quantity_subs)

    # Dictionary for use with mustache templating library
    quantity_list = [{'name':str(qty_var), 'expr':str(qty_expr)} for qty_var, qty_expr in zip(quantity_sym, quantity_expr)]

    # Function partial that takes derivative while considering quantities
    derivative_fn = ft.partial(total_derivative, dependent_vars=quantity_vars)

    yield quantity_vars
    yield quantity_list
    yield derivative_fn

def make_augmented_cost(cost, constraints, location):
    """Augments the cost function with the given list of constraints.

    Returns the augmented cost function
    """
    filtered_list = constraints.get(location)

    def make_lagrange_mult(c, ind = 1):
        return sympify2('lagrange_' + c.type + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind) for (ind,c) in enumerate(filtered_list,1)]

    aug_cost_expr = cost.expr + sum(nu*c for (nu, c) in zip(lagrange_mult, filtered_list))

    aug_cost = SymbolicVariable({'expr':aug_cost_expr, 'unit': cost.unit}, sym_key='expr')
    return aug_cost
    # yield aug_cost
    # yield lagrange_mult

def make_aug_params(constraints, location):
    """Make the lagrange multiplier terms for boundary conditions."""
    filtered_list = constraints.get(location)
    def make_lagrange_mult(c, ind = 1):
        return sympify2('lagrange_' + c.type + '_' + str(ind))
    lagrange_mult = [make_lagrange_mult(c, ind) for (ind,c) in enumerate(filtered_list,1)]
    return lagrange_mult


def make_hamiltonian_and_costates(states, path_cost, derivative_fn):
    """simplepipe task for creating the hamiltonian and costates

    Workspace variables
    -------------------
    states - list of dict
        List of "sympified" states

    path_cost - Object representing the path cost terminal

    Returns the hamiltonian and the list of costates
    """

    costate_names = [sympify2('lam'+str(s.name).upper()) for s in states]
    ham = path_cost.expr + sum([lam*s.eom
                             for s, lam in zip(states, costate_names)])

    costates = [SymbolicVariable({'name': lam, 'eom':derivative_fn(-1*(ham), s)})
                for s, lam in zip(states, costate_names)]
    yield ham
    yield costates

def sanitize_constraint_expr(constraint, states):
    """
    Checks the initial/terminal constraint expression for invalid symbols
    Also updates the constraint expression to reflect what would be in code
    """
    if constraint.type == 'initial':
        pattern = r'([\w\d\_]+)_0'
        prefix = '_x0'
    elif constraint.type == 'terminal':
        pattern = r'([\w\d\_]+)_f'
        prefix = '_xf'
    else:
        raise ValueError('Invalid constraint type')

    m = _re.findall(pattern,str(constraint.expr))
    invalid = [x for x in m if x not in states]

    if not all(x is None for x in invalid):
        raise ValueError('Invalid expression(s) in boundary constraint:\n'+str([x for x in invalid if x is not None]))

    return _re.sub(pattern,prefix+r"['\1']",str(constraint.expr))


def make_boundary_conditions(constraints, states, costates, cost, derivative_fn, location):
    """simplepipe task for creating boundary conditions for initial and terminal
    constraints."""

    bc_list = [sanitize_constraint_expr(x, states)
                    for x in constraints.get(location)]
    # bc_terminal = [sanitize_constraint_expr(x, states)
    #                 for x in constraints.get('terminal')]

    if location == 'initial':
        sign = sympify2('-1')
    elif location == 'terminal':
        sign = sympify2('1')

    cost_expr = sign * cost

    #TODO: Fix hardcoded if conditions
    #TODO: Change to symbolic
    bc_list += [str(costate - derivative_fn(cost_expr, state))
                        for state, costate in zip(states, costates)]

    return bc_list

def make_time_bc(constraints, bc_terminal):
    """Makes free or fixed final time boundary conditions."""
    time_constraints = constraints.get('independent')
    if len(time_constraints) > 0:
        return bc_terminal+['tf - 1']
    else:
        # Add free final time boundary condition
        return bc_terminal+['_H - 0']



def make_dhdu(ham, controls, derivative_fn):
    """Computes the partial of the hamiltonian w.r.t control variables."""
    dhdu = []
    for ctrl in controls:
        dHdu = derivative_fn(ham, ctrl)
        custom_diff = dHdu.atoms(sympy.Derivative)
        # Substitute "Derivative" with complex step derivative
        repl = {(d,im(f.func(v+1j*1e-30))/1e-30) for d in custom_diff
                    for f,v in zip(d.atoms(sympy.AppliedUndef),d.atoms(Symbol))}

        dhdu.append(dHdu.subs(repl))

    return dhdu

def make_control_law(dhdu, controls):
    """Solves control equation to get control law."""
    ctrl_sol = sympy.solve(dhdu, controls, dict=True)
    control_options = [ [{'name':str(ctrl), 'expr':str(expr)}
                            for (ctrl,expr) in option.items()]
                            for option in ctrl_sol]
    return control_options

def generate_problem_data(workspace):
    """Generates the `problem_data` dictionary used for code generation."""

    tf_var = sympify2('tf') #TODO: Change to independent var?
    problem_data = {
    'aux_list': [
            {
            'type' : 'const',
            'vars': [str(k) for k in workspace['constants']]
            }
     ],
     'state_list':
         [str(x) for x in itertools.chain(workspace['states'], workspace['costates'])]
         + ['tf']
     ,
     'parameter_list': [str(p) for p in itertools.chain(workspace['initial_lm_params'],
                                                        workspace['terminal_lm_params'])],
     'deriv_list':
         [str(tf_var*state.eom) for state in workspace['states']] +
         [str(tf_var*costate.eom) for costate in workspace['costates']] +
         [0]   # TODO: Hardcoded 'tf'
     ,
     'num_states': 2*len(workspace['states']) + 1,
     'dHdu': workspace['dhdu'],
     'bc_initial': [str(_) for _ in workspace['bc_initial']],
     'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
     'control_options': workspace['control_law'],
     'control_list': [str(u) for u in workspace['controls']],
     'num_controls': len(workspace['controls']),
     'ham_expr': str(workspace['ham']),
     'quantity_list': workspace['quantity_list'],
    }
    return problem_data

def load_eqn_template(problem_data, template_file,
                        renderer = pystache.Renderer(escape=lambda u: u)):
    """Loads pystache template and uses it to generate code.

    Parameters
    ----------
        problem_data - dict
            Workspace defining variables for template

        template_file - str
            Path to template file to be used

        renderer
            Renderer used to convert template file to code

    Returns
    -------
    Code generated from template
    """
    with open(template_file) as f:
        tmpl = f.read()
        # Render the template using the data
        code = renderer.render(tmpl, problem_data)
        return code

def create_module(problem_name):
    """Creates a new module for storing compiled code.

    Parameters
    ----------
    problem_name - str
        Unique name for the module

    Returns
    -------
    New module for holding compiled code
    """
    return imp.new_module('_beluga_'+problem_name)

def compile_code_py(code_string, module, function_name):
    """
    Compiles a function specified by template in filename and stores it in
    self.compiled

    Parameters
    ----------
    code_string - str
        String containing the python code to be compiled

    module - dict
        Module in which the new functions will be defined

    function_name - str
        Name of the function being compiled (this must be defined in the
        template with the same name)

    Returns:
        Module for compiled function
        Compiled function
    """
    # For security
    module.__dict__.update({'__builtin__':{}})
    exec(code_string, module.__dict__)
    return getattr(module,function_name)


def make_bvp(workspace):
    """Makes the BVP object for passing into numerical solver."""
    bvp = BVP(workspace['deriv_func_fn'],workspace['bc_func_fn'])

    bvp.solution.aux['const'] = dict((str(const.name),float(const.value)) for const in workspace['constants'])
    bvp.solution.aux['parameters'] = workspace['problem_data']['parameter_list']
    # self.bvp.solution.aux['function']  = problem.functions

    bvp.control_func = workspace['compute_control_fn']
    bvp.problem_data = workspace['problem_data']
    return bvp


def init_workspace(ocp):
    """Initializes the simplepipe workspace using an OCP definition."""
    workspace = {}
    # variable_list = ['states', 'controls', 'constraints', 'quantities', 'initial_cost', 'terminal_cost', 'path_cost']
    workspace['problem_name'] = ocp.name
    workspace['indep_var'] = SymbolicVariable(ocp._properties['independent'])
    workspace['states'] = [SymbolicVariable(s) for s in ocp.states()]
    workspace['controls'] = [SymbolicVariable(u) for u in ocp.controls()]
    workspace['constants'] = [SymbolicVariable(k) for k in ocp.constants()]
    workspace['constraints'] = ocp.constraints()
    workspace['quantities'] = [SymbolicVariable(q) for q in ocp.quantities()]
    workspace['initial_cost'] = SymbolicVariable(ocp.get_cost('initial'), sym_key='expr')
    workspace['terminal_cost'] = SymbolicVariable(ocp.get_cost('terminal'), sym_key='expr')
    workspace['path_cost'] = SymbolicVariable(ocp.get_cost('path'), sym_key='expr')
    return workspace


# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow([
    sp.Task(process_quantities,
            inputs=('quantities'),
            outputs=('quantity_vars', 'quantity_list', 'derivative_fn')),
    sp.Task(ft.partial(make_augmented_cost, location='initial'),
            inputs=('initial_cost', 'constraints'),
            outputs=('aug_initial_cost')),
    sp.Task(ft.partial(make_aug_params, location='initial'),
            inputs=('constraints'),
            outputs=('initial_lm_params')),
    sp.Task(ft.partial(make_augmented_cost, location='terminal'),
            inputs=('terminal_cost', 'constraints'),
            outputs=('aug_terminal_cost')),
    sp.Task(ft.partial(make_aug_params, location='terminal'),
            inputs=('constraints'),
            outputs=('terminal_lm_params')),
    sp.Task(make_hamiltonian_and_costates,
            inputs=('states', 'path_cost', 'derivative_fn'),
            outputs=('ham', 'costates')),
    sp.Task(ft.partial(make_boundary_conditions, location='initial'),
            inputs=('constraints', 'states', 'costates', 'aug_initial_cost', 'derivative_fn'),
            outputs=('bc_initial')),
    sp.Task(ft.partial(make_boundary_conditions, location='terminal'),
            inputs=('constraints', 'states', 'costates', 'aug_terminal_cost', 'derivative_fn'),
            outputs=('bc_terminal')),
    sp.Task(make_time_bc, inputs=('constraints', 'bc_terminal'), outputs=('bc_terminal')),
    sp.Task(make_dhdu,
            inputs=('ham', 'controls', 'derivative_fn'),
            outputs=('dhdu')),
    sp.Task(make_control_law,
            inputs=('dhdu','controls'),
            outputs=('control_law')),

    sp.Task(generate_problem_data,
            inputs='*',
            outputs=('problem_data')),

    # TODO: Move this part into numerical algorithm?
    # Create module for holding compiled code
    sp.Task(ft.partial(create_module), inputs='problem_name', outputs=('code_module')),

    # Load equation template files and generate code
    sp.Task(ft.partial(load_eqn_template,
                template_file=get_root()+'/optimlib/templates/brysonho/deriv_func.py.mu'),
            inputs='problem_data',
            outputs='deriv_func_code'),
    sp.Task(ft.partial(load_eqn_template,
                template_file=get_root()+'/optimlib/templates/brysonho/bc_func.py.mu'),
            inputs='problem_data',
            outputs='bc_func_code'),
    sp.Task(ft.partial(load_eqn_template,
                template_file=get_root()+'/optimlib/templates/brysonho/compute_control.py.mu'),
            inputs='problem_data',
            outputs='compute_control_code'),

    # Compile generated code
    sp.Task(ft.partial(compile_code_py, function_name='deriv_func'),
            inputs=['deriv_func_code', 'code_module'],
            outputs='deriv_func_fn'),
    sp.Task(ft.partial(compile_code_py, function_name='bc_func'),
            inputs=['bc_func_code', 'code_module'],
            outputs='bc_func_fn'),
    sp.Task(ft.partial(compile_code_py, function_name='compute_control'),
            inputs=['compute_control_code', 'code_module'],
            outputs='compute_control_fn'),

    sp.Task(make_bvp, inputs='*', outputs=['bvp'])
], description='Traditional optimal control workflow')

traditional = BrysonHo



## Unit tests ##################################################################
from beluga.problem import ConstraintList
from beluga.problem import SymbolicVariable

def test_process_quantities():
    quantities = [SymbolicVariable(dict(name='rho', val='rho0*exp(-h/H)')),
                  SymbolicVariable(dict(name='D', val='0.5*rho*v^2*Cd*Aref'))]
    qvars, qlist, _ = process_quantities(quantities)

    qvars_expected = dict(rho= sympify2('rho0*exp(-h/H)'),
                          D= sympify2('0.5*Aref*Cd*rho0*v**2*exp(-h/H)'))
    qlist_expected = [{'expr': 'rho0*exp(-h/H)', 'name': 'rho'},
                      {'expr': '0.5*Aref*Cd*rho0*v**2*exp(-h/H)', 'name': 'D'}]

    assert qvars == qvars_expected
    assert qlist == qlist_expected

def test_ham_and_costates():
    states = [SymbolicVariable({'name':'x','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'y','eom':'-v*sin(theta)','unit':'m'}),
              SymbolicVariable({'name':'v','eom':'g*sin(theta)','unit':'m/s'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')

    expected_output = (sympify2('g*lamV*sin(theta) + lamX*v*cos(theta) - lamY*v*sin(theta) + 1'),
                       [SymbolicVariable({'name':'lamX','eom':'0'}),
                       SymbolicVariable({'name':'lamY','eom':'0'}),
                       SymbolicVariable({'name':'lamV','eom':'-lamX*cos(theta) - lamY*sin(theta)'})])

    ham, costates = make_hamiltonian_and_costates(states, path_cost, total_derivative)

    assert ham == expected_output[0]
    assert costates == expected_output[1]

def test_augmented_cost():
    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('h - h_f', 'm')
    terminal_cost = SymbolicVariable({'expr': '-v^2', 'unit': 'm^2/s^2'}, sym_key='expr')

    expected_output = SymbolicVariable({'expr': 'lagrange_terminal_1*(h - h_f) - v**2',
                       'unit': 'm**2/s**2'}, sym_key='expr')
    expected_params = [sympify2('lagrange_terminal_1')]
    aug_cost = make_augmented_cost(terminal_cost, constraints, 'terminal')
    params = make_aug_params(constraints, 'terminal')
    assert aug_cost == expected_output
    assert params == expected_params


def test_make_boundary_conditions():
    states = [SymbolicVariable({'name':'h','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'theta','eom':'v*sin(theta)/r','unit':'rad'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')
    ham, costates = make_hamiltonian_and_costates(states, path_cost, total_derivative)

    constraints = ConstraintList()
    constraints.initial('h - h_0', 'm') # doctest:+ELLIPSIS
    constraints.terminal('theta - theta_f', 'rad') # doctest:+ELLIPSIS

    initial_cost = sympify2('0')
    bc_initial = make_boundary_conditions(constraints, states, costates, initial_cost, total_derivative, 'initial')
    assert bc_initial == ["h - _x0['h']", 'lamH', 'lamTHETA']

    terminal_cost = sympify2('-theta^2')
    bc_terminal = make_boundary_conditions(constraints, states, costates, terminal_cost, total_derivative, 'terminal')
    assert bc_terminal == ["theta - _xf['theta']", 'lamH', 'lamTHETA + 2*theta']

def test_make_control_law():
    states = [SymbolicVariable({'name':'x','eom':'v*cos(theta)','unit':'m'}),
              SymbolicVariable({'name':'y','eom':'v*sin(theta)','unit':'m'}),
              SymbolicVariable({'name':'v','eom':'g*sin(theta)','unit':'m/s'})]
    path_cost = SymbolicVariable({'expr': 1}, sym_key='expr')
    controls = [SymbolicVariable({'name':'theta','unit':'rad'})]
    ham, costates = make_hamiltonian_and_costates(states, path_cost, total_derivative)
    dhdu = make_dhdu(ham, controls, total_derivative)
    assert dhdu == [sympify2('g*lamV*cos(theta) - lamX*v*sin(theta) + lamY*v*cos(theta)')]
    control_law = make_control_law(dhdu, controls)
    assert control_law == [{controls[0]._sym: sympify2('-2*atan((lamX*v - sqrt(g**2*lamV**2 + 2*g*lamV*lamY*v + lamX**2*v**2 + lamY**2*v**2))/(g*lamV + lamY*v))')},
                           {controls[0]._sym: sympify2('-2*atan((lamX*v + sqrt(g**2*lamV**2 + 2*g*lamV*lamY*v + lamX**2*v**2 + lamY**2*v**2))/(g*lamV + lamY*v))')}]

def test_compile_equations(tmpdir):
    workspace = {'mult': 2}

    code_mod = create_module('test_problem')

    # Write test template file
    code_file = tmpdir.mkdir("templates").join('test.py.mu')
    test_code_tmpl = """def test(foo):
    return foo*{{mult}}"""
    code_file.write(test_code_tmpl)

    # Check if codee generation works
    out_code = load_eqn_template(workspace, str(code_file))

    test_code_expected = """def test(foo):
    return foo*2"""
    assert out_code == test_code_expected
    # Check if code compilation works
    out_fn = compile_code_py(out_code, code_mod, 'test')
    assert out_fn(3) == 6
