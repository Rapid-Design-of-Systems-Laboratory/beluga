from .BaseAlgorithm import BaseAlgorithm, BVPResult
from .Shooting import Shooting
from .SPBVP import SPBVP

available_algorithms = [Shooting, SPBVP]


def bvp_algorithm(name, **kwargs):
    """
    Helper method to load bvp algorithm by name.

    :param name: The name of the bvp algorithm
    :keywords: Additional keyword arguments passed into the bvp solver.
    :return: An instance of the bvp solver.
    """
    # Load algorithm from the package
    for algorithm in available_algorithms:
        if name.lower() == algorithm.__name__.lower():
            return algorithm(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm by the given name
        raise ValueError('Algorithm ' + name + ' not found')
