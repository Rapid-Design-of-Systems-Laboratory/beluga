import pytest
from beluga.optimlib import init_workspace
from sympy import Symbol

def test_init_workspace():
    from beluga.problem import OCP
    problem = OCP('test_problem')

    # Throw an error with no independent variable defined.
    with pytest.raises(KeyError):
        init_workspace(problem)

    problem.independent('t', 's')
    problem.state('x', 'v', 'm')
    problem.state('v', 'g + u', 'm/s')
    problem.control('u', 'N')
    problem.constant('g', 9.80665, 'm/s^2')
    problem.path_cost('1', 's')
    problem.constraints().initial('x-x_0', 'm')
    problem.constraints().initial('v-v_0', 'm/s')
    problem.constraints().terminal('x-x_f', 'm')
    problem.scale(m='x', s='x/v', N=1)

    ws = init_workspace(problem)

    assert isinstance(ws, dict)
    assert ws['problem_name'] == 'test_problem'

def test_make_augmented_cost():

