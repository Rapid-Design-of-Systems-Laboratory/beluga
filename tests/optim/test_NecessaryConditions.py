from beluga.optim import NecessaryConditions
from beluga.utils import sympify2
from mock import *
from beluga.optim.problem import Constraint
from beluga.optim.problem import State
from beluga.optim import Problem
from beluga.optim.problem import Expression
import pytest
from beluga import Beluga

def test_make_costate_rate():
    mock_obj = Mock(NecessaryConditions)
    mock_obj.ham = sympify2('x^2 - y^3 + 4*x*y')
    mock_obj.quantity_vars = []
    states = [sympify2('x')]
    NecessaryConditions.make_costate_rate(mock_obj,states)

    assert mock_obj.costate_rates == [sympify2('-2*x - 4*y')]

def test_make_ctrl_partial():
    mock_obj = Mock(NecessaryConditions)
    mock_obj.ham = sympify2('x^2 + u^2 + u + 1/3*y^3')
    mock_obj.quantity_vars = []
    controls = [sympify2('u')]
    NecessaryConditions.make_ctrl_partial(mock_obj,controls)

    assert mock_obj.ham_ctrl_partial == [sympify2('2*u + 1')]

def test_make_ctrl():

    # Test case where control has an analytic
    mock_obj = Mock(NecessaryConditions)
    mock_obj.ham_ctrl_partial = sympify2('u^2 + 2*u + 1')

    controls = [sympify2('u')]
    NecessaryConditions.make_ctrl(mock_obj,controls)

    assert mock_obj.control_options[0][0]['expr'] == '-1'

    # Test case where control has no analytic solution
    mock_obj.ham_ctrl_partial = sympify2('Cust_Func(u)^2 + 2*u + 1')

    NecessaryConditions.make_ctrl(mock_obj,controls)

    # Check if empty
    assert not mock_obj.control_options

def test_make_aug_cost():
    mock_obj = Mock(NecessaryConditions)
    mock_obj.aug_cost = {}
    mock_obj.parameter_list = []
    aug_cost = sympify2('x^2 + u^2')

    # Test initial constraint
    type = 'initial'
    expr = 'x*u'
    unit = 'm/s'
    constraint = [Constraint(type, expr, unit)]

    location = 'initial'
    NecessaryConditions.make_aug_cost(mock_obj, aug_cost, constraint, location)

    assert mock_obj.parameter_list == ['lagrange_initial_1']
    assert mock_obj.aug_cost['initial'] == sympify2('lagrange_initial_1*u*x + u**2 + x**2')

    # Test terminal constraint
    type = 'terminal'
    expr = 'x*u'
    unit = 'm/s'
    constraint = [Constraint(type, expr, unit)]

    location = 'terminal'
    NecessaryConditions.make_aug_cost(mock_obj, aug_cost, constraint, location)

    assert mock_obj.parameter_list == ['lagrange_initial_1', 'lagrange_terminal_1']
    assert mock_obj.aug_cost['terminal'] == sympify2('lagrange_terminal_1*u*x + u**2 + x**2')

def test_make_costate_bc():
    mock_obj = Mock(NecessaryConditions)
    mock_obj.bc_initial = []
    mock_obj.bc_terminal = []
    mock_obj.parameter_list = []
    mock_obj.aug_cost = {}
    mock_obj.aug_cost['initial'] = sympify2('x^2 + y^2')
    mock_obj.aug_cost['terminal'] = sympify2('cos(x) + sin(y)')
    mock_obj.quantity_vars = []
    var = 'x'
    process_eqn = '-x'
    unit = 'nd'
    indep_var = 't'
    states = [State(var, process_eqn, unit, indep_var)]

    var = 'y'
    process_eqn = 'y'
    unit = 'nd'
    indep_var = 't'
    states.append(State(var, process_eqn, unit, indep_var))

    location = 'initial'
    NecessaryConditions.make_costate_bc(mock_obj, states, location)

    location = 'terminal'
    NecessaryConditions.make_costate_bc(mock_obj, states, location)

    # TODO: Change to symbolic
    # assert mock_obj.bc_initial == [str(sympify2('lagrange_x + 2*x')), str(sympify2('lagrange_y + 2*y'))]
    # assert mock_obj.bc_terminal == [str(sympify2('lagrange_x + sin(x)')), str(sympify2('lagrange_y - cos(y)'))]
    assert mock_obj.bc_initial == [str(sympify2('lamX + 2*x')), str(sympify2('lamY + 2*y'))]
    assert mock_obj.bc_terminal == [str(sympify2('lamX + sin(x)')), str(sympify2('lamY - cos(y)'))]

def test_make_ham():
    mock_obj = Mock(NecessaryConditions)
    mock_obj.costates = [sympify2('lamX'), sympify2('lamY')]
    mock_obj.ham = sympify2('0')
    mock_obj.equality_constraints = []

    problem = Problem('test_make_ham')
    problem.cost = {}
    problem.cost['initial'] = Expression('x','m')
    problem.cost['terminal'] = Expression('y','m')
    problem.cost['path'] = Expression('u^2','m/s')

    problem.state('x','-cos(x)','m')   \
           .state('y','sin(y)^2','kg')

    NecessaryConditions.make_ham(mock_obj,problem)

    assert mock_obj.ham == sympify2('lamX*(-cos(x)) + lamY*(sin(y)^2) + u^2')

def test_sanitize_constraint():
    mock_obj = Mock(NecessaryConditions)

    type = 'terminal'
    expr = 'x_f^2 + 1/2*y_f'
    unit = 'm'
    constraint = Constraint(type, expr, unit)

    problem = Problem('test_make_ham')
    problem.state('x','-cos(x)','m')   \
           .state('y','sin(y)^2','kg')

    constraint = NecessaryConditions.sanitize_constraint(mock_obj, constraint, problem)

    assert constraint.expr == "_xf['x']^2 + 1/2*_xf['y']"

    type = 'initial'
    expr = 'x_0^2 + 1/2*y_0'
    unit = 'm'
    constraint = Constraint(type, expr, unit)

    constraint = NecessaryConditions.sanitize_constraint(mock_obj, constraint, problem)

    assert constraint.expr == "_x0['x']^2 + 1/2*_x0['y']"

    with pytest.raises(ValueError) as excinfo:
        type = 'fail'
        expr = 'x_0^2 + 1/2*y_0'
        unit = 'm'
        constraint = Constraint(type, expr, unit)
        constraint = NecessaryConditions.sanitize_constraint(mock_obj, constraint, problem)
    assert 'Invalid constraint type' in str(excinfo.value)

def test_init():
    mock_obj = Mock(NecessaryConditions)
    NecessaryConditions.__init__(mock_obj)

    assert mock_obj.aug_cost == {}
    assert mock_obj.costates == []
    assert mock_obj.costate_rates == []
    assert mock_obj.parameter_list == []
    assert mock_obj.ham == sympify2('0')
    assert mock_obj.ham_ctrl_partial == []
    assert mock_obj.ctrl_free == []
    assert mock_obj.bc_initial == []
    assert mock_obj.bc_terminal == []
    assert mock_obj.compile_list == ['deriv_func','bc_func','compute_control']
    assert mock_obj.template_prefix == Beluga.config.getroot()+'/beluga/bvpsol/templates/'
    assert mock_obj.template_suffix == '.py.mu'
        # self.cached = cached

    assert True

def test_compile_function():
    assert True

def test_get_bvp():
    assert True
