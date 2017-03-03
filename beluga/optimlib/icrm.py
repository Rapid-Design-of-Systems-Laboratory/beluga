"""
Contains classes and functions related to Optimal Control.

Module: optimlib
"""

def sigmoid_two_sided(x, ub, lb, slopeAtZero=1):
    """Two-sided saturation function based on the sigmoid function."""
    pass


def sigmoid_one_sided(x, ub=None, lb=None, slopeAtZero=1):
    """
    One-sided saturation function based on the sigmoid function.

    Only of the bounds must be defined.
    """
    pass



# class OCProblem(object):
#     """Describes an optimal control problem."""
#     pass
#  OCProblem
#     -> states (array from Problem object)
#     -> costates (similar array as states)
#     -> Hamiltonian

# Call doctest if the script is run directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()
