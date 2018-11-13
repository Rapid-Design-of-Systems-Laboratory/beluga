import pytest
from beluga.optimlib import *

def test_init_workspace():
    class emptyobj(object):
        def __new__(cls):
            obj = super(emptyobj, cls).__new__(cls)
            obj.dae_num_states = 0
            return obj

    guess = emptyobj()
    from beluga.problem import OCP
    problem = OCP('test_problem')

    # Throw an error with no independent variable defined.
    with pytest.raises(KeyError):
        init_workspace(problem, guess)

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

    ws = init_workspace(problem, guess)

    assert isinstance(ws, dict)
    assert ws['problem_name'] == 'test_problem'


# def test_make_augmented_cost():
#     cost = SymVar({'expr': '1', 'unit': 'nd'}, sym_key='expr')
#     constraints = dict()
#     constraints['initial'] = [{'expr': 'x-x_0', 'unit': 'nd'}, {'expr': 'y-y_0', 'unit': 'nd'}]
#     constraints['terminal'] = [{'expr': 'x-x_f', 'unit': 'nd'}]
#     constraints = {c_type: [SymVar(c_obj, sym_key='expr') for c_obj in c_list]
#                    for c_type, c_list in constraints.items()
#                    if c_type != 'path'}
#
#     location = 'initial'
#
#     lambdas = make_augmented_params(constraints, location)
#     result = make_augmented_cost(cost, constraints, location)
#     assert result == lambdas[0]*constraints['initial'][0] + lambdas[1]*constraints['initial'][1] + cost
#     assert len(lambdas) == 2
#
#     location = 'terminal'
#
#     lambdas = make_augmented_params(constraints, location)
#     result = make_augmented_cost(cost, constraints, location)
#     assert result == lambdas[0] * constraints['terminal'][0] + cost
#     assert len(lambdas) == 1
