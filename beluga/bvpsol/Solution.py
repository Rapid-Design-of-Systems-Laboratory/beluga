import inspect
import math
import numpy as np
import numexpr as ne

from beluga.ivpsol import Trajectory


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
        dynamical_parameters = kwargs.get('dynamical_parameters', None)
        nondynamical_parameters = kwargs.get('nondynamical_parameters', None)
        aux = kwargs.get('aux', None)
        state_list = kwargs.get('state_list', None)
        control_list = kwargs.get('control_list', None)
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

        if dynamical_parameters is not None:
            obj.dynamical_parameters = np.array(dynamical_parameters, dtype=np.float64)
        else:
            obj.dynamical_parameters = np.array([])

        if nondynamical_parameters is not None:
            obj.nondynamical_parameters = np.array(nondynamical_parameters, dtype=np.float64)
        else:
            obj.nondynamical_parameters = np.array([])

        if aux is None:
            obj.aux = {"initial": [], "terminal": [], "const": {}, "parameters": [], "arc_seq": (0,)}
        else:
            obj.aux = aux

        obj.state_list = state_list
        obj.control_list = control_list
        obj.var_dict = None
        obj.converged = False
        obj.arcs = arcs

        obj.y_splines = None
        obj.u_splines = None
        obj.extra = None
        obj.converged = False
        return obj


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
        t, y, u, p, arcs = self.t, self.y, self.u, self.dynamical_parameters, self.arcs
        if not overwrite:
            t, y, u, arcs = new_t, new_y, new_u, new_arcs

        # Define every aux variable (such as constants) in the dictionary
        variables = [(aux_name, np.ones_like(t)*aux_val)
                     for aux_type in self.aux
                     if isinstance(self.aux[aux_type], dict)
                     for (aux_name, aux_val) in self.aux[aux_type].items()
                     if isinstance(aux_val, float)
                     ]
        # Define state variables
        # Have to do in this order to override state values with arrays
        variables += [(state, np.array(y[:, idx], dtype=np.float64))
                      for idx, state in enumerate(problem_data['state_list'])]

        # Define control variables
        variables += [(control, np.array(u[:, idx], dtype=np.float64))
                      for idx, control in enumerate(problem_data['control_list'])]

        t_list = []
        tf_ind = [str(p) for p in problem_data['dynamical_parameters']].index('tf')
        last_t = 0
        for arc_start, arc_end in arcs:
            start_t = t[arc_start]
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

    def evaluate(self, expr):
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
