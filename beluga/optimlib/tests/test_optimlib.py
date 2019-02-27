import pytest
from beluga.optimlib import *

METHODS = ['traditional', 'icrm', 'direct']
tol = 1e-8


@pytest.mark.parametrize("method", METHODS)
def test_composable_functors(method):
    from beluga import OCP, ocp2bvp

    problem = OCP('test_problem')
    problem.independent('t', 's')
    problem.state('x', 'v*cos(theta)', 'm')
    problem.state('y', 'v*sin(theta)', 'm')
    problem.state('v', 'g*sin(theta)', 'm/s')

    problem.constant_of_motion('c1', 'lamX', 's/m')
    problem.constant_of_motion('c2', 'lamY', 's/m')

    problem.control('theta', 'rad')

    problem.constant('g', -9.81, 'm/s^2')
    problem.constant('x_f', 1, 'm')
    problem.constant('y_f', -1, 'm')

    problem.path_cost('1', '1')
    problem.constraints().initial('x', 'm')
    problem.constraints().initial('y', 'm')
    problem.constraints().initial('v', 'm')
    problem.constraints().terminal('x - x_f', 'm')
    problem.constraints().terminal('y - y_f', 'm')

    bvp, mapper, mapper_inv = ocp2bvp(problem, method)

    gamma = Trajectory()
    gamma.t = np.linspace(0, 1, num=10)
    gamma.y = np.vstack([np.linspace(0, 0, num=10) for _ in range(3)]).T
    gamma.dual = np.vstack([np.linspace(-1, -1, num=10) for _ in range(3)]).T
    gamma.u = -np.pi / 2 * np.ones((10, 1))
    gamma.const = np.array([-9.81, 1, -1])

    g1 = mapper(gamma)
    g2 = mapper_inv(g1)

    assert g2.y.shape == gamma.y.shape
    assert (g2.y - gamma.y < tol).all()

    assert g2.q.shape == gamma.q.shape
    assert (g2.q - gamma.q < tol).all()

    assert g2.dual.shape == gamma.dual.shape
    assert (g2.dual - gamma.dual < tol).all()

    assert g2.u.shape == gamma.u.shape
    assert (g2.u - gamma.u < tol).all()

    assert g2.t.size == gamma.t.size
    assert (g2.t - gamma.t < tol).all()

    assert g2.dynamical_parameters.size == gamma.dynamical_parameters.size
    assert (g2.dynamical_parameters - gamma.dynamical_parameters < tol).all()

    assert g2.nondynamical_parameters.size == gamma.nondynamical_parameters.size
    assert (g2.nondynamical_parameters - gamma.nondynamical_parameters < tol).all()


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
