"""
Computes the necessary conditions of optimality using Bryson & Ho's method

[1] Bryson, Arthur Earl. Applied optimal control: optimization, estimation and control. CRC Press, 1975.
"""

from .optimlib import *
from beluga.utils import sympify
import simplepipe as sp


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
        var_sol = mathematica_solve(dhdu,var_list)
        # TODO: Extend numerical control laws to mu's
        ctrl_sol = var_sol
    logging.info('Control found')
    logging.info(ctrl_sol)
    control_options = ctrl_sol
    return control_options


def generate_problem_data(workspace):
    """Generates the `problem_data` dictionary used for code generation."""

    tf_var = sympify('tf')
    problem_data = {
        'method': 'brysonho',
        'problem_name': workspace['problem_name'],
        'aux_list': [
            {
            'type' : 'const',
            'vars': [str(k) for k in workspace['constants']]
            }
        ],
        'state_list':
            [str(x) for x in it.chain(workspace['states'], workspace['costates'])]
        ,
        'parameter_list': [str(tf_var)] + [str(p) for p in workspace['parameters']],
        'x_deriv_list': [str(tf_var*state.eom) for state in workspace['states']],
        'lam_deriv_list':[str(tf_var*costate.eom) for costate in workspace['costates']],
        'deriv_list':
            [str(tf_var*state.eom) for state in workspace['states']] +
            [str(tf_var*costate.eom) for costate in workspace['costates']]
        ,
        'states': workspace['states'],
        'costates': workspace['costates'],
        'constants': workspace['constants'],
        'parameters': [tf_var] + workspace['parameters'],
        'controls': workspace['controls'],
        'mu_vars': workspace['mu_vars'],
        'quantity_vars': workspace['quantity_vars'],

        'costate_eoms': workspace['costate_eoms'],
        'bc_list': workspace['bc_list'],
        'ham': workspace['ham'],
        's_list': workspace['s_list'],
        'num_states': 2*len(workspace['states']),
        'num_params': len(workspace['parameters']) + 1,
        'dHdu': workspace['dhdu'],
        'bc_initial': [str(_) for _ in workspace['bc_initial']],
        'bc_terminal': [str(_) for _ in workspace['bc_terminal']],
        'control_options': workspace['control_law'],
        'control_list': [str(u) for u in workspace['controls']+workspace['mu_vars']],
        'num_controls': len(workspace['controls'])+len(workspace['mu_vars']),
        'ham_expr': str(workspace['ham']),
        'quantity_list': workspace['quantity_list'],
        'nOdes': 2*len(workspace['states'])
    }

    return problem_data


# Implement workflow using simplepipe and functions defined above
BrysonHo = sp.Workflow()
BrysonHo.add_task(BaseWorkflow)
BrysonHo.add_task(make_control_law, inputs=('dhdu','controls'), outputs=('control_law'))
BrysonHo.add_task(generate_problem_data, inputs='*', outputs=('problem_data'))
traditional = BrysonHo
