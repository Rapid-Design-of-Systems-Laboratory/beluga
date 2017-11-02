import numpy as np
import numexpr as ne
from scipy.interpolate import InterpolatedUnivariateSpline
import math

class Solution(object):
    x = None
    y = None
    p = None
    nOdes = 0
    def __init__(self, x=None, y=None, parameters=None, aux=None, state_list=None, arcs=None):
        "x,y and parameters should be vectors"
        if x is not None and y is not None:
            self.x = np.array(x, dtype=np.float64)
            self.y = np.array(y, dtype=np.float64)
        else:
            self.x = self.y = self.u = None
        if parameters is not None:
            self.parameters = np.array(parameters, dtype=np.float64)
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

        self.y_splines = None
        self.u_splines = None
        self.extra = None

    # TODO: Write test for interpolation system
    def init_interpolate(self):
        """
        Fits splines to all states in the solution data
        """
        self.y_splines = []
        self.u_splines = []
        for arc_start, arc_end in self.arcs:
            y_spline_arc = []
            u_spline_arc = []
            for j,row in enumerate(self.y):
                spline = InterpolatedUnivariateSpline(self.x[arc_start:arc_end+1], row[arc_start:arc_end+1])
                y_spline_arc.append(spline)

            if len(self.u.shape) ==1 :
                spline = InterpolatedUnivariateSpline(self.x[arc_start:arc_end+1], self.u[arc_start:arc_end+1])
                u_spline_arc.append(spline)
            else:
                for j,row in enumerate(self.u):
                    spline = InterpolatedUnivariateSpline(self.x[arc_start:arc_end+1], row[arc_start:arc_end+1])
                    u_spline_arc.append(spline)

            self.y_splines.append(y_spline_arc)
            self.u_splines.append(u_spline_arc)

    def interpolate(self, new_x, new_arcs, overwrite=False):
        """
        Interpolates solution data over a new mesh of 'x'

        new_x : new mesh to evaluate
        overwrite: Should the current solution be overwritten?
        """
        # Account for old data files with no sol_splines
        if self.y_splines is None or self.u_splines is None:
            self.init_interpolate()

        new_y = np.hstack([np.vstack([spline(new_x[arc_start:arc_end+1]) for spline in spline_arc])
                           for (arc_start, arc_end), spline_arc in zip(new_arcs, self.y_splines)])
        new_u = np.hstack([np.vstack([spline(new_x[arc_start:arc_end+1]) for spline in spline_arc])
                           for (arc_start, arc_end), spline_arc in zip(new_arcs, self.u_splines)])

        if overwrite:
            self.x = new_x
            self.y = new_y
            self.u = new_u
            self.arcs = new_arcs
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
        if not hasattr(self, 'arcs'):
            self.arcs = ((0,len(self.x)-1),)
        if mesh_size is not None and mesh_size > len(self.x)*len(self.arcs):
            # Update solution to use new mesh if needed
            new_x_list = []
            new_arcs = []
            arc_ctr = 0
            for arc_start, arc_end in self.arcs:
                new_x_list.append(np.linspace(self.x[arc_start], self.x[arc_end], mesh_size))
                new_arcs.append((arc_ctr, arc_ctr + mesh_size - 1))
                arc_ctr += mesh_size

            new_x = np.hstack(new_x_list)
            (new_y, new_u) = self.interpolate(new_x, new_arcs, overwrite=overwrite)
        else:
            new_x, new_y, new_u, new_arcs = self.x, self.y, self.u, self.arcs
        x,y,u,arcs = self.x, self.y, self.u, self.arcs
        if not overwrite:
            x,y,u,arcs = new_x, new_y, new_u, new_arcs

        #TODO: Write test for prepare()
        #TODO: Make state_list a part of the Solution object

        # Define every aux variable (such as constants) in the dictionary
        variables = [(aux_name, np.ones_like(x)*aux_val)
                     for aux_type in self.aux
                     if isinstance(self.aux[aux_type], dict)
                     for (aux_name, aux_val) in self.aux[aux_type].items()
                     if isinstance(aux_val, float)
                     ]
        # Define state variables
        # Have to do in this order to override state values with arrays
        variables += [(state,np.array(y[idx,:], dtype=np.float64))
                       for idx,state in enumerate(problem_data['state_list'])]

        # Define control variables
        variables += [(control,np.array(u[idx,:], dtype=np.float64))
                       for idx,control in enumerate(problem_data['control_list'])]


        # Define constants
        # variables += [(str(constant),np.ones_like(x)*float(self.aux['const'][].value))
        #                for idx,constant in enumerate(problem_data['constants'])]

        # TODO: Name 'tf' is hardcoded
        t_list = []
        tf_ind = problem_data['state_list'].index('tf')
        last_t = 0
        for arc_start, arc_end in arcs:
            start_x = x[arc_start]
            # from beluga.utils import keyboard
            # keyboard()
            t_list.append(last_t+(x[arc_start:arc_end+1] - start_x)*y[tf_ind,arc_start])
            last_t += y[tf_ind,arc_start]

        variables += [('t', np.hstack(t_list))]

        if 'quantity_list' in problem_data:
            self.qvars = {q['name']:q['expr'] for q in problem_data['quantity_list']}
        else:
            self.qvars = problem_data.get('quantity_vars', {})
        variables += [(str(q_k), ne.evaluate(str(q_v), dict(variables)))
                      for q_k, q_v in self.qvars.items()]
        self.var_dict = dict(variables)
        self.var_dict['pi'] = math.pi

    def evaluate(self,expr):
        """
        Evaluates an expressions involving the variables in this solution

        The caller is responsible for calling the prepare() method first
        """
        #TODO: Write test for evaluate()
        return ne.evaluate(expr,self.var_dict)
        
