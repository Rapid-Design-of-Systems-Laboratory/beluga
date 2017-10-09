import numpy as np
import numexpr as ne
from scipy.interpolate import InterpolatedUnivariateSpline

class Solution(object):
    x = None
    y = None
    p = None
    nOdes = 0
    def __init__(self, x=None, y=None, parameters=None, aux=None, state_list=None, arcs=None):
        "x,y and parameters should be vectors"
        if x is not None and y is not None:
            self.x = np.array(x)
            self.y = np.array(y)
        else:
            self.x = self.y = self.u = None
        if parameters is not None:
            self.parameters = np.array(parameters)
        else:
            self.parameters = None

        self.y_splines = self.u_splines = None

        if aux is None:
            self.aux = {"initial": [], "terminal": [], "const": [], "parameters":[]}
        else:
            self.aux = aux
        self.state_list = state_list
        self.var_dict = None
        self.converged = False
        self.arcs = arcs

    # TODO: Write test for interpolation system
    def init_interpolate(self):
        """
        Fits splines to all states in the solution data
        """
        self.y_splines = []
        self.u_splines = []
        for i,row in enumerate(self.y):
            spline = InterpolatedUnivariateSpline(self.x, row)
            self.y_splines.append(spline)

        if len(self.u.shape) ==1 :
            spline = InterpolatedUnivariateSpline(self.x, self.u)
            self.u_splines.append(spline)
        else:
            for i,row in enumerate(self.u):
                spline = InterpolatedUnivariateSpline(self.x, row)
                self.u_splines.append(spline)

    def interpolate(self, new_x, overwrite=False):
        """
        Interpolates solution data over a new mesh of 'x'

        new_x : new mesh to evaluate
        overwrite: Should the current solution be overwritten?
        """
        # Account for old data files with no sol_splines
        if not hasattr(self,'y_splines') or not hasattr(self,'u_splines') \
            or self.y_splines is None or self.u_splines is None:
            self.init_interpolate()

        new_y = np.array([spline(new_x) for spline in self.y_splines])
        new_u = np.array([spline(new_x) for spline in self.u_splines])
        if overwrite:
            self.x = new_x
            self.y = new_y
            self.u = new_u

        return (new_y, new_u)

    def prepare(self, problem_data, mesh_size = None, overwrite=False):
        """
        Creates the dictionary required to evaluate expressions over the solution

        mesh_size: Evaluate over new mesh
        overwrite: Overwrite existing solution with new mesh
        """
        # TODO: Test mesh_size improvement in prepare()
        # from beluga.utils import keyboard
        # keyboard()
        if mesh_size is not None and mesh_size > len(self.x):
            # Update solution to use new mesh if needed
            new_x = np.linspace(self.x[0],self.x[-1],mesh_size)
            (new_y, new_u) = self.interpolate(new_x, overwrite=overwrite)
        else:
            new_x, new_y, new_u = self.x, self.y, self.u
        x,y,u = self.x, self.y, self.u
        if not overwrite:
            x,y,u = new_x, new_y, new_u

        #TODO: Write test for prepare()
        #TODO: Make state_list a part of the Solution object

        # Define every aux variable (such as constants) in the dictionary
        variables = [(aux_name, aux_val)
                     for aux_type in self.aux
                     if isinstance(self.aux[aux_type], dict)
                     for (aux_name, aux_val) in self.aux[aux_type].items()
                     ]
        # Define state variables
        # Have to do in this order to override state values with arrays
        variables += [(state,np.array(y[idx,:]))
                       for idx,state in enumerate(problem_data['state_list'])]

        # Define control variables
        variables += [(control,np.array(u[idx,:]))
                       for idx,control in enumerate(problem_data['control_list'])]

        # TODO: Name 'tf' is hardcoded
        tf_ind = problem_data['state_list'].index('tf')
        variables += [('t',x*y[tf_ind,1])]
        self.var_dict = dict(variables)


    def evaluate(self,expr):
        """
        Evaluates an expressions involving the variables in this solution

        The caller is responsible for calling the prepare() method first
        """
        #TODO: Write test for evaluate()
        return ne.evaluate(expr,self.var_dict)
