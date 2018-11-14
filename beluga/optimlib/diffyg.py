from sympy.diffgeom import Manifold as sympyManifold
from sympy.diffgeom import Patch, CoordSystem, Differential, covariant_order, WedgeProduct
from sympy.printing import pprint
from sympy.simplify import simplify
import logging
import numpy as np
import itertools as it
from .optimlib import *

def ocp_to_bvp(ocp, guess):
    ws = init_workspace(ocp, guess)
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
    constants_of_motion_units = ws['constants_of_motion_units']
    symmetries = ws['symmetries']
    constraints = ws['constraints']
    constraints_units = ws['constraints_units']
    quantities = ws['quantities']
    quantities_values = ws['quantities_values']
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

    dynamical_parameters = []

    quantity_vars, quantity_list, derivative_fn = process_quantities(quantities, quantities_values)
    Q = Manifold(states, 'State_Space')
    E = Manifold(states + controls, 'Input_Space')
    R = Manifold([independent_variable], 'Independent_Space')
    tau_Q = FiberBundle(Q, R, 'State_Bundle')
    tau_E = FiberBundle(E, R, 'Input_Bundle')
    J1tau_Q = JetBundle(tau_Q, 1, 'Jet_Bundle')
    num_states = len(states)
    num_states_total = len(J1tau_Q.vertical.base_coords)

    hamiltonian, hamiltonian_units, costates, costates_units = make_hamiltonian(states, states_rates, states_units, path_cost, cost_units)
    setx = dict(zip(states + costates, J1tau_Q.vertical.base_coords))
    vector_names = [Symbol('D_' + str(x)) for x in states]
    settangent = dict(zip(vector_names, J1tau_Q.vertical.base_vectors[:num_states]))

    # Change original terms to be written on manifolds so the diffy g calculations are handled properly
    states = [x.subs(setx, simultaneous=True) for x in states]
    states_rates = [x.subs(setx, simultaneous=True) for x in states_rates]
    costates = J1tau_Q.vertical.base_coords[num_states:]
    constants_of_motion_values = [x.subs(setx, simultaneous=True) for x in constants_of_motion_values]
    symmetries = [x.subs(setx, simultaneous=True) for x in symmetries]
    symmetries = [x.subs(settangent, simultaneous=True) for x in symmetries]
    constraints['initial'] = [x.subs(setx, simultaneous=True) for x in constraints['initial']]
    constraints['terminal'] = [x.subs(setx, simultaneous=True) for x in constraints['terminal']]
    initial_cost = initial_cost.subs(setx, simultaneous=True)
    terminal_cost = terminal_cost.subs(setx, simultaneous=True)

    pi = 0
    for ii in range(num_states):
        pi += WedgeProduct(J1tau_Q.base_vectors[ii], J1tau_Q.base_vectors[ii + num_states])

    hamiltonian = 1
    for ii in range(num_states):
        hamiltonian += states_rates[ii] * J1tau_Q.base_coords[ii + num_states]

    def X_(arg):
        return pi.rcall(None, arg)

    do_stage1_reduction = False
    do_stage2_reduction = False
    quadratures_list = []
    if len(constants_of_motion) > 0:
        do_stage1_reduction = True
        logging.info('Checking commutation relations... ')
        commutation_relations = []
        for c1, c2 in it.product(constants_of_motion_values, constants_of_motion_values):
            commutation_relations.append(pi.rcall(c1,c2))

        commutation_relations_valid = [False]*len(commutation_relations)
        for ii in range(len(commutation_relations)):
            if commutation_relations[ii] == 0:
                commutation_relations_valid[ii] = True

        logging.info('Done.')
        if all(commutation_relations_valid):
            do_stage2_reduction = True
        else:
            logging.warning('Commutation relations do not vanish. Skipping stage 2 reduction.')

    # TODO: Overriding the reductions. Implement these later
    do_stage2_reduction = False

    reduction_1_success = False
    reduced_states = states + costates
    if do_stage1_reduction:
        free_vars = set()
        for c in constants_of_motion_values:
            free_vars |= c.atoms(states[0])

        logging.info('Attempting simultaneous stage 1 reduction... ')

        eq_set = [constants_of_motion[ii] - constants_of_motion_values[ii] for ii in range(len(constants_of_motion))]
        constants_sol = sympy.solve(eq_set, list(free_vars), dict=False, minimal=True, simplify=False)
        reduced_states = []
        reduced_vectors = []
        reduced_forms = []
        removed_states = []
        removed_vectors = []
        removed_forms = []
        for ii, x in enumerate(states + costates):
            if x in constants_sol.keys():
                removed_states.append(x)
                removed_vectors.append(J1tau_Q.vertical.base_vectors[ii])
                removed_forms.append(J1tau_Q.vertical.base_oneforms[ii])
            else:
                reduced_states.append(x)
                reduced_vectors.append(J1tau_Q.vertical.base_vectors[ii])
                reduced_forms.append(J1tau_Q.vertical.base_oneforms[ii])

        for c in constants_sol.keys():
            dynamical_parameters.append(c)

        hamiltonian = hamiltonian.subs(constants_sol, simultaneous=True)
        pi = pi.subs(constants_sol, simultaneous=True) # TODO: Also change the vectors and differential forms
        reduction_1_success = True
        logging.info('Done.')

        if do_stage2_reduction:
            raise NotImplementedError
        else:
            logging.info('Skipping stage 2 reduction.')
    else:
        logging.info('Skipping stage 1 and 2 reductions.')

    equations_of_motion = pi.rcall(None, hamiltonian)
    if reduction_1_success:
        equations_of_motion_list = []
        for D_x in reduced_vectors:
            equations_of_motion_list.append(J1tau_Q.flat(equations_of_motion).rcall(D_x))
    else:
        equations_of_motion_list = [J1tau_Q.flat(equations_of_motion).rcall(D_x) for D_x in J1tau_Q.vertical.base_vectors]

    augmented_initial_cost, augmented_initial_cost_units, initial_lm_params, initial_lm_params_units = make_augmented_cost(initial_cost, cost_units, constraints, constraints_units, location='initial')
    augmented_terminal_cost, augmented_terminal_cost_units, terminal_lm_params, terminal_lm_params_units = make_augmented_cost(terminal_cost, cost_units, constraints, constraints_units, location='terminal')

    # for var in quantity_vars.keys():
    #     hamiltonian = hamiltonian.subs(Symbol(var), quantity_vars[var])
    dV_cost_initial = J1tau_Q.verticalexteriorderivative(augmented_initial_cost)
    dV_cost_terminal = J1tau_Q.verticalexteriorderivative(augmented_terminal_cost)
    bc_initial = constraints['initial'] + [costate + dV_cost_initial.rcall(D_x) for costate, D_x in zip(costates, J1tau_Q.vertical.base_vectors[:num_states])]
    bc_terminal = constraints['terminal'] + [costate - dV_cost_terminal.rcall(D_x) for costate, D_x in zip(costates, J1tau_Q.vertical.base_vectors[:num_states])]
    bc_terminal = make_time_bc(constraints, hamiltonian, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    nond_parameters = initial_lm_params + terminal_lm_params
    control_law = make_control_law(dHdu, controls)

    # Generate the problem data
    control_law = [{str(u): str(law[u]) for u in law.keys()} for law in control_law]
    tf_var = sympify('tf')
    dynamical_parameters = [tf_var] + parameters
    dynamical_parameters_units = [independent_variable_units] + parameters_units
    nondynamical_parameters = initial_lm_params + terminal_lm_params
    nondynamical_parameters_units = initial_lm_params_units + terminal_lm_params_units

    out = {'method': 'diffyg',
           'problem_name': problem_name,
           'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
           'states': [str(x) for x in it.chain(states, costates)],
           'states_units': [str(x) for x in states_units + costates_units],
           'deriv_list': [str(tf_var * rate) for rate in equations_of_motion_list],
           'constants': [str(c) for c in constants],
           'constants_units': [str(c) for c in constants_units],
           'constants_values': [float(c) for c in constants_values],
           'constants_of_motion': [str(c) for c in constants_of_motion],
           'dynamical_parameters': [str(c) for c in dynamical_parameters],
           'dynamical_parameters_units': [str(c) for c in dynamical_parameters_units],
           'nondynamical_parameters': [str(c) for c in nondynamical_parameters],
           'nondynamical_parameters_units': [str(c) for c in nondynamical_parameters_units],
           'independent_variable': str(independent_variable),
           'independent_variable_units': str(independent_variable_units),
           'control_list': [str(x) for x in it.chain(controls)],
           'controls': [str(u) for u in controls],
           'hamiltonian': str(hamiltonian),
           'hamiltonian_units': str(hamiltonian_units),
           'num_states': 2 * len(states),
           'dHdu': str(dHdu),
           'bc_initial': [str(_) for _ in bc_initial],
           'bc_terminal': [str(_) for _ in bc_terminal],
           'control_options': control_law,
           'num_controls': len(controls)}
    return out

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

    def __init__(self, *args, verbose=False):
        logging.info('The manifold \'{}\' has been created'.format(self.name))
        self.base_coords = self._coordsystem.coord_functions()
        logging.info('The following coordinates have been created: ' + str(self.base_coords))
        self.base_vectors = self._coordsystem.base_vectors()
        logging.info('The following base vectors have been created: ' + str(self.base_vectors))
        self.base_oneforms = self._coordsystem.base_oneforms()
        logging.info('The following base one forms have been created: ' + str(self.base_oneforms))

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
        super(FiberBundle, self).__init__(*args, verbose=verbose)

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


# TODO: Delete this?
# class SymplecticManifold(Manifold):
#     def __new__(cls, *args, verbose=False):
#         obj = super(SymplecticManifold, cls).__new__(cls, *args, verbose=verbose)
#         if obj.dimension % 2 == 1:
#             raise ValueError
#         obj.symplecticform = 0
#         return obj
#
#     def __init__(self, *args, verbose=False):
#         super(SymplecticManifold, self).__init__(*args, verbose=verbose)
#         d = int(self.dimension/2)
#         self.symplecticform = sum([WedgeProduct(dx,dy) for (dx, dy) in zip(self.base_oneforms[:d], self.base_oneforms[d:])])


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
    logging.info("Attempting using SymPy (v" + __version__ + ")...")
    logging.debug("dHdu = " + str(dhdu))
    ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)
    logging.info('Control found')
    logging.debug(ctrl_sol)
    control_options = ctrl_sol
    return control_options
