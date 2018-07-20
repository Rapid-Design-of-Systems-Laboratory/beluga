import numpy as np
import numexpr as ne
from scipy.interpolate import InterpolatedUnivariateSpline
import math
from beluga.ivpsol import Trajectory
from beluga.utils import keyboard


class Solution(Trajectory):
    def __new__(cls, *args, **kwargs):
        """
        Creates a new Solution object.

        :param args:
        :param kwargs:
        :return:
        """

        t = kwargs.get('t', None)
        y = kwargs.get('y', None)
        q = kwargs.get('q', None)
        u = kwargs.get('u', None)
        parameters = kwargs.get('parameters', None)
        aux = kwargs.get('aux', None)
        state_list = kwargs.get('state_list', None)
        arcs = kwargs.get('arcs', None)

        if t is not None:
            t = np.array(t, dtype=np.float64)
        if y is not None:
            y = np.array(y, dtype=np.float64)
        if q is not None:
            q = np.array(q, dtype=np.float64)
        if u is not None:
            u = np.array(u, dtype=np.float64)

        obj = super(Solution, cls).__new__(cls, t, y, q, u)

        if parameters is not None:
            obj.parameters = np.array(parameters, dtype=np.float64)
        else:
            obj.parameters = np.array([])

        if aux is None:
            obj.aux = {"initial": [], "terminal": [], "const": {}, "parameters": [], "arc_seq": (0,)}
        else:
            obj.aux = aux

        obj.state_list = state_list
        obj.var_dict = None
        obj.converged = False
        obj.arcs = arcs

        obj.y_splines = None
        obj.u_splines = None
        obj.extra = None
        obj.converged = False
        return obj

    # TODO: Remove this and use Trajectory()'s interpolation.
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
                spline = InterpolatedUnivariateSpline(self.t[arc_start:arc_end+1], row[arc_start:arc_end+1])
                y_spline_arc.append(spline)

            if len(self.u.shape) ==1 :
                spline = InterpolatedUnivariateSpline(self.t[arc_start:arc_end+1], self.u[arc_start:arc_end+1])
                u_spline_arc.append(spline)
            else:
                for j,row in enumerate(self.u):
                    spline = InterpolatedUnivariateSpline(self.t[arc_start:arc_end+1], row[arc_start:arc_end+1])
                    u_spline_arc.append(spline)

            self.y_splines.append(y_spline_arc)
            self.u_splines.append(u_spline_arc)

    def interpolate(self, new_t, new_arcs, overwrite=False):
        """
        Interpolates solution data over a new mesh of 't'

        new_t : new mesh to evaluate
        overwrite: Should the current solution be overwritten?
        """
        # Account for old data files with no sol_splines
        if self.y_splines is None or self.u_splines is None:
            self.init_interpolate()

        new_y = np.hstack([np.vstack([spline(new_t[arc_start:arc_end+1]) for spline in spline_arc])
                           for (arc_start, arc_end), spline_arc in zip(new_arcs, self.y_splines)])
        new_u = np.hstack([np.vstack([spline(new_t[arc_start:arc_end+1]) for spline in spline_arc])
                           for (arc_start, arc_end), spline_arc in zip(new_arcs, self.u_splines)])

        if overwrite:
            self.t = new_t
            self.y = new_y
            self.u = new_u
            self.arcs = new_arcs

        return new_y, new_u

    def prepare(self, problem_data, mesh_size=None, overwrite=False):
        """
        Creates the dictionary required to evaluate expressions over the solution

        mesh_size: Evaluate over new mesh
        overwrite: Overwrite existing solution with new mesh
        """

        if self.arcs is None:
            self.arcs = ((0,len(self.t)-1),)
        if mesh_size is not None and mesh_size > len(self.t)*len(self.arcs):
            # Update solution to use new mesh if needed
            new_t_list = []
            new_arcs = []
            arc_ctr = 0
            for arc_start, arc_end in self.arcs:
                new_t_list.append(np.linspace(self.t[arc_start], self.t[arc_end], mesh_size))
                new_arcs.append((arc_ctr, arc_ctr + mesh_size - 1))
                arc_ctr += mesh_size

            new_t = np.hstack(new_t_list)
            (new_y, new_u) = self.interpolate(new_t, new_arcs, overwrite=overwrite)
        else:
            new_t, new_y, new_u, new_arcs = self.t, self.y, self.u, self.arcs
        t, y, u, p, arcs = self.t, self.y, self.u, self.parameters, self.arcs
        if not overwrite:
            t, y, u, arcs = new_t, new_y, new_u, new_arcs

        #TODO: Write test for prepare()
        #TODO: Make state_list a part of the Solution object

        # Define every aux variable (such as constants) in the dictionary
        variables = [(aux_name, np.ones_like(t)*aux_val)
                     for aux_type in self.aux
                     if isinstance(self.aux[aux_type], dict)
                     for (aux_name, aux_val) in self.aux[aux_type].items()
                     if isinstance(aux_val, float)
                     ]
        # Define state variables
        # Have to do in this order to override state values with arrays
        variables += [(state,np.array(y[:, idx], dtype=np.float64))
                       for idx,state in enumerate(problem_data['state_list'])]

        # Define control variables
        variables += [(control,np.array(u[:, idx], dtype=np.float64))
                       for idx,control in enumerate(problem_data['control_list'])]


        # Define constants
        # variables += [(str(constant),np.ones_like(x)*float(self.aux['const'][].value))
        #                for idx,constant in enumerate(problem_data['constants'])]

        t_list = []
        tf_ind = problem_data['parameter_list'].index('tf')
        last_t = 0
        for arc_start, arc_end in arcs:
            start_t = t[arc_start]
            # from beluga.utils import keyboard
            # keyboard()
            t_list.append(last_t+(t[arc_start:arc_end+1] - start_t))
            last_t += y[tf_ind, arc_start]

        variables += [('t', np.hstack(t_list))]

        if 'quantity_list' in problem_data:
            self.qvars = {q['name']:q['expr'] for q in problem_data['quantity_list']}
        else:
            self.qvars = problem_data.get('quantity_vars', {})

        qvars = []
        for q_k, q_v in self.qvars.items():
            qvars.append((str(q_k), ne.evaluate(str(q_v), dict(variables+qvars))))

        variables += qvars
        self.var_dict = dict(variables)
        self.var_dict['pi'] = math.pi

    def evaluate(self,expr):
        """
        Evaluates an expression or custom function involving the variables in this solution

        The caller is responsible for calling the prepare() method first
        """

        if callable(expr):
            # Custom plot function
            return expr(**{arg_name:self.var_dict[arg_name] for arg_name in inspect.getargspec(expr).args})
        else:
            # String specified in plot
            return ne.evaluate(expr,self.var_dict)
