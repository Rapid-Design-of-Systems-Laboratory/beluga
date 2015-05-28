from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Hamiltonian(object):
    """Defines Hamiltonian information and methods."""
    
    def __init__(self):
        """Initialize Hamiltonian object."""
        self.free = '0'
        self.ctrl_partial = []
        self.ctrl_free = []
        self.costate_rate = []

    def make_costate_rate(self,costate):
        self.costate_rate.append(str(diff(parse_expr(
        '-1*(' + self.free + ')'),symbols(costate))))

    def make_ctrl_partial(self,ctrl):
        self.ctrl_partial.append(str(diff(parse_expr(self.free),
            symbols(ctrl))))
    
    def make_ctrl(self, ctrl, i = 0):
        self.ctrl_free.append(str(solve(parse_expr(self.ctrl_partial[i]),
            symbols(ctrl))))
