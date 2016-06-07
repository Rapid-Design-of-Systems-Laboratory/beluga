from .Solution import Solution
class BVP(object):
    """
    Defines a boundary value problem
    """
    def __init__(self, deriv_func, bc_func, initial_bc = None, terminal_bc = None, const = [], constraint = [], parameters = []):
        self.deriv_func  = deriv_func
        self.bc_func = bc_func
        self.solution = Solution()
        self.solution.aux = {"initial": initial_bc, "terminal": terminal_bc, "const": const, "constraint":constraint, "parameters":parameters}
        self.solution.converged = False
