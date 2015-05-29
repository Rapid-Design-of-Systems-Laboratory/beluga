from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from utils.keyboard import keyboard
from optim import NecessaryConditions

# from string import *

# from optimalControlClasses import eom

# from classes.classes_necessary_conditions import AugmentedCost


def compute_necessary_conditions(problem):
    """Perform variational calculus calculations on optimal control problem."""
    
    # Initialize necessary conditions object
    nec_cond = NecessaryConditions()    
    
    ## Create costate list
    for i in range(len(problem.state)):
        nec_cond.costate.append(problem.state[i].make_costate())
    
    # Build augmented cost strings
    aug_cost_init = problem.cost['init'].expr
    nec_cond.make_aug_cost(aug_cost_init,problem.constraint,'init')
    
    aug_cost_term = problem.cost['term'].expr
    nec_cond.make_aug_cost(aug_cost_term,problem.constraint,'term')
    
    # Compute costate conditions
    nec_cond.make_costate_bc(problem.state,'init')
    nec_cond.make_costate_bc(problem.state,'term')
    
    ## Unconstrained arc calculations
    # Construct Hamiltonian
    nec_cond.make_ham(problem)
    
    # Compute costate process equations
    for i in range(len(problem.state)):
        nec_cond.make_costate_rate(problem.state[i].state_var)
    
    # Compute unconstrained control partial
    for i in range(len(problem.control)):
        nec_cond.make_ctrl_partial(problem.control[i].var)
    
    # Compute unconstrained control law (need to add singular arc and bang/bang smoothing, numerical solutions)
    for i in range(len(problem.control)):
        nec_cond.make_ctrl(problem.control[i].var, i)
    
    return nec_cond

    
    