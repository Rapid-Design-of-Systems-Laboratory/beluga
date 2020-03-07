# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


class beluga:
    @staticmethod
    def time_import():
        import beluga


class Brachistochrone:
    timeout = 240

    def __init__(self):
        self.beluga = None
        self.ocp = None
        self.continuation_steps = None

    def setup(self):
        import beluga

        self.beluga = beluga
        ocp = beluga.OCP('brachisto')

        # Define independent variables
        ocp.independent('t', 's')

        # Define equations of motion
        ocp.state('x', 'v*cos(theta)', 'm') \
            .state('y', 'v*sin(theta)', 'm') \
            .state('v', 'g*sin(theta)', 'm/s')

        ocp.constant_of_motion('c1', 'lamX', 's/m')
        ocp.constant_of_motion('c2', 'lamY', 's/m')

        # Define controls
        ocp.control('theta', 'rad')

        # Define constants
        ocp.constant('g', -9.81, 'm/s^2')
        ocp.constant('x_f', 0, 'm')
        ocp.constant('y_f', 0, 'm')

        # Define costs
        ocp.path_cost('1', '1')

        # Define constraints
        ocp.constraints() \
            .initial_constraint('x', 'm') \
            .initial_constraint('y', 'm') \
            .initial_constraint('v', 'm/s') \
            .terminal_constraint('x-x_f', 'm') \
            .terminal_constraint('y-y_f', 'm')

        ocp.scale(m='y', s='y/v', kg=1, rad=1, nd=1)
        self.ocp = ocp

        continuation_steps = self.beluga.init_continuation()

        continuation_steps.add_step('bisection') \
            .num_cases(21) \
            .const('x_f', 10) \
            .const('y_f', -10)

        self.continuation_steps = continuation_steps

    def time_shooting(self):
        from math import pi

        bvp_solver = self.beluga.bvp_algorithm('Shooting')
        guess_maker = self.beluga.guess_generator(
            'auto',
            start=[0, 0, 0],  # Starting values for states in order
            direction='forward',
            costate_guess=-0.1,
            control_guess=[-pi/2],
            use_control_guess=True,
        )

        self.beluga.solve(
            ocp=self.ocp,
            method='traditional',
            bvp_algorithm=bvp_solver,
            steps=self.continuation_steps,
            guess_generator=guess_maker, autoscale=True
        )

    def time_pseudospectral(self):
        from math import pi

        bvp_solver = self.beluga.bvp_algorithm('Pseudospectral')
        guess_maker = self.beluga.guess_generator(
            'auto',
            start=[0, 0, 0],  # Starting values for states in order
            direction='forward',
            costate_guess=-0.1,
            control_guess=[-pi/2],
            use_control_guess=True,
        )

        self.beluga.solve(
            ocp=self.ocp,
            method='traditional',
            bvp_algorithm=bvp_solver,
            steps=self.continuation_steps,
            guess_generator=guess_maker, autoscale=True)
