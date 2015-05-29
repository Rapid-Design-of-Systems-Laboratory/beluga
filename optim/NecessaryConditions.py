
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

from utils import keyboard

class NecessaryConditions(object):
    """Defines necessary conditions of optimality."""
    
    def __init__(self):
        """Initializes all of the relevant necessary conditions."""
        self.aug_cost = {}
        self.costate = []
        self.costate_rate = []
        self.ham = '0'
        self.ham_ctrl_partial = []
        self.ctrl_free = []
        self.bc = BoundaryConditions()
    
    def make_costate_rate(self, state):
        self.costate_rate.append(str(diff(parse_expr(
        '-1*(' + self.ham + ')'),symbols(state))))

    def make_ctrl_partial(self, ctrl):
        self.ham_ctrl_partial.append(str(diff(parse_expr(self.ham),
            symbols(ctrl))))
    
    def make_ctrl(self, ctrl, i = 0):
        # Need to do all at once. Only works for one control.
        ctrl_free_sym = [[] for m in range(1)]
        ctrl_free_sym.append(solve(parse_expr(self.ham_ctrl_partial[i]),
            symbols(ctrl)))
        # Convert symbolic solutions to strings
        for j in range(len(ctrl_free_sym)):
            for k in range(len(ctrl_free_sym[j])):
                self.ctrl_free.append(str(ctrl_free_sym[j][k]))
    
    def make_aug_cost(self,aug_cost, constraint,location):
        ind = 0
        for i in range(len(constraint)):
            if constraint[i].type is location:
                ind += 1
                aug_cost += ' + ' + constraint[i].make_aug_cost(ind)
        self.aug_cost[location] = aug_cost
        
    def make_costate_bc(self, state, location):
        if location is 'init':
            sign = '-'
        elif location is 'term':
            sign = ''
            
        for i in range(len(state)):
            self.bc.init.append(
                diff(parse_expr(sign + '(' + self.aug_cost[location] + ')'),
                symbols(state[i].state_var)))
                
    def make_ham(self, problem):
        self.ham = problem.cost['path'].expr
        for i in range(len(problem.state)):
            self.ham += ' + ' + self.costate[i] + '*' + \
                problem.state[i].process_eqn
    
class BoundaryConditions(object):
    """Defines boundary condtiions."""
    
    def __init__(self):
        self.init = []
        self.term = []