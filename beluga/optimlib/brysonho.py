"""
Computes the necessary conditions of optimality using Bryson & Ho's method
"""

from .optimlib import *
from beluga.utils import sympify
import simplepipe as sp
from beluga.utils import keyboard


def ocp_to_bvp(ocp, guess):
    ws = init_workspace(ocp, guess)
    problem_name = ws['problem_name']
    independent_variable = ws['indep_var']
    states = ws['states']
    controls = ws['controls']
    constants = ws['constants']
    constants_of_motion = ws['constants_of_motion']
    constraints = ws['constraints']
    constraints_adjoined = ws['constraints_adjoined']
    path_constraints = ws['path_constraints']
    quantities = ws['quantities']
    initial_cost = ws['initial_cost']
    terminal_cost = ws['terminal_cost']
    path_cost = ws['path_cost']
    quantity_vars, quantity_list, derivative_fn, jacobian_fn = process_quantities(quantities)
    # TODO: Process path constraints here. Ref #51
    mu_vars = []
    s_list = []
    augmented_initial_cost = make_augmented_cost(initial_cost, constraints, constraints_adjoined, location='initial')
    initial_lm_params = make_augmented_params(constraints, constraints_adjoined, location='initial')
    augmented_terminal_cost = make_augmented_cost(terminal_cost, constraints, constraints_adjoined, location='terminal')
    terminal_lm_params = make_augmented_params(constraints, constraints_adjoined, location='terminal')
    hamiltonian, costates = make_ham_lamdot_with_eq_constraint(states, constraints, path_cost, derivative_fn)
    bc_initial = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_initial_cost, derivative_fn, location='initial')
    bc_terminal = make_boundary_conditions(constraints, constraints_adjoined, states, costates, augmented_terminal_cost, derivative_fn, location='terminal')
    bc_terminal = make_time_bc(constraints, bc_terminal)
    dHdu = make_dhdu(hamiltonian, controls, derivative_fn)
    parameters = make_parameters(initial_lm_params, terminal_lm_params, s_list)
    bc_free_mask = make_bc_mask(states, controls, [], initial_cost, augmented_initial_cost, derivative_fn)
    # TODO: More path constraints are processed here. Ref #51
    costate_eoms, bc_list = make_constrained_arc_fns(states, costates, controls, parameters, constants, quantity_vars, hamiltonian, mu_vars, s_list)
    control_law = make_control_law(dHdu, controls)

    # Generate the problem data
    tf_var = sympify('tf')
    problem_data = {'method': 'brysonho',
        'problem_name': problem_name,
        'aux_list': [{'type': 'const', 'vars': [str(k) for k in constants]}],
        'state_list':[str(x) for x in it.chain(states, costates)],
        'parameter_list': [str(tf_var)] + [str(p) for p in parameters],
        'x_deriv_list': [str(tf_var * state.eom) for state in states],
        'lam_deriv_list': [str(tf_var * costate.eom) for costate in costates],
        'deriv_list': [str(tf_var * state.eom) for state in states] + [str(tf_var * costate.eom) for costate in costates],
        'states': states,
        'costates': costates,
        'constants': constants,
        'constants_of_motion': constants_of_motion,
        'parameters': [tf_var] + parameters,
        'controls': controls,
        'mu_vars': mu_vars,
        'quantity_vars': quantity_vars,
        'costate_eoms': costate_eoms,
        'bc_list': bc_list,
        'ham': hamiltonian,
        's_list': s_list,
        'num_states': 2 * len(states),
        'num_params': len(parameters) + 1,
        'dHdu': dHdu,
        'bc_initial': [str(_) for _ in bc_initial],
        'bc_terminal': [str(_) for _ in bc_terminal],
        'control_options': control_law,
        'control_list': [str(u) for u in controls + mu_vars],
        'num_controls': len(controls) + len(mu_vars),
        'ham_expr': str(hamiltonian),
        'quantity_list': quantity_list,
        'nOdes': 2 * len(states)}
    return problem_data


def make_control_law(dhdu, controls):
    """
    Solves control equation to get control law.
    :param dhdu:
    :param controls:
    :return: Control law options.
    """
    try:
        logging.info(controls)
        var_list = list(controls)
        logging.info("Attempting using SymPy ...")
        logging.debug("dHdu = "+str(dhdu))
        ctrl_sol = sympy.solve(dhdu, var_list, dict=True, minimal=True, simplify=False)

        # raise ValueError() # Force mathematica
    except ValueError as e:  # FIXME: Use right exception name here
        logging.debug(e)
        logging.info("No control law found")
        from beluga.utils_old.pythematica import mathematica_solve
        logging.info("Attempting using Mathematica ...")
        var_sol = mathematica_solve(dhdu, var_list)
        # TODO: Extend numerical control laws to mu's
        ctrl_sol = var_sol
    logging.info('Control found')
    logging.info(ctrl_sol)
    control_options = ctrl_sol
    return control_options
