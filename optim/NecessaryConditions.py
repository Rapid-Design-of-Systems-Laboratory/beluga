
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

from utils import keyboard

import bvpsol.BVP
import pystache, imp, re
from optim.problem import *

class NecessaryConditions(object):
    """Defines necessary conditions of optimality."""
    
    compile_list = ['deriv_func','bc_func','compute_control']
    template_prefix = '../bvpsol/templates/'
    template_suffix = '.tmpl.py'
    
    # pystache renderer without HTML escapes
    renderer = pystache.Renderer(escape=lambda u: u)
    
    def __init__(self, problem):
        """Initializes all of the relevant necessary conditions."""
        self.aug_cost = {}
        self.costate = []
        self.costate_rate = []
        self.ham = '0'
        self.ham_ctrl_partial = []
        self.ctrl_free = []
        self.bc = BoundaryConditions()
        self.problem = problem
    
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
                
    # Compiles a function template file into a function object
    # using the given data
    def compile_function(self,filename,verbose=False):
        """Compiles a function specified by filename and stores it in
        self.compiled
           
        Returns: 
            bool: True if successful
            
        Raises:
            ValueError: If 'problem_data' or 'compiled' is not defined
        """
        f = open(filename)
        tmpl = f.read()
        f.close()
        
        if self.problem_data is None:
            raise ValueError('Problem data not defined. Unable to compile function.')
        
        if self.compiled is None:
            raise ValueError('Problem module not defined. Unable to compile function.')
            
        # Render the template using the data 
        code = self.renderer.render(tmpl,self.problem_data)
        if verbose:
            print(code)
        return exec(code,self.compiled.__dict__)
        
    
    def sanitize_constraint(self,constraint):
        if constraint.type == 'initial':
            pattern = r'([\w\d\_]+)_0'
            prefix = '_x0'
        elif constraint.type == 'terminal':
            pattern = r'([\w\d\_]+)_f'
            prefix = '_xf'
        else:
            raise ValueError('Invalid constraint type')
        
        m = re.findall(pattern,constraint.expr)
        invalid = [x for x in m if x[0] not in self.problem.state]

        if not all(x is None for x in invalid):
            raise ValueError('Invalid expression in boundary constraint')

        constraint.expr = re.sub(pattern,prefix+r"['\1']",constraint.expr)
        return constraint
        
    def get_bvp(self):
        """Perform variational calculus calculations on optimal control problem
           and returns an object describing the boundary value problem to be solved
        
        Returns: bvpsol.BVP object
        """
    
        ## Create costate list
        for i in range(len(self.problem.state)):
            self.costate.append(self.problem.state[i].make_costate())
    
        # Build augmented cost strings
        aug_cost_init = self.problem.cost['init'].expr
        self.make_aug_cost(aug_cost_init,self.problem.constraints,'init')
    
        aug_cost_term = self.problem.cost['term'].expr
        self.make_aug_cost(aug_cost_term,self.problem.constraints,'term')
    
        # Compute costate conditions
        self.make_costate_bc(self.problem.state,'init')
        self.make_costate_bc(self.problem.state,'term')
    
        ## Unconstrained arc calculations
        # Construct Hamiltonian
        self.make_ham(self.problem)
    
        # Compute costate process equations
        for i in range(len(self.problem.state)):
            self.make_costate_rate(self.problem.state[i].state_var)
    
        # Compute unconstrained control partial
        for i in range(len(self.problem.control)):
            self.make_ctrl_partial(self.problem.control[i].var)
    
        # Compute unconstrained control law (need to add singular arc and bang/bang smoothing, numerical solutions)
        for i in range(len(self.problem.control)):
            self.make_ctrl(self.problem.control[i].var, i)
    
        self.control_options = []
    
        for i in range(len(self.problem.control)):
            for j in range(len(self.ctrl_free)):  
                self.control_options.append([{'name':self.problem.control[i].var,'expr':self.ctrl_free[j]}])

        # Create problem dictionary
        # ONLY WORKS FOR ONE CONTROL
        # NEED TO ADD BOUNDARY CONDITIONS
        
        initial_bc = self.problem.constraints.get('initial')
        terminal_bc = self.problem.constraints.get('terminal')
        
        bc1 = [self.sanitize_constraint(x) for x in initial_bc]
        
        self.problem_data = {
        'aux_list': [
                {
                'type' : 'const',
                'vars': [self.problem.constant[i].var for i in range(len(self.problem.constant))]
                },
                {
                'type' : 'constraint',
                'vars': []
                }
         ],
         'state_list': 
             [self.problem.state[i].state_var for i in range(len(self.problem.state))] + 
             [self.costate[i] for i in range(len(self.costate))] + 
             ['tf']
         ,
         'deriv_list':
             ['tf*(' + self.problem.state[i].process_eqn + ')' for i in range(len(self.problem.state))] + 
             ['tf*(' + self.costate_rate[i] + ')' for i in range(len(self.costate_rate))] + 
             ['tf*0']
         ,
         'num_states': 2*len(self.problem.state) + 1,


         # Compute these automatically?
         # 'left_bc_list':[self.sanitize_constraint(x).expr for x in initial_bc]+self.bc.init,
         # 'right_bc_list':[self.sanitize_constraint(x).expr for x in terminal_bc]+self.bc.term,
         
         'left_bc_list':[
             "x - _x0['x']", # x(0
             "y - _x0['y']", # y(0)
             "v - _x0['v']"
         ],
         'right_bc_list':[
             "x - _xf['x']", # x(tf)
             "y - _xf['y']", # y(tf)
             "lagrange_v + 0.0",   # lamV(tf)
             "_H     - 0",     # H(tf)
         ],
         'control_options': self.control_options,
         'control_list':[self.problem.control[i].var for i in range(len(self.problem.control))],
         'ham_expr':self.ham
        }

    #    problem.constraints[i].expr for i in range(len(problem.constraints))

        # Create problem functions by importing from templates
        self.compiled = imp.new_module('brachisto_prob')
        compile_result = [self.compile_function(self.template_prefix+func+self.template_suffix) for func in self.compile_list]  

        # Make this generic for BCs, constants and constraints
        self.bvp = bvpsol.BVP(self.compiled.deriv_func,self.compiled.bc_func,
                        initial_bc  = {'x':0.0, 'y':0.0, 'v':1.0},
                        terminal_bc = {'x':0.1, 'y':-0.1}, 
                        const = {'g':9.81},
                        constraint = {}
                    )
        return self.bvp
    
class BoundaryConditions(object):
    """Defines boundary condtiions."""
    
    def __init__(self):
        self.init = []
        self.term = []