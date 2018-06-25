import pytest
from beluga.optimlib import init_workspace
from beluga.optimlib import make_augmented_params, make_augmented_cost
from beluga.problem import SymVar

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
    cost = SymVar({'expr': '1', 'unit': 'nd'}, sym_key='expr')
    constraints = dict()
    constraints['initial'] = [{'expr': 'x-x_0', 'unit': 'nd'}, {'expr': 'y-y_0', 'unit': 'nd'}]
    constraints['terminal'] = [{'expr': 'x-x_f', 'unit': 'nd'}]
    constraints = {c_type: [SymVar(c_obj, sym_key='expr') for c_obj in c_list]
                   for c_type, c_list in constraints.items()
                   if c_type != 'path'}

    constraints_adjoined = False
    location = 'initial'

    lambdas = make_augmented_params(constraints, constraints_adjoined, location)
    result = make_augmented_cost(cost, constraints, constraints_adjoined, location)
    assert result == 1
    assert len(lambdas) == 0

    constraints_adjoined = True

    lambdas = make_augmented_params(constraints, constraints_adjoined, location)
    result = make_augmented_cost(cost, constraints, constraints_adjoined, location)
    assert result == lambdas[0]*constraints['initial'][0] + lambdas[1]*constraints['initial'][1] + cost
    assert len(lambdas) == 2

    constraints_adjoined = False
    location = 'terminal'

    lambdas = make_augmented_params(constraints, constraints_adjoined, location)
    result = make_augmented_cost(cost, constraints, constraints_adjoined, location)
    assert result == 1
    assert len(lambdas) == 0

    constraints_adjoined = True

    lambdas = make_augmented_params(constraints, constraints_adjoined, location)
    result = make_augmented_cost(cost, constraints, constraints_adjoined, location)
    assert result == lambdas[0] * constraints['terminal'][0] + cost
    assert len(lambdas) == 1
