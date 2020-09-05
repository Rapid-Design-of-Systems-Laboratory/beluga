import inspect

from .BaseAlgorithm import BaseAlgorithm, BVPResult
from .Shooting import Shooting
from .spbvp import spbvp

# import os
# import glob
# modules = glob.glob(os.path.dirname(__file__)+"/*.py")
# __all__ = [os.path.basename(f)[:-3] for f in modules]

available_algorithms = [Shooting, spbvp]


def bvp_algorithm(name, **kwargs):
    """
    Helper method to load bvp algorithm by name.

    :param name: The name of the bvp algorithm
    :keywords: Additional keyword arguments passed into the bvp solver.
    :return: An instance of the bvp solver.
    """
    # Load algorithm from the package
    for algorithm in available_algorithms:
        if name == algorithm.__name__:
            return algorithm(**kwargs)
    else:
        # Raise exception if the loop completes without finding an algorithm by the given name
        raise ValueError('Algorithm ' + name + ' not found')
