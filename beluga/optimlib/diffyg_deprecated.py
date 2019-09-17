from sympy.diffgeom import Manifold as sympyManifold
from sympy.diffgeom import Patch, CoordSystem, Differential, covariant_order, WedgeProduct, TensorProduct
import copy
import logging
from beluga.ivpsol import Trajectory
from beluga.codegen import make_jit_fn
import numpy as np
import itertools as it
from .optimlib import *


def ocp_to_bvp(ocp, **kwargs):
    """
    Converts an OCP to a BVP using diffy G methods.

    :param ocp: An OCP.
    :return: bvp, map, map_inverse
    """

    logging.warning('\'diffyg_deprecated\' method is deprecated and will be removed in a later version, use \'indirect\'.')

    ws = init_workspace(ocp)
    problem_name = ws['problem_name']
    independent_variable = ws['independent_var']
    independent_variable_units = ws['independent_var_units']
    states = ws['states']
    states_rates = ws['states_rates']
    states_units = ws['states_units']
    controls = ws['controls']
    controls_units = ws['controls_units']
    constants = ws['constants']
    constants_units = ws['constants_units']
    constants_values = ws['constants_values']
    constants_of_motion = ws['constants_of_motion']
    constants_of_motion_values = ws['constants_of_motion_values']
    constants_of_motion_values_original = copy.deepcopy(constants_of_motion_values)
    constants_of_motion_units = ws['constants_of_motion_units']
    symmetries = ws['symmetries']
    constraints = ws['constraints']
    constraints_units = ws['constraints_units']
    constraints_lower = ws['constraints_lower']
    constraints_upper = ws['constraints_upper']
    constraints_activators = ws['constraints_activators']
    constraints_method = ws['constraints_method']
    switches = ws['switches']
    switches_values = ws['switches_values']
    switches_conditions = ws['switches_conditions']
    switches_tolerance = ws['switches_tolerance']
    parameters = ws['parameters']
    parameters_units = ws['parameters_units']
    initial_cost = ws['initial_cost']
    initial_cost_units = ws['initial_cost_units']
    terminal_cost = ws['terminal_cost']
    terminal_cost_units = ws['terminal_cost_units']
    path_cost = ws['path_cost']
    path_cost_units = ws['path_cost_units']

    if initial_cost != 0:
        cost_units = initial_cost_units
    elif terminal_cost != 0:
        cost_units = terminal_cost_units
    elif path_cost != 0:
        cost_units = path_cost_units*independent_variable_units
    else:
        raise ValueError('Initial, path, and terminal cost functions are not defined.')

    """
    Deal with path constraints
    """
    for ii, c in enumerate(constraints['path']):
        if constraints_method['path'] is None:
            raise NotImplementedError

        if constraints_method['path'][ii].lower() == 'utm':
            path_cost += utm_path(c, constraints_lower['path'][ii], constraints_upper['path'][ii],
                                  constraints_activators['path'][ii])
        elif constraints_method['path'][ii].lower() == 'epstrig':
            path_cost += epstrig_path(c, constraints_lower['path'][ii], constraints_upper['path'][ii],
                                  constraints_activators['path'][ii])
            upper = constraints_upper['path'][ii]
            lower = constraints_lower['path'][ii]
            subber = dict(zip([constraints['path'][ii]], [(upper - lower)/2*sympy.sin(constraints['path'][ii]) + (upper+lower)/2]))
            for ii in range(len(states_rates)):
                states_rates[ii] = states_rates[ii].subs(subber, simultaneous=True)
        else:
            raise NotImplementedError('Unknown path constraint method \"' + str(constraints_method['path'][ii]) + '\"')

    dynamical_parameters = []

    """
    Deal with staging and switches
    """
    for ii in range(len(switches)):
        if isinstance(switches_values[ii], list):
            true_value = 0
            for jj in range(len(switches_values[ii])):
                temp_value = switches_values[ii][jj]
                for kk in range(len(switches_conditions[ii][jj])):
                    temp_value *= rash_mult(switches_conditions[ii][jj][kk], switches_tolerance[ii])
                true_value += temp_value
            switches_values[ii] = true_value

    """
    Make substitutions with the switches
    """
    switch_vars, switch_list, derivative_fn = process_quantities(switches, switches_values)
    for var in switch_vars.keys():
        initial_cost = initial_cost.subs(Symbol(var), switch_vars[var])
        path_cost = path_cost.subs(Symbol(var), switch_vars[var])
        terminal_cost = terminal_cost.subs(Symbol(var), switch_vars[var])
        for ii in range(len(states_rates)):
            states_rates[ii] = states_rates[ii].subs(Symbol(var), switch_vars[var])

    Q = Manifold(states, 'State_Space')
    E = Manifold(states + controls, 'Input_Space')
    R = Manifold([independent_variable], 'Independent_Space')
    tau_Q = FiberBundle(Q, R, 'State_Bundle')
    tau_E = FiberBundle(E, R, 'Input_Bundle')
    J1tau_Q = JetBundle(tau_Q, 1, 'Jet_Bundle')
    num_states = len(states)
    num_states_total = len(J1tau_Q.vertical.base_coords)

    hamiltonian, hamiltonian_units, costates, costates_units = make_hamiltonian(states, states_rates, states_units,
                                                                                path_cost, cost_units)

    setx = dict(zip(states + costates, J1tau_Q.vertical.base_coords))
    vector_names = [Symbol('D_' + str(x)) for x in states]
    settangent = dict(zip(vector_names, J1tau_Q.vertical.base_vectors[:num_states]))

    # Change original terms to be written on manifolds so the diffy g calculations are handled properly
    states = [x.subs(setx, simultaneous=True) for x in states]
    states_rates = [x.subs(setx, simultaneous=True) for x in states_rates]
    costates = J1tau_Q.vertical.base_coords[num_states:]
    constants_of_motion_values = [x.subs(setx, simultaneous=True) for x in constants_of_motion_values]
    constants_of_motion_values_original = [x.subs(setx, simultaneous=True) for x in constants_of_motion_values_original]
    symmetries = [x.subs(setx, simultaneous=True) for x in symmetries]
    symmetries = [x.subs(settangent, simultaneous=True) for x in symmetries]
    constraints['initial'] = [x.subs(setx, simultaneous=True) for x in constraints['initial']]
    constraints['terminal'] = [x.subs(setx, simultaneous=True) for x in constraints['terminal']]
    initial_cost = initial_cost.subs(setx, simultaneous=True)
    terminal_cost = terminal_cost.subs(setx, simultaneous=True)

    hamiltonian = hamiltonian.subs(setx, simultaneous=True)
    dhdt = derivative_fn(hamiltonian, independent_variable)
    # if dhdt == 0:
    #     constants_of_motion = constants_of_motion + [Symbol('hamiltonian')]
    #     constants_of_motion_values = constants_of_motion_values + [hamiltonian]
    #     constants_of_motion_units = constants_of_motion_units + [hamiltonian_units]

    coparameters = make_costate_names(parameters)
    coparameters_units = [path_cost_units / parameter_units for parameter_units in parameters_units]
    coparameters_rates = make_costate_rates(hamiltonian, parameters, coparameters, derivative_fn)

    quads = []
    quads_rates = []
    quads_units = []
    quads += coparameters
    quads_rates += coparameters_rates
    quads_units += coparameters_units

    pi = 0
    omega = 0
    for ii in range(num_states):
        # pi += WedgeProduct(J1tau_Q.base_vectors[ii], J1tau_Q.base_vectors[ii + num_states])
        pi += TensorProduct(J1tau_Q.base_vectors[ii], J1tau_Q.base_vectors[ii + num_states]) - \
              TensorProduct(J1tau_Q.base_vectors[ii + num_states], J1tau_Q.base_vectors[ii])
        omega += WedgeProduct(J1tau_Q.base_oneforms[ii], J1tau_Q.base_oneforms[ii + num_states])

    state_costate_pairing = 0
    for ii in range(num_states):
        state_costate_pairing += TensorProduct(J1tau_Q.base_coords[ii + num_states]*J1tau_Q.base_vectors[ii]) + \
                                 TensorProduct(J1tau_Q.base_coords[ii]*J1tau_Q.base_vectors[ii + num_states])

    constant_2_units = {c: u for c, u in zip(constants_of_motion, constants_of_motion_units)}

    reduced_states = states + costates
    original_states = copy.copy(reduced_states)
    reduced_states_units = states_units + costates_units
    state_2_units = {x: u for x, u in zip(reduced_states, reduced_states_units)}

    X_H = pi.rcall(None, hamiltonian)
    equations_of_motion = [X_H.rcall(x) for x in J1tau_Q.vertical.base_coords]

    augmented_initial_cost, augmented_initial_cost_units, initial_lm_params, initial_lm_params_units =\
        make_augmented_cost(initial_cost, cost_units, constraints, constraints_units, location='initial')
    augmented_terminal_cost, augmented_terminal_cost_units, terminal_lm_params, terminal_lm_params_units =\
        make_augmented_cost(terminal_cost, cost_units, constraints, constraints_units, location='terminal')

    dV_cost_initial = J1tau_Q.verticalexteriorderivative(augmented_initial_cost)
    dV_cost_terminal = J1tau_Q.verticalexteriorderivative(augmented_terminal_cost)
    bc_initial = constraints['initial'] + \
        [costate + dV_cost_initial.rcall(D_x) for costate, D_x
         in zip(costates, J1tau_Q.vertical.base_vectors[:num_states])] + \
        [coparameter - derivative_fn(augmented_initial_cost, parameter) for parameter, coparameter
         in zip(parameters, coparameters)]
    bc_terminal = constraints['terminal'] + \
        [costate - dV_cost_terminal.rcall(D_x) for costate, D_x
         in zip(costates, J1tau_Q.vertical.base_vectors[:num_states])] + \
        [coparameter - derivative_fn(augmented_terminal_cost, parameter) for parameter, coparameter
         in zip(parameters, coparameters)]
    time_bc = make_time_bc(constraints, derivative_fn, hamiltonian, independent_variable)

    if time_bc is not None:
        bc_terminal += [time_bc]
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    control_law = make_control_law(dHdu, controls)

    tf = sympify('_tf')
    # bc_terminal = [bc.subs(independent_variable, tf, simultaneous=True) for bc in bc_terminal]
    dynamical_parameters = parameters + [tf]
    dynamical_parameters_units = parameters_units + [independent_variable_units]
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units

    subalgebras = []
    if len(constants_of_motion) > 0:
        logging.debug('Checking commutation relations... ')
        num_consts = len(constants_of_motion)

        commutation_relations = [[None for _ in range(num_consts)] for _ in range(num_consts)]
        for ii, c1 in enumerate(constants_of_motion_values):
            for jj, c2 in enumerate(constants_of_motion_values):
                commutation_relations[ii][jj] = pi.rcall(c1, c2)

        for ii, c1 in enumerate(constants_of_motion_values):
            subalgebras.append({constants_of_motion[ii]})
            for jj in range(0, num_consts):
                if commutation_relations[ii][jj] != 0:
                    subalgebras[-1] |= {constants_of_motion[jj]}

        subalgebras = [gs for ii, gs in enumerate(subalgebras) if gs not in subalgebras[ii+1:]]
        reducible_subalgebras = [len(gs) == 1 for gs in subalgebras]
        logging.debug('Done. ' + str(sum(reducible_subalgebras)) + ' of ' + str(len(subalgebras))
                     + ' subalgebras are double reducible.')

    for subalgebra in subalgebras:
        constant_2_value = {c: v for c, v in zip(constants_of_motion, constants_of_motion_values)}
        dim = len(subalgebra)
        if dim > 1:
            raise NotImplementedError
        # G_name = 'G_' + str(subalgebra).replace('{','').replace('}','')
        # G = LieGroup(list(subalgebra), G_name)
        # h = constant_2_value[constants_of_motion[0]]

        logging.debug('Attempting reduction of ' + str(subalgebra) + '...')
        # M_r, phi = restrictor(M, dict([(x, constant_2_value[x]) for x in list(subalgebra)]))
        free_vars = set()
        const = dict([(x, constant_2_value[x]) for x in list(subalgebra)])
        for c in const.keys():
            free_vars |= const[c].atoms(reduced_states[0])

        eq_set = [c - const[c] for c in const.keys()]
        constants_sol = sympy.solve(eq_set, list(free_vars), dict=True, minimal=True, simplify=False)[0]

        # hamiltonian = phi.pullback(hamiltonian)

        # g_ii = 0
        # for ii in range(len(M_r.base_coords)):
        #     for jj in range(len(M_r.base_coords)):
        #         g_ii += TensorProduct(M_r.base_oneforms[ii], M_r.base_oneforms[jj])
        # omega = phi.pullback(omega)
        # # pi = M_r.sharp(omega)
        # constants_of_motion = [phi.pullback(c) for c in constants_of_motion]
        # dH = M_r.exteriorderivative(hamiltonian)
        # eoms = omega.rcall(None, M_r.sharp(dH))
        # breakpoint()
        # eps_c = omega.rcall(None, M_r.sharp(M_r.exteriorderivative(constants_of_motion[0])))
        # quad_field = eoms.rcall(M_r.sharp(omega.rcall(None, constants_of_motion[0])))
        # breakpoint()
        #
        # breakpoint()
        for x in constants_sol:
            reduced_states.remove(x)
            quads.append(state_costate_pairing.rcall(x))
            quant = [constant_2_value[c] for c in subalgebra][0]
            quads_rates.append(J1tau_Q.flat(X_H).rcall(pi.rcall(None, quant)))
            quads_units.append(state_2_units[state_costate_pairing.rcall(x)])
            reduced_states.remove(state_costate_pairing.rcall(x))

        temp = copy.copy(subalgebra)
        temp2 = copy.copy(temp)
        dynamical_parameters.append(temp.pop())
        dynamical_parameters_units.append(constant_2_units[temp2.pop()])

        hamiltonian = hamiltonian.subs(constants_sol, simultaneous=True)
        pi = pi.subs(constants_sol, simultaneous=True)  # TODO: Also change the vectors and differential forms
        X_H = pi.rcall(None, hamiltonian)
        equations_of_motion = [X_H.rcall(x) for x in reduced_states]

        for ii in range(len(quads_rates)):
            quads_rates[ii] = quads_rates[ii].subs(constants_sol, simultaneous=True)

        for ii in range(len(control_law)):
            for control in control_law[ii]:
                control_law[ii][control] = control_law[ii][control].subs(constants_sol, simultaneous=True)

        for ii in range(len(constants_of_motion_values)):
            constants_of_motion_values[ii] = constants_of_motion_values[ii].subs(constants_sol, simultaneous=True)

        for ii in range(len(bc_initial)):
            bc_initial[ii] = bc_initial[ii].subs(constants_sol, simultaneous=True)

        for ii in range(len(bc_terminal)):
            bc_terminal[ii] = bc_terminal[ii].subs(constants_sol, simultaneous=True)

        logging.debug('Done.')

    # Generate the problem data
    control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
    out = {'method': 'diffyg',
           'problem_name': problem_name,
           'control_method': '',
           'consts': [str(k) for k in constants],
           'initial_cost': None,
           'initial_cost_units': None,
           'path_cost': None,
           'path_cost_units': None,
           'terminal_cost': None,
           'terminal_cost_units': None,
           'states': [str(x) for x in reduced_states],
           'states_units': [str(state_2_units[x]) for x in reduced_states],
           'states_rates': [str(tf * rate) for rate in equations_of_motion],
           'states_jac': [None, None],
           'quads': [str(x) for x in quads],
           'quads_rates': [str(tf * x) for x in quads_rates],
           'quads_units': [str(x) for x in quads_units],
           'path_constraints': [],
           'path_constraints_units': [],
           'constants': [str(c) for c in constants],
           'constants_units': [str(c) for c in constants_units],
           'constants_values': [float(c) for c in constants_values],
           'constants_of_motion': [str(c) for c in constants_of_motion],
           'dynamical_parameters': [str(c) for c in dynamical_parameters],
           'dynamical_parameters_units': [str(c) for c in dynamical_parameters_units],
           'nondynamical_parameters': [str(c) for c in nondynamical_parameters],
           'nondynamical_parameters_units': [str(c) for c in nondynamical_parameters_units],
           'control_list': [str(x) for x in it.chain(controls)],
           'controls': [str(u) for u in controls],
           'hamiltonian': str(hamiltonian),
           'hamiltonian_units': str(hamiltonian_units),
           'num_states': len(reduced_states),
           'dHdu': [str(x) for x in dHdu],
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'control_options': control_law,
           'num_controls': len(controls)}

    states_2_constants_fn = [make_jit_fn([str(x) for x in original_states + controls], str(c))
                             for c in constants_of_motion_values_original]
    states_2_reduced_states_fn = [make_jit_fn([str(x) for x in original_states], str(y)) for y in reduced_states]

    constants_2_states_fn = [make_jit_fn([str(x) for x in reduced_states + constants_of_motion], str(y))
                             for y in constants_of_motion]

    def guess_map(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        nodes = len(sol.t)
        n_c = len(constants_of_motion)
        sol_out.t = copy.copy(sol.t / sol.t[-1])
        sol_out.y = np.array([[fn(*sol.y[ii], *sol.dual[ii]) for fn in states_2_reduced_states_fn]
                              for ii in range(sol.t.size)])
        sol_out.q = sol.q
        if len(quads) > 0:
            sol_out.q = -0.0*np.array([np.ones((len(quads)))])
        sol_out.dynamical_parameters = np.hstack((sol.dynamical_parameters, sol.t[-1],
                                                  np.array([fn(*sol.y[0], *sol.dual[0], *sol.u[0])
                                                            for fn in states_2_constants_fn])))
        sol_out.nondynamical_parameters = np.ones(len(nondynamical_parameters))
        sol_out.u = np.array([]).reshape((nodes, 0))
        sol_out.const = sol.const
        return sol_out

    def guess_map_inverse(sol, _compute_control=None):
        if _compute_control is None:
            raise ValueError('Guess mapper not properly set up. Bind the control law to keyword \'_compute_control\'')
        sol_out = copy.deepcopy(sol)
        sol_out.u = np.vstack([_compute_control(yi, None, sol.dynamical_parameters, sol.const) for yi in sol.y])
        return sol_out

    return out, guess_map, guess_map_inverse


class Manifold(object):
    def __new__(cls, *args):
        obj = super(Manifold, cls).__new__(cls)
        if len(args) >= 1:
            dependent = args[0]

        if len(args) >= 2:
            name = args[1]
        else:
            name = 'manifold'

        obj.name = name
        obj.dimension = len(dependent)
        obj._manifold = sympyManifold(obj.name, obj.dimension)
        obj._patch = Patch('Atlas', obj._manifold)
        obj._coordsystem = CoordSystem('Coordinates', obj._patch, names=[str(d) for d in dependent])
        return obj

    def __init__(self, *args):
        logging.debug('The manifold \'{}\' has been created'.format(self.name))
        self.base_coords = self._coordsystem.coord_functions()
        logging.debug('The following coordinates have been created: ' + str(self.base_coords))
        self.base_vectors = self._coordsystem.base_vectors()
        logging.debug('The following base vectors have been created: ' + str(self.base_vectors))
        self.base_oneforms = self._coordsystem.base_oneforms()
        logging.debug('The following base one forms have been created: ' + str(self.base_oneforms))

    def sharp(self, f):
        set1d = dict(zip(self.base_oneforms, self.base_vectors))
        return f.subs(set1d, simultaneous=True)

    def flat(self, f):
        set1D = dict(zip(self.base_vectors, self.base_oneforms))
        return f.subs(set1D, simultaneous=True)

    def exteriorderivative(self, f):
        order = covariant_order(f)

        # Automatically return 0 if f's grade is equal to manifold dimension
        if order == self.dimension:
            return 0

        if order == 0:
            return sum([Differential(f)(D_x)*dx for (D_x, dx) in zip(self.base_vectors, self.base_oneforms)])

        # If's f's grade is 1 or higher, we still need to implement this
        if order > 0:
            raise NotImplementedError('Exterior derivative of forms higher order than 1 is not implemented.')


class LieGroup(Manifold):
    pass


class FiberBundle(Manifold):
    def __new__(cls, *args):
        if len(args) < 2:
            raise ValueError('Fiber bundles must be constructed with two manifolds.')

        A = args[0]
        B = args[1]

        if len(args) == 3:
            name = args[2]
        else:
            name = A.name + B.name + '_fiberbundle'

        Ax = [str(x) for x in A.base_coords]
        Bx = [str(x) for x in B.base_coords]

        obj = super(FiberBundle, cls).__new__(cls, Ax + Bx, name)
        obj.vertical = A
        obj.horizontal = B

        return obj

    def __init__(self, *args, verbose=False):
        super(FiberBundle, self).__init__(*args)

        set1x = dict(zip(self.horizontal.base_coords, self.base_coords[self.vertical.dimension:]))
        set1d = dict(zip(self.horizontal.base_oneforms, self.base_oneforms[self.vertical.dimension:]))
        set1D = dict(zip(self.horizontal.base_vectors, self.base_vectors[self.vertical.dimension:]))
        set2x = dict(zip(self.vertical.base_coords, self.base_coords[:self.vertical.dimension]))
        set2d = dict(zip(self.vertical.base_oneforms, self.base_oneforms[:self.vertical.dimension]))
        set2D = dict(zip(self.vertical.base_vectors, self.base_vectors[:self.vertical.dimension]))

        self.horizontal.base_coords = [x.subs(set1x, simultaneous=True) for x in self.horizontal.base_coords]
        self.horizontal.base_oneforms = [d.subs(set1d, simultaneous=True) for d in self.horizontal.base_oneforms]
        self.horizontal.base_vectors = [D.subs(set1D, simultaneous=True) for D in self.horizontal.base_vectors]
        self.vertical.base_coords = [x.subs(set2x, simultaneous=True) for x in self.vertical.base_coords]
        self.vertical.base_oneforms = [d.subs(set2d, simultaneous=True) for d in self.vertical.base_oneforms]
        self.vertical.base_vectors = [D.subs(set2D, simultaneous=True) for D in self.vertical.base_vectors]

    def projection(self, input):
        return input[self.vertical.dimension:]

    def horizontalexteriorderivative(self, f):
        return self.horizontal.exteriorderivative(f)

    def verticalexteriorderivative(self, f):
        return self.vertical.exteriorderivative(f)


class JetBundle(FiberBundle):
    jet_identifier = ''

    def __new__(cls, *args):
        if not isinstance(args[0], FiberBundle):
            raise ValueError('Jet bundles must be constructed from a fiber bundle.')

        if not isinstance(args[1], int):
            raise ValueError('Jet bundles must have a jet order.')

        if len(args) >= 3:
            name = args[2]
        else:
            name = args[0].name + '_jetbundle'

        bundle_input = args[0]

        horizontal = bundle_input.horizontal

        jetorder = args[1]
        ver_dim = len(bundle_input.vertical.base_coords)
        hor_dim = len(bundle_input.horizontal.base_coords)
        base_coords = [str(x) for x in bundle_input.vertical.base_coords]
        coords = [str(x) for x in bundle_input.vertical.base_coords]
        for ii in range(jetorder):
            vals = [list(range(hor_dim)) for _ in range(ii+1)]
            for jord in it.product(*vals):
                for state in base_coords:
                    str_to_append = [str(_) for _ in jord]
                    coords.append(state + cls.jet_identifier + str(cls.jet_identifier.join(str_to_append)))

        vertical = Manifold(coords, 'J' + bundle_input.vertical.name)
        obj = super(JetBundle, cls).__new__(cls, vertical, horizontal, name)

        return obj


def MomentumShift(bundle):
    vertical = Manifold(bundle.vertical.base_coords + bundle.horizontal.base_coords, 'Momentum_Shifted_Vertical')
    tau = Manifold(['_tau'], 'Nondimensionalized_Base')
    bundle2 = FiberBundle(vertical, tau)
    return bundle2


def make_control_law(dhdu, controls):
    r"""
    Solves control equation to get control law.

    .. math::
        \frac{dH}{d\textbf{u}} = 0

    :param dhdu: The expression for :math:`dH / d\textbf{u}`.
    :param controls: A list of control variables, :math:`[u_1, u_2, \cdots, u_n]`.
    :return: Control law options.
    """
    var_list = list(controls)
    from sympy import __version__
    logging.debug("Attempting using SymPy (v" + __version__ + ")...")
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.debug('Control found')
    control_options = ctrl_sol
    return control_options


def restrictor(M, const):
    free_vars = set()
    for c in const.keys():
        free_vars |= const[c].atoms(M.base_coords[0])

    eq_set = [c - const[c] for c in const.keys()]
    constants_sol = sympy.solve(eq_set, list(free_vars), dict=True, minimal=True, simplify=False)
    constants_sol1 = constants_sol[0]

    coords = copy.deepcopy(M.base_coords)
    indices = [ii for ii in range(len(coords))]
    for x in constants_sol1.keys():
        ind = M.base_coords.index(x)
        coords.remove(x)
        indices.remove(ind)

    M_restricted = Manifold(coords, 'M_restricted')
    extras = dict((M.base_coords[indices[ii]], M_restricted.base_coords[ii])
                  for ii in range(len(M_restricted.base_coords)))
    constants_sol1.update(extras)
    mapper = Map(M, M_restricted, constants_sol1)
    return M_restricted, mapper


class Map(object):
    def __new__(cls, source, target, function):
        obj = super(Map, cls).__new__(cls)
        obj.source = source
        obj.target = target
        obj.coord = function
        obj.form = dict()
        for x in function.keys():
            dx0 = obj.source.exteriorderivative(x)
            dxf = obj.target.exteriorderivative(function[x])
            obj.form.update({dx0: dxf})

        return obj

    def pullback(self, func):
        # TODO: Fully implement the pullback operation. I think there's a bug in SymPy 1.3 that is preventing this.
        func = func.subs(self.coord, simultaneous=True)
        func = func.subs(self.form, simultaneous=True)
        return func

    def pushforward(self, func):
        raise NotImplementedError
