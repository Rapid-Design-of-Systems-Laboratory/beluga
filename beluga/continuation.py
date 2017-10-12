"""
Module: continuation2

Holds all classes and functions related to continuation
"""
import numpy as np
import logging
import inspect
import functools
import sys

import operator as op
from beluga.utils import keyboard
class ContinuationList(list):
    def __init__(self):
        # Create list of available strategies
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        self.strategy_list = {obj.strategy_name: obj
                                for (name,obj) in clsmembers
                                if hasattr(obj,'strategy_name')
                              }

    def add_step(self, strategy='manual', *args, **kwargs):
        """
        Adds a continuation step with specified strategy

        Returns the strategy object to further chain calls into it
        """
        # Create object if strategy is specified as a string
        if isinstance(strategy, str):
            if strategy in self.strategy_list:
                strategy_obj = self.strategy_list[strategy](*args, **kwargs)
            else:
                logging.error('Invalid strategy name')
                raise ValueError('Continuation strategy : '+strategy+' not found.')
        else:
            strategy_obj = strategy

        self.append(strategy_obj)
        return strategy_obj


class ContinuationVariable(object):
    def __init__(self,name,target):
        self.name = name
        self.target = target
        self.value = np.nan
        self.steps = []

class ActivateConstraint(object):
    strategy_name = 'activate_constraint'
    def __init__(self, name):
        self.name = name
        self.solved = False
        self.ctr  = 0

    def num_cases(self):
        return 1

    def reset(self):
        self.solved = False

    def clear(self):
        self.solved = False

    def init(self, sol, problem_data):
        """Split the solution into arcs to introduce constraint."""
        # Get expr corresponding to name
        s = sol.aux['constraints'][self.name]
        expr = s['expr']
        arc_type = s['arc_type']
        pi_list = s['pi_list']
        num_params = problem_data['num_params']

        current_arcs = sol.arcs
        current_arcseq = sol.aux.get('arc_seq', (0,))
        if current_arcs is None:
            current_arcs = [(0, len(sol.x)-1)]

        sol.prepare(problem_data, 200, True)
        # Evaluate expr on sol
        s_vals = sol.evaluate(expr)

        # Find zero crossing
        # TODO: add check to see if constraint active

        if s['direction'] == '>':
            # Find min value (most away from zero)
            s_lim_i = np.argmin(s_vals)
            s_lim_val = s_vals[s_lim_i]
            if s_lim_val > 0:
                print('Constraint is not active')
            s_lim_val = min(0, s_lim_val)
            # print('Max_violation : ', s_lim_val)
        else:
            # Find max value
            s_lim_i = np.argmax(s_vals)
            s_lim_val = s_vals[s_lim_i]
            if s_lim_val < 0:
                print('Constraint is not active')
            s_lim_val = max(0, s_lim_val)
            # print('Max_violation : ', s_lim_val)

        if s_lim_i == 0:
            s_lim_i = 1
        elif s_lim_i == len(sol.x)-1:
            s_lim_i = s_lim_i - 1

        arc_to_split = int(np.floor(sol.x[s_lim_i]))
        logging.info('Added constrained arc with max violation : %.4lf %s in arc %d' % (s_lim_val, s['unit'], arc_to_split))

        # Store constraint limit in aux
        sol.aux['constraint'][(self.name, 1)] = s_lim_val

        arc_num = arc_to_split
        old_arc_idx = sol.arcs[arc_num] # See where previous arc starts and ends

        # new arc index relative to start of previous arc
        idx_arc_start = s_lim_i - old_arc_idx[0]
        idx_arc_end = s_lim_i+1 - old_arc_idx[0]

        old_arc_idx = (old_arc_idx[0], old_arc_idx[1]+1)
        old_arc_x = np.array(sol.x[slice(*old_arc_idx)], copy=True)
        old_arc_y = np.array(sol.y[:,slice(*old_arc_idx)], copy=True)
        old_arc_u = np.array(sol.u[:,slice(*old_arc_idx)], copy=True)
        original_tf = old_arc_y[-1,0]

        t_before = old_arc_x[idx_arc_start]*original_tf
        t_during = (old_arc_x[idx_arc_end] - old_arc_x[idx_arc_start])*original_tf
        t_after = (old_arc_x[-1] - old_arc_x[idx_arc_end])*original_tf

        logging.info('Arc position : t='+str(sol.x[s_lim_i])+'s')
        old_arc_x[0:idx_arc_start+1] = (old_arc_x[0:idx_arc_start+1] - old_arc_x[0])/(old_arc_x[idx_arc_start] - old_arc_x[0]) + arc_num # TODO: Fix for multi arc
        old_arc_x[idx_arc_end:] = (old_arc_x[idx_arc_end:] - old_arc_x[idx_arc_end])/(old_arc_x[-1] - old_arc_x[idx_arc_end]) + arc_num + 2

        new_arc_x = np.hstack((old_arc_x[:idx_arc_start+1], old_arc_x[idx_arc_start:idx_arc_end+1], old_arc_x[idx_arc_end:]))
        new_arc_y = np.hstack((old_arc_y[:,:idx_arc_start+1], old_arc_y[:,idx_arc_start:idx_arc_end+1], old_arc_y[:,idx_arc_end:]))
        new_arc_u = np.hstack((old_arc_u[:,:idx_arc_start+1], old_arc_u[:,idx_arc_start:idx_arc_end+1], old_arc_u[:,idx_arc_end:]))

        new_arc_y[-1,:idx_arc_start+1] = t_before
        new_arc_y[-1,idx_arc_start+1] = t_during # "tf" for constrained arc
        new_arc_y[-1,idx_arc_end+1] = t_during
        new_arc_y[-1,idx_arc_end+2:] = t_after

        num_odes = sol.y.shape[0]
        num_controls = sol.u.shape[0]
        sol.x = np.hstack((sol.x[:old_arc_idx[0]], new_arc_x, sol.x[old_arc_idx[1]:]))
        sol.y = np.hstack((sol.y[:,:old_arc_idx[0]], new_arc_y, sol.y[:,old_arc_idx[1]:]))
        sol.u = np.hstack((sol.u[:,:old_arc_idx[0]], new_arc_u, sol.u[:,old_arc_idx[1]:]))

        new_arcs = [(old_arc_idx[0], old_arc_idx[0]+idx_arc_start),
                    (old_arc_idx[0]+idx_arc_start+1, old_arc_idx[0]+idx_arc_end+1),
                    (old_arc_idx[0]+idx_arc_end+2, old_arc_idx[0]+len(new_arc_x)-1)]

        sol.arcs = (*sol.arcs[:arc_num], *new_arcs, *sol.arcs[arc_num+1:])
        arc_seq = (*sol.aux['arc_seq'][:arc_num+1], arc_type, *sol.aux['arc_seq'][arc_num:])
        sol.aux['arc_seq'] = arc_seq

        pi_idx_start = len(sol.parameters)
        pi_idx = np.array(list(range(pi_idx_start, pi_idx_start+len(pi_list))))
        sol.parameters = np.append(sol.parameters, np.ones(len(pi_list))*0.0)

        if len(pi_idx) == 0:
            pi_idx = None
        new_pi_seq = (None, pi_idx, None)
        pi_seq = (*sol.aux['pi_seq'][:arc_num], *new_pi_seq, *sol.aux['pi_seq'][arc_num+1:])
        sol.aux['pi_seq'] = pi_seq

        # keyboard()
        self.sol = sol

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        if self.solved:
            raise StopIteration
        else:
            self.solved = True
            self.ctr += 1
            return self.sol.aux


# Can be subclassed to allow automated stepping
class ManualStrategy(object):
    """Defines one continuation step in continuation set"""
    # A unique short name to select this class
    strategy_name = 'manual'

    def __init__(self, num_cases = 1,vars=[], sol=None):
        self.sol = sol
        self._num_cases = num_cases
        self._spacing = 'linear'
        self.vars = {}  # dictionary of values
        self.ctr  = 0   # iteration counter
        self.last_sol = None

        self.terminal = functools.partial(self.set, param_type='terminal')
        self.initial = functools.partial(self.set, param_type='initial')
        self.const = functools.partial(self.set, param_type='const')

        self.constant = self.const

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def clear(self):
        """Clears all the previously set continuation variables"""
        self.vars = {}
        self.reset()

    def constraint(self, name, target, index):
        """Continuation on constraint limit.

        index : Specify which constraint arc to use."""
        # sol.aux['constraints'][self.name]['limit'][1]
        self.set((name,index), target, param_type='constraint')

    def var_iterator(self):
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                yield var_type, var_name

    # TODO: Change to store only stepsize and use yield
    def init(self, sol, problem_data):
        self.sol = sol

        # Iterate through all types of variables
        for var_type, var_name in self.var_iterator():
        # for var_type in self.vars.keys():
        #     for var_name in self.vars[var_type].keys():
            # Look for the variable name from continuation in the BVP
            if var_name not in sol.aux[var_type].keys():
                raise ValueError('Variable '+var_name+' not found in boundary value problem')

            # Set current value of each continuation variable
            self.vars[var_type][var_name].value = sol.aux[var_type][var_name]
            # Calculate update steps for continuation process
            if self._spacing == 'linear':
                self.vars[var_type][var_name].steps = np.linspace(self.vars[var_type][var_name].value,
                                                                  self.vars[var_type][var_name].target,
                                                                  self._num_cases)
            elif self._spacing == 'log':
                self.vars[var_type][var_name].steps = np.logspace(np.log10(self.vars[var_type][var_name].value),
                                                                  np.log10(self.vars[var_type][var_name].target),
                                                                  self._num_cases)

    def set(self,name,target,param_type):
        """
        Sets the target value for the specified parameter
        """
        if param_type not in self.vars.keys():
            self.vars[param_type] = {}

        # Create continuation variable object
        self.vars[param_type][name] = ContinuationVariable(name,target)
        return self

    def num_cases(self,num_cases=None,spacing='linear'):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self._spacing   = spacing
            return self

        self.set('const',name,target)
        return self

    def __str__(self):
        return str(self.vars)

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    def next(self, ignore_last_step = False):
        """Generator class to create BVPs for the continuation step iterations
        ignore_last_step: Should the non-convergence of previous step be ignored?
        """

        if self.sol is None:
            raise ValueError('No boundary value problem associated with this object')

        if not ignore_last_step and self.last_sol is not None and not self.last_sol.converged:
            logging.error('The last step did not converge!')
            raise RuntimeError('Solution diverged! Stopping.')

        if self.ctr >= self._num_cases:
            raise StopIteration

        # Update auxiliary variables using previously calculated step sizes
        for var_type in self.vars:
            for var_name in self.vars[var_type]:
                self.sol.aux[var_type][var_name] = self.vars[var_type][var_name].steps[self.ctr]

        self.ctr += 1
        self.last_sol = self.sol
        return self.sol.aux

class BisectionStrategy(ManualStrategy):
    """Defines one continuation step in continuation set"""
    # A unique short name to select this class
    strategy_name = 'bisection'

    def __init__(self, initial_num_cases = 5, max_divisions=10, num_divisions = 2, vars=[], aux=None):
        super(BisectionStrategy, self).__init__(num_cases=initial_num_cases)
        self.last_sol = None
        self.num_divisions = num_divisions
        self.max_divisions = max_divisions
        self.division_ctr = 0

    def __str__(self):
        return str(self.vars)

    def next(self):
        """Generator class to create BVPs for the continuation step iterations

            last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.last_sol.converged:
            # Reset division counter
            self.division_ctr = 0
            return super(BisectionStrategy, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work!!')
            raise RuntimeError('Initial guess does not converge.')
            return self.last_sol

        if self.division_ctr > self.max_divisions:
            logging.error('Solution does not without exceeding max_divisions : '+str(self.max_divisions))
            raise RuntimeError('Exceeded max_divisions')

        # If previous step did not converge, move back a half step
        for var_type, var_name in self.var_iterator():
            # Set current value of each continuation variable
            # self.vars[var_type][var_name].value = aux[var_type][var_name]
            # insert new steps
            old_steps = self.vars[var_type][var_name].steps
            if self._spacing == 'linear':
                new_steps = np.linspace(old_steps[self.ctr-2],old_steps[self.ctr-1],self.num_divisions+1)
            elif self._spacing == 'log':
                new_steps = np.logspace(np.log10(old_steps[self.ctr-2]),np.log10(old_steps[self.ctr-1]),self.num_divisions+1)
            else:
                raise ValueError('Invalid spacing type')

            # Insert new steps
            self.vars[var_type][var_name].steps = np.insert(
                    self.vars[var_type][var_name].steps,
                    self.ctr-1,
                    new_steps[1:-1] # Ignore first element as it is repeated
                )
        # Move the counter back
        self.ctr = self.ctr - 1
        # Increment total number of steps
        self._num_cases = self._num_cases + self.num_divisions-1

        logging.info('Increasing number of cases to '+str(self._num_cases)+'\n')
        self.division_ctr = self.division_ctr + 1
        return super(BisectionStrategy, self).next(True)
