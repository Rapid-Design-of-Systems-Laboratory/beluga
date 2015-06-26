#TODO: Write test for NecessaryConditions and call it before this test
from beluga.optim import Scaling, Problem
from beluga.bvpsol import BVP, Solution
def setup_function(function):
    pass

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)

def test_scale():
    s = Scaling()
    s.unit('m','h')       \
     .unit('s','h/v')     \
     .unit('kg','mass')   \
     .unit('rad',1)

    
