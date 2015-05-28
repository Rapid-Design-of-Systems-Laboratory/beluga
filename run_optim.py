from sandbox.inputFile import inputs
from optim.necessary_conditions import compute_necessary_conditions
import imp

# from optim import *

# from necessary_conditions import compute_necessary_conditions
# import pdb

def run_optim():
    
    # Read from input file
    problem = inputs()
    
    # Perform necessary conditions calculations
    nec_cond = compute_necessary_conditions(problem)
    
    
        # Import problem templates
    # Read file here
    
    # Create unconstrained control function object
    ctrl_un_fn_str = """def ctrl_unconstrained(a,b):
    return a+b
    """
    
    dyn_module = imp.new_module('mycodemodule') # can be called anything, but should be unique (probably use problem name here)
    exec(ctrl_un_fn_str, dyn_module.__dict__)
    print(dyn_module.ctrl_unconstrained(1,2))
    
    
    # for ctr in range(len(problem.states)):
    #     print(problem.states[ctr].variable)
    # 
    # for ctr in range(len(problem.controls)):
    #     print(problem.controls[ctr].variable)
    #     
    # print(problem.costs.path.cost)
    # print(problem.costs.point.interior.cost)
    # print(problem.costs.point.initial.cost)
    # print(problem.costs.point.terminal.cost)
    # 
        
    # print(costs.path)