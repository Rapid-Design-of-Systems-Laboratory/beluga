"""
References
----------
.. [1] Kristof Altmann, and Simon Stingelin, and Fredi Tr\"{o}ltzsch. "On Some Optimal Control Problems for Electric
    Circuits." International Journal of Circuit Theory and Applications 42.8 (2014): 808-830.
"""

import beluga
import logging

import matplotlib.pyplot as plt

i_0 = 1
lu = 1
lq = 1e5

ocp = beluga.OCP('oneloop')

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
ocp.constraints() \
    .initial('i + i_0', 'a') \
    .path('u', 'v', lower='u_min', upper='u_max', activator='eps1', method='utm') \
    .terminal('i - i_0', 'a') \
    .terminal('t-1', 's')

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
    optim_options={'control_method': 'icrm'},
    bvp_algorithm=bvp_solver_indirect,
    steps=continuation_steps,
    guess_generator=guess_maker_indirect,
    autoscale=False
)

sol_indirect = sol_set_indirect[-1][-1]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Current [A]', color=color)
ax1.plot(sol_indirect.t, sol_indirect.y[:,0], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Voltage [volts]', color=color)
ax2.plot(sol_indirect.t, sol_indirect.u[:,0], color=color)
ax2.plot([sol_indirect.t[0], sol_indirect.t[-1]], [sol_indirect.const[0]]*2, linestyle='--', color='k')
ax2.plot([sol_indirect.t[0], sol_indirect.t[-1]], [sol_indirect.const[1]]*2, linestyle='--', color='k', label='Min/Max Voltage')
ax2.tick_params(axis='y', labelcolor=color)

plt.legend()
plt.grid(True)
fig.tight_layout()
plt.show()
