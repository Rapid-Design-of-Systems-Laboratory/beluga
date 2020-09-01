"""
References
----------
.. [1] Kristof Altmann, and Simon Stingelin, and Fredi Tr\"{o}ltzsch. "On Some Optimal Control Problems for Electric
    Circuits." International Journal of Circuit Theory and Applications 42.8 (2014): 808-830.
"""

import beluga
import logging

i_0 = 1
lu = 1
lq = 1e5

ocp = beluga.Problem()

# Define independent variables
ocp.independent('t', 's')

# Define equations of motion
ocp.state('i', '-Rc/L*i + u/L', 'a')

# Define controls
ocp.control('u', 'v')

# Define constants
ocp.constant('u_min', -300, 'v')
ocp.constant('u_max', 300, 'v')
ocp.constant('i_0', 0.1, 'a')
ocp.constant('Rc', 145, 'o')
ocp.constant('L', 3.5, 'H')
ocp.constant('lu', 1, '1')
ocp.constant('lq', 1, '1')
ocp.constant('eps1', 100, '1')

# Define costs
ocp.path_cost('lu*u**2/2 + lq*(i-i_0)**2/2', '1')

# Define constraints
ocp.initial_constraint('i + i_0', 'a')
ocp.initial_constraint('t', 's')
ocp.terminal_constraint('i - i_0', 'a')
ocp.terminal_constraint('t-1', 's')

ocp.path_constraint('u', 'v', lower='u_min', upper='u_max', activator='eps1', method='utm')

ocp.scale(a='i', v='u_max', s='1', H='L', o='L')

bvp_solver_indirect = beluga.bvp_algorithm('spbvp')

guess_maker_indirect = beluga.guess_generator(
    'auto',
    start=[-i_0/10],
    direction='forward',
    costate_guess=-0.1,
    control_guess=[0],
    use_control_guess=True,
    time_integrate=0.1
)


beluga.add_logger(logging_level=logging.DEBUG, display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(5) \
    .const('i_0', i_0)

continuation_steps.add_step('bisection') \
    .num_cases(20, 'log') \
    .const('lu', lu) \
    .const('lq', lq)

continuation_steps.add_step('bisection') \
    .num_cases(20, 'log') \
    .const('eps1', 1e-2)

sol_set_indirect = beluga.solve(
    ocp=ocp,
    method='indirect',
    optim_options={'control_method': 'differential'},
    bvp_algo=bvp_solver_indirect,
    steps=continuation_steps,
    guess_gen=guess_maker_indirect,
    autoscale=False
)
