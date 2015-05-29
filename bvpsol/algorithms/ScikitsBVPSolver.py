import numpy as np
from .. import Solution
from utils.ode45 import ode45
from ..Algorithm import Algorithm
import scikits.bvp_solver as bvp_solver

class ScikitsBVPSolver(Algorithm):
    def __init__(self, num_left_boundary_conditions = 0):
        self.num_left_boundary_conditions = num_left_boundary_conditions
        
    def bc_wrapper(self,bc_func,ya,yb,p,aux):
        res = bc_func(ya,yb,p,aux)
        left_bc = res[:self.num_left_boundary_conditions]
        right_bc = res[self.num_left_boundary_conditions:]
        return (left_bc, right_bc) 
        
    def solve(self,bvp):
        
        solinit = bvp.guess
        num_ODE = len(bvp.aux_vars['initial'])

        deriv_func = lambda x,y,p=None: bvp.deriv_func(x,y,p,bvp.aux_vars)
        bc_func = lambda ya,yb,p=None: self.bc_wrapper(bvp.bc_func,ya,yb,p,bvp.aux_vars)

        prob = bvp_solver.ProblemDefinition(num_ODE = num_ODE,
                                          num_parameters = len(solinit.parameters) if solinit.parameters is not None else 0 ,
                                          num_left_boundary_conditions = self.num_left_boundary_conditions,
                                          boundary_points = (solinit.x[0], solinit.x[-1]),
                                          function = deriv_func,
                                          boundary_conditions = bc_func,
                                    )

        soln = bvp_solver.solve(prob,
                    solution_guess = solinit.y,
                    initial_mesh   = solinit.x,
                    parameter_guess = np.array([solinit.parameters]))
        
        sol = Solution
        sol.x = np.linspace(0,1,100)
        sol.y = soln(sol.x)
        sol.parameters = soln.parameters
        return sol