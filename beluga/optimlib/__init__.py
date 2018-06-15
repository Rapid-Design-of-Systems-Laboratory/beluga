from .brysonho import BrysonHo
from .icrm import ICRM

from .optimlib import (init_workspace, jacobian, make_augmented_cost, make_augmented_params, make_costate_names,
                       make_costate_rates, make_dhdu, make_parameters, make_time_bc, process_quantities,
                       sanitize_constraint_expr, total_derivative)

methods = {'traditional': BrysonHo, 'icrm': ICRM, 'brysonho': BrysonHo}
