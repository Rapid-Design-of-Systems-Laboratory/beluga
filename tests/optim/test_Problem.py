import pytest
import beluga
from beluga.optim import Problem
from beluga import Beluga

def describe_problem():
    @pytest.fixture
    def problem():
        return beluga.optim.Problem('test_problem')

    # Tests if problem name was set correctly
    # TODO: Add test for formatting of name
    def sets_problem_name(problem):
        assert problem.name == 'test_problem'

    # Tests addition of independent variable to default dynamic system
    def adds_independent_variable(problem):
        problem.independent('t', 's')
        assert problem.systems['default'][0].independent_var.var == 't'
        assert problem.systems['default'][0].independent_var.unit == 's'

    # Tests addition of state variables
    def adds_state_variables(problem):
        problem.state('x','v*cos(theta)','m')
        assert problem.systems['default'][0].states[0].state_var == 'x'
        assert problem.systems['default'][0].states[0].process_eqn == 'v*cos(theta)'
        assert problem.systems['default'][0].states[0].unit == 'm'
        problem.state('y','v*sin(theta)','m')
        assert problem.systems['default'][0].states[1].state_var == 'y'
        assert problem.systems['default'][0].states[1].process_eqn == 'v*sin(theta)'
        assert problem.systems['default'][0].states[1].unit == 'm'

    # Tests addition of control variables
    def adds_control_variables(problem):
        problem.control('theta','rad')
        assert problem.systems['default'][0].controls[0].var == 'theta'
        assert problem.systems['default'][0].controls[0].unit == 'rad'
        problem.control('gamma','rad')
        assert problem.systems['default'][0].controls[1].var == 'gamma'
        assert problem.systems['default'][0].controls[1].unit == 'rad'

    # Tests addition of constants
    def adds_constants(problem):
        # Value is given as string
        problem.constant('g','9.81','m/s^2')
        assert problem.systems['default'][0].constants[0].var == 'g'
        assert problem.systems['default'][0].constants[0].val == 9.81
        assert problem.systems['default'][0].constants[0].unit == 'm/s^2'

        # Value is given as float
        problem.constant('rho0',1.125,'kg/m^3')
        assert problem.systems['default'][0].constants[1].var == 'rho0'
        assert problem.systems['default'][0].constants[1].val == 1.125
        assert problem.systems['default'][0].constants[1].unit == 'kg/m^3'
        
