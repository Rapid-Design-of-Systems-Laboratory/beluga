#TODO: Write test for NecessaryConditions and call it before this test
from beluga.optim import Scaling, Problem, NecessaryConditions
from beluga.bvpsol import BVP, Solution
import pytest
import numpy as np
import numpy.testing as npt
def setup_function(function):
    pass

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)

def test_scale(problem_1, scaled_problem_1_bvp, scaled_problem_1_solinit):
    s = problem_1.scale
    nec_cond = NecessaryConditions()
    bvp = nec_cond.get_bvp(problem_1)

    solinit = problem_1.guess.generate(bvp)
    state_names = nec_cond.problem_data['state_list']
    initial_states = solinit.y[:,0] # First column
    terminal_states = solinit.y[:,-1] # Last column
    initial_bc = dict(zip(state_names,initial_states))
    terminal_bc = dict(zip(state_names,terminal_states))
    bvp.solution.aux['initial'] = initial_bc
    bvp.solution.aux['terminal'] = terminal_bc

    s.initialize(problem_1,nec_cond.problem_data)
    s.compute_scaling(bvp)
    s.scale(bvp)

    # Compare to 5 decimal places
    npt.assert_almost_equal(np.array(solinit.y),np.array(scaled_problem_1_solinit.y),decimal=5)

    #TODO: Write proper test for unscale()
    s.unscale(bvp)
