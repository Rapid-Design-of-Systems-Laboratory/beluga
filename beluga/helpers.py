import problem2
from beluga.bvpsol import algorithms
from problem2 import Problem

def initial_guess(*args, **kwargs):
    """Creates initial guess"""
    guess = problem2.Guess()
    guess.setup(*args,**kwargs)
    return guess

def bvp_algorithm(algo, **kwargs):
    """
    Helper method to load algorithm by name
    """
    # Load algorithm from the package
    for name, obj in inspect.getmembers(algorithms):
        if inspect.isclass(obj):
            if name.lower() == algo.lower():
                return obj(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm
        # by the given name
        raise ValueError('Algorithm '+algo+' not found')

def solve(ocp, **kwargs):
    """Runs the solver on the given problem package."""
    problem = dict(ocp=ocp, **kwargs)
