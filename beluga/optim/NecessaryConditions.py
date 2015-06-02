
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import pystache, imp, re

from beluga import bvpsol
import beluga.bvpsol.BVP

# import beluga.Beluga as Beluga
from beluga.utils import keyboard
from beluga.optim.problem import *

class NecessaryConditions(object):
    """Defines necessary conditions of optimality."""

    # pystache renderer without HTML escapes
    renderer = pystache.Renderer(escape=lambda u: u)

    def __init__(self, problem):
        """Initializes all of the relevant necessary conditions."""
        self.aug_cost = {}
        self.costates = []
        self.states = []
        self.costate_rate = []
        self.ham = '0'
        self.ham_ctrl_partial = []
        self.ctrl_free = []
        self.bc = BoundaryConditions()
        self.problem = problem

        from .. import Beluga # helps prevent cyclic imports
        self.compile_list = ['deriv_func','bc_func','compute_control']
        self.template_prefix = Beluga.config['root']+'/beluga/bvpsol/templates/'
        self.template_suffix = '.tmpl.py'
        self.states   = self.process_systems()

    def make_costate_rate(self, states):
        self.costate_rate = [str(diff(parse_expr(
        '-1*(' + self.ham + ')'),state)) for state in states]
        # self.costate_rate.append(str(diff(parse_expr(
        # '-1*(' + self.ham + ')'),state)))

    def make_ctrl_partial(self, controls):
        self.ham_ctrl_partial = [diff(parse_expr(self.ham),ctrl) for ctrl in controls]
        # self.ham_ctrl_partial.append(str(diff(parse_expr(self.ham),
        #     symbols(ctrl))))

    def make_ctrl(self, controls):
        # Solve all controls simultaneously
        ctrl_free_sym = solve(self.ham_ctrl_partial,controls,dict=True)


        # solve() returns answer in the form
        # [ {ctrl1: expr11, ctrl2:expr22},
        #   {ctrl1: expr21, ctrl2:expr22}]
        # Convert this to format required by template
        self.control_options = [{'name':str(ctrl), 'expr':str(expr)}
                                    for option in ctrl_free_sym
                                    for (ctrl,expr) in option.items()]


    def make_aug_cost(self,aug_cost, constraint,location):
        ind = 0

        #TODO: Refactor code to use 'join' and list comprehension
        for i in range(len(constraint)):
            if constraint[i].type is location:
                ind += 1
                aug_cost += ' + ' + constraint[i].make_aug_cost(ind)
        self.aug_cost[location] = aug_cost

    def make_costate_bc(self, state, location):
        if location is 'init':
            sign = '-'
        elif location is 'term':
            sign = ''

        for i in range(len(state)):
            self.bc.init.append(
                diff(parse_expr(sign + '(' + self.aug_cost[location] + ')'),
                state[i].sym))

    def make_ham(self, problem):
        self.ham = problem.cost['path'].expr
        for i in range(len(problem.states())):
            self.ham += ' + ' + self.costates[i] + '*' + \
                problem.states()[i].process_eqn

    # Compiles a function template file into a function object
    # using the given data
    def compile_function(self,filename,verbose=False):
        """Compiles a function specified by filename and stores it in
        self.compiled

        Returns:
            bool: True if successful

        Raises:
            ValueError: If 'problem_data' or 'compiled' is not defined
        """
        with open(filename) as f:
            tmpl = f.read()

            if self.problem_data is None:
                raise ValueError('Problem data not defined. Unable to compile function.')

            if self.compiled is None:
                raise ValueError('Problem module not defined. Unable to compile function.')

            # Render the template using the data
            code = self.renderer.render(tmpl,self.problem_data)
            if verbose:
                print(code)

            # For security
            self.compiled.__dict__.update({'__builtin__':{}})
            return exec(code,self.compiled.__dict__)


    def sanitize_constraint(self,constraint):
        if constraint.type == 'initial':
            pattern = r'([\w\d\_]+)_0'
            prefix = '_x0'
        elif constraint.type == 'terminal':
            pattern = r'([\w\d\_]+)_f'
            prefix = '_xf'
        else:
            raise ValueError('Invalid constraint type')

        m = re.findall(pattern,constraint.expr)
        invalid = [x for x in m if x[0] not in self.problem.states()]

        if not all(x is None for x in invalid):
            raise ValueError('Invalid expression in boundary constraint')

        constraint.expr = re.sub(pattern,prefix+r"['\1']",constraint.expr)
        return constraint

    def process_systems(self):
        """Traverses dynamic systems list and extracts information"""
        for (system_type,system_list) in self.problem.systems.items():
            for idx,system_inst in enumerate(system_list):
                # new_states = [state.add_prefix(system_type+'_'+str(idx)+'_')
                #                 for state in system_inst.states]
                new_states = [state
                                for state in system_inst.states]
        # print(new_states)


    def get_bvp(self):
        """Perform variational calculus calculations on optimal control problem
           and returns an object describing the boundary value problem to be solved

        Returns: bvpsol.BVP object
        """

        # Should this be moved into __init__ ?
        self.process_systems()

        ## Create costate list
        for i in range(len(self.problem.states())):
            self.costates.append(self.problem.states()[i].make_costate())

        # Build augmented cost strings
        aug_cost_init = self.problem.cost['init'].expr
        self.make_aug_cost(aug_cost_init,self.problem.constraints(),'init')

        aug_cost_term = self.problem.cost['term'].expr
        self.make_aug_cost(aug_cost_term,self.problem.constraints(),'term')

        # Compute costate conditions
        self.make_costate_bc(self.problem.states(),'init')
        self.make_costate_bc(self.problem.states(),'term')

        ## Unconstrained arc calculations
        # Construct Hamiltonian
        self.make_ham(self.problem)

        # Compute costate process equations
        self.make_costate_rate(self.problem.states())

        # for i in range(len(self.problem.states())):
        #     self.make_costate_rate(self.problem.states()[i].state_var)

        # Compute unconstrained control partial
        # for i in range(len(self.problem.controls())):
            # self.make_ctrl_partial(self.problem.controls()[i].var)

        # TODO(thomas): Combine into a single control computation method?
        self.make_ctrl_partial(self.problem.controls())
        self.make_ctrl(self.problem.controls())
        # Compute unconstrained control law (need to add singular arc and bang/bang smoothing, numerical solutions)
        # for i in range(len(self.problem.controls())):
        #     self.make_ctrl(self.problem.controls()[i].var, i)

        # self.control_options = []
        #
        # for i in range(len(self.problem.controls())):
        #     for j in range(len(self.ctrl_free)):
        #         self.control_options.append([{'name':self.problem.controls()[i].var,'expr':self.ctrl_free[j]}])

        # Create problem dictionary
        # ONLY WORKS FOR ONE CONTROL
        # NEED TO ADD BOUNDARY CONDITIONS

        initial_bc = self.problem.constraints().get('initial')
        terminal_bc = self.problem.constraints().get('terminal')

        # bc1 = [self.sanitize_constraint(x) for x in initial_bc]

        self.problem_data = {
        'aux_list': [
                {
                'type' : 'const',
                'vars': [self.problem.constants()[i].var for i in range(len(self.problem.constants()))]
                },
                {
                'type' : 'constraint',
                'vars': []
                }
         ],
         'state_list':
             [self.problem.states()[i].state_var for i in range(len(self.problem.states()))] +
            #  [self.costates[i] for i in range(len(self.costate))] +
             [costate for costate in self.costates] +
             ['tf']
         ,
         'deriv_list':
             ['tf*(' + self.problem.states()[i].process_eqn + ')' for i in range(len(self.problem.states()))] +
             ['tf*(' + self.costate_rate[i] + ')' for i in range(len(self.costate_rate))] +
             ['tf*0']
         ,
         'num_states': 2*len(self.problem.states()) + 1,


         # Compute these automatically?
        #  'left_bc_list':[self.sanitize_constraint(x).expr for x in initial_bc]+self.bc.init,
        #  'right_bc_list':[self.sanitize_constraint(x).expr for x in terminal_bc]+self.bc.term,
        #  'left_bc_list':initial_bc,
         'left_bc_list':[
             "x - _x0['x']", # x(0
             "y - _x0['y']", # y(0)
             "v - _x0['v']"
         ],
         'right_bc_list':[
             "x - _xf['x']", # x(tf)
             "y - _xf['y']", # y(tf)
             "lagrange_v + 0.0",   # lamV(tf)
             "_H     - 0",     # H(tf)
         ],
         'control_options': self.control_options,
         'control_list':[self.problem.controls()[i].var for i in range(len(self.problem.controls()))],
         'ham_expr':self.ham
        }

    #    problem.constraints[i].expr for i in range(len(problem.constraints))

        # Create problem functions by importing from templates
        self.compiled = imp.new_module('brachisto_prob')
        compile_result = [self.compile_function(self.template_prefix+func+self.template_suffix, verbose=True) for func in self.compile_list]

        # Make this generic for BCs, constants and constraints
        self.bvp = bvpsol.BVP(self.compiled.deriv_func,self.compiled.bc_func,
                        initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                        terminal_bc = {'x':0.1, 'y':-0.1},
                        const = {'g':9.81},
                        constraint = {}
                    )
        return self.bvp

class BoundaryConditions(object):
    """Defines boundary condtiions."""

    def __init__(self):
        self.init = []
        self.term = []
