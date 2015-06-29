from beluga.continuation import ContinuationList, ContinuationStep
import numpy.testing as npt
import numpy as np
import pytest

class Dummy(object):
    pass

dummy_bvp = Dummy()

def test_continuation_terminal():
    """Tests change in terminal variables"""
    step_one = ContinuationStep(num_cases=11)
    # Test for changing one 'terminal' variable
    step_one.terminal('x',10)
    dummy_bvp.aux_vars = {'terminal':{'x':0}}
    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['terminal']['x'].value == 0)
    npt.assert_equal(step_one.vars['terminal']['x'].steps, np.linspace(0,10,11))

    # Test for changing two 'terminal' variables
    step_one.clear()
    dummy_bvp.aux_vars = {'terminal':{'x':0,'y':1}}
    step_one.terminal('x',10).terminal('y',5)
    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['terminal']['x'].value == 0)
    assert(step_one.vars['terminal']['y'].value == 1)
    npt.assert_equal(step_one.vars['terminal']['x'].steps, np.linspace(0,10,11))
    npt.assert_equal(step_one.vars['terminal']['y'].steps, np.linspace(1,5,11))

def test_continuation_initial():
    """Tests change in initial variables"""
    step_one = ContinuationStep(num_cases=11)
    # Test for changing one 'initial' variable
    step_one.clear()
    dummy_bvp.aux_vars = {'initial':{'a':10}}
    step_one.initial('a',0)
    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['initial']['a'].value == 10)
    npt.assert_equal(step_one.vars['initial']['a'].steps, np.linspace(10,0,11))

    # Test for changing two 'initial' variables
    step_one.clear()
    dummy_bvp.aux_vars = {'initial':{'a':10,'b':10}}
    step_one.initial('a',0).initial('b',-10)

    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['initial']['a'].value == 10)
    assert(step_one.vars['initial']['b'].value == 10)
    npt.assert_equal(step_one.vars['initial']['a'].steps, np.linspace(10,0,11))
    npt.assert_equal(step_one.vars['initial']['b'].steps, np.linspace(10,-10,11))

def test_continuation_const():
    """Tests change in 'const' values"""
    step_one = ContinuationStep(num_cases=5)
    # Test for changing one 'const' variable
    dummy_bvp.aux_vars = {'const':{'rho0':0}}
    step_one.const('rho0',1.217)
    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['const']['rho0'].value == 0)
    npt.assert_equal(step_one.vars['const']['rho0'].steps, np.linspace(0,1.217,5))

def test_continuation_mixed():
    """Tests change in mixed variable types"""
    step_one = ContinuationStep(num_cases=51)
    # Test for changing one 'const' variable
    dummy_bvp.aux_vars = {'const':{'rho0':0},'terminal':{'h':80000}}
    step_one.const('rho0',1.217)
    step_one.terminal('h',0)
    step_one.set_bvp(dummy_bvp)
    assert(step_one.vars['const']['rho0'].value == 0)
    assert(step_one.vars['terminal']['h'].value == 80000)
    npt.assert_equal(step_one.vars['const']['rho0'].steps, np.linspace(0,1.217,51))
    npt.assert_equal(step_one.vars['terminal']['h'].steps, np.linspace(80000,0,51))

def test_continuation():
    """Tests ContinuationStep functionality"""
    step_one = ContinuationStep(num_cases=100)
    step_one.terminal('x',10)

    # Test for error when no BVP has been set
    with pytest.raises(ValueError):
        step_one.next()

    dummy_bvp.aux_vars = {'terminal':{'h':0},'initial':{'h':80000}}
    # Test for error when variable doesn't exist
    with pytest.raises(ValueError):
        step_one.set_bvp(dummy_bvp)

    step_one.clear()
    step_one.terminal('h',0)
    step_one.set_bvp(dummy_bvp)
    # Test for the case where there is no change in the variable
    assert(step_one.vars['terminal']['h'].value == 0)
    npt.assert_equal(step_one.vars['terminal']['h'].steps, np.zeros(100))

    step_one.clear()

    # Test num_cases function
    step_one.num_cases(21)
    assert(step_one.num_cases() == 21)

    step_one.initial('h',50000)
    step_one.set_bvp(dummy_bvp)
    i = 0
    dh = np.linspace(80000,50000,21)
    for bvp in step_one:
        assert(bvp.aux_vars['initial']['h'] == dh[i])
        i += 1

    # Test reset function
    step_one.reset()
    assert(step_one.ctr == 0)

    # Test that unspecified variable is not changed
    assert(bvp.aux_vars['terminal']['h'] == 0)

    # Test ContinutionList class
    steps = ContinuationList()
    steps.add_step(step_one)
    steps.add_step()

    assert len(steps) == 2
