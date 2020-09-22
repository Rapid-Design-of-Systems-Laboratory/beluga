import abc
import copy
import time

import numpy as np
import logging
import inspect
import itertools
import functools
import sys

from tqdm import tqdm

from beluga.symbolic import Problem
from beluga.symbolic.data_classes.components_structures import getattr_from_list


def gamma_norm(const1, const2):
    norm = sum(abs(const2 - const1))
    return norm


class ContinuationList(list):
    def __init__(self):

        list.__init__(self)

        # Create list of available strategies
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        self.strategy_list = {
            obj.strategy_name: obj
            for (name, obj) in clsmembers
            if hasattr(obj, 'strategy_name')
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
    """
    Class containing information for a continuation variable.
    """

    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.value = np.nan
        self.steps = []

    def __str__(self):
        return self.name + ' -> ' + str(self.target)


class ContinuationStrategy(abc.ABC):
    def __init__(self, *args, **kwargs):
        self.solution_reference = None
        self.gammas = []
        self.vars = {}
        self.ctr = None
        self.bvp = None
        self.constant_names = []

    def __str__(self):
        return str(self.vars)

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    def __len__(self):
        return self.num_cases()

    def add_gamma(self, gamma):
        self.gammas.append(copy.deepcopy(gamma))

    def get_closest_gamma(self, const):
        norms = []
        for traj in self.gammas:
            if traj.converged is False:
                norms.append(9e99)
            else:
                norms.append(gamma_norm(traj.const, const))

        return np.argmin(norms)

    def init(self, gamma, bvp):
        self.bvp = bvp
        # for var_name in self.var_iterator():
        #     if var_name not in [str(s['symbol']) for s in self.bvp.get_constants()]:
        #         raise ValueError('Variable ' + var_name + ' not found in boundary value problem')
        gamma_in = copy.deepcopy(gamma)
        gamma_in.converged = False
        self.gammas = [gamma_in]
        self.constant_names = getattr_from_list(bvp.constants, 'name')

    def next(self, ignore_last_step=False):
        if len(self.gammas) == 0:
            raise ValueError('No boundary value problem associated with this object')

        if not ignore_last_step and len(self.gammas) != 1 and not self.gammas[-1].converged:
            logging.error('The last step did not converge!')
            raise RuntimeError('Solution diverged! Stopping.')

        if self.ctr >= self.num_cases():
            raise StopIteration

        # Update auxiliary variables using previously calculated step sizes
        total_change = 0.0
        const0 = copy.deepcopy(self.gammas[-1].const)
        for var_name in self.vars:
            jj = self.constant_names.index(var_name)
            const0[jj] = self.vars[var_name].steps[self.ctr]
            total_change += abs(self.vars[var_name].steps[self.ctr])

        i = int(self.get_closest_gamma(const0))
        gamma_guess = copy.deepcopy(self.gammas[i])
        gamma_guess.const = const0
        self.ctr += 1
        logging.beluga('CHOOSE\ttraj #' + str(i) + ' as guess.')
        return gamma_guess

    def var_iterator(self):
        for var_name in self.vars.keys():
            yield var_name

    def num_cases(self):
        pass


class ManualStrategy(ContinuationStrategy):
    """
    Class defining the manual continuation strategy.
    """
    # A unique short name to select this class
    strategy_name = 'manual'

    def __init__(self, num_cases=1, _vars=None):  # TODO change vars to other variable name to avoid overwriting
        super(ManualStrategy, self).__init__()
        self._num_cases = num_cases
        self._spacing = 'linear'
        if _vars is None:
            self.vars = {}
        else:
            self.vars = _vars  # dictionary of values
        self.ctr = 0   # iteration counter
        self.last_sol = None

        self.const = functools.partial(self.set, param_type='const')
        self.orig_num_cases = num_cases
        self.constant = self.const

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def clear(self):
        """Clears all the previously set continuation variables"""
        self.vars = {}
        self.reset()

    # TODO: Change to store only step-size and use yield
    def init(self, sol, bvp):
        super(ManualStrategy, self).init(sol, bvp)

        # Iterate through all types of variables
        for var_name in self.var_iterator():
            if var_name not in self.constant_names:
                raise ValueError('Variable ' + var_name + ' not found in boundary value problem')

            # Set current value of each continuation variable
            jj = self.constant_names.index(var_name)
            self.vars[var_name].value = sol.const[jj]
            # Calculate update steps for continuation process
            if self._spacing == 'linear':
                self.vars[var_name].steps = np.linspace(self.vars[var_name].value,
                                                        self.vars[var_name].target,
                                                        self._num_cases)
            elif self._spacing == 'log':
                self.vars[var_name].steps = np.logspace(np.log10(self.vars[var_name].value),
                                                        np.log10(self.vars[var_name].target),
                                                        self._num_cases)

    def set(self, name, target, param_type):
        """
        Sets the target value for the specified parameter
        """
        # Create continuation variable object
        self.vars[name] = ContinuationVariable(name, target)
        return self

    def num_cases(self, num_cases=None, spacing='linear'):
        if num_cases is None:
            return self._num_cases

        if self.ctr > 0:
            raise RuntimeError('Cannot set num_cases during iteration')

        self._num_cases = num_cases
        self.orig_num_cases = num_cases
        self._spacing = spacing
        return self


class BisectionStrategy(ManualStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'bisection'

    def __init__(self, initial_num_cases=5, max_divisions=10, num_divisions=2):
        super(BisectionStrategy, self).__init__(num_cases=initial_num_cases)
        self.last_sol = None
        self.num_divisions = num_divisions
        self.max_divisions = max_divisions
        self.division_ctr = 0
        self.orig_num_cases = initial_num_cases

    def __str__(self):
        return ', '.join(str(continuationVariable) for continuationVariable in self.vars.values())

    def next(self, ignore_last_step=False):
        """Generator class to create BVPs for the continuation step iterations

        last_converged: Specfies if the previous continuation step converged
        """
        # If it is the first step or if previous step converged
        # continue with usual behavior
        if self.ctr == 0 or self.gammas[-1].converged:
            # Reset division counter
            self.division_ctr = 0
            return super(BisectionStrategy, self).next()

        # If first step didn't converge, the process fails
        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work.')
            raise RuntimeError('Initial guess does not converge.')
            # return self.gammas[-1]

        if self.division_ctr > self.max_divisions:
            logging.error('Solution does not without exceeding max_divisions : '+str(self.max_divisions))
            raise RuntimeError('Exceeded max_divisions')

        # If previous step did not converge, move back a half step
        for var_name in self.var_iterator():
            old_steps = self.vars[var_name].steps
            if self._spacing == 'linear':
                new_steps = np.linspace(old_steps[self.ctr-2], old_steps[self.ctr-1], self.num_divisions+1)
            elif self._spacing == 'log':
                new_steps = np.logspace(np.log10(old_steps[self.ctr-2]), np.log10(old_steps[self.ctr-1]),
                                        self.num_divisions+1)
            else:
                raise ValueError('Invalid spacing type')

            # Insert new steps
            self.vars[var_name].steps = np.insert(
                    self.vars[var_name].steps,
                    self.ctr-1,
                    new_steps[1:-1]  # Ignore first element as it is repeated
                )
        # Move the counter back
        self.ctr = self.ctr - 1
        # Increment total number of steps
        self._num_cases = self._num_cases + self.num_divisions-1

        logging.beluga('Increasing number of cases to '+str(self._num_cases)+'\n')
        self.division_ctr = self.division_ctr + 1
        return super(BisectionStrategy, self).next(True)


class ProductStrategy(ContinuationStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'productspace'

    def __init__(self, num_subdivisions=1, sol=None):
        ContinuationStrategy.__init__(self)
        self.sol = sol
        self.sols = []
        self._num_cases = None
        self._num_subdivisions = num_subdivisions
        self.division_ctr = 0
        self.vars = {}  # dictionary of values
        self.ctr = 0  # iteration counter

        self.const = functools.partial(self.set, param_type='const')
        self.constant = self.const

        self.last_sol = None
        self.orig_num_cases = None

    def __str__(self):
        return str(self.vars)

    def next(self, ignore_last_step=False):
        if self.ctr == 0 or self.gammas[-1].converged:
            # Reset division counter
            self.division_ctr = 0
            return super(ProductStrategy, self).next(False)

        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work.')
            raise RuntimeError('Initial guess does not converge.')

        return super(ProductStrategy, self).next(True)

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def set(self, name, target, param_type):
        """
        Sets the target value for the specified parameter
        """
        self.vars[name] = ContinuationVariable(name, target)
        return self

    def init(self, sol, bvp):
        super(ProductStrategy, self).init(sol, bvp)

        num_vars = len(self.vars)
        self.num_cases(self.num_subdivisions() ** num_vars)
        for var_name in self.vars.keys():
            jj = bvp.raw['constants'].index(var_name)
            self.vars[var_name].value = sol.const[jj]

        ls_set = [np.linspace(self.vars[var_name].value, self.vars[var_name].target,
                              self._num_subdivisions) for var_name in self.vars.keys()]
        for val in itertools.product(*ls_set):
            ii = 0
            for var_name in self.vars.keys():
                self.vars[var_name].steps.append(val[ii])
                ii += 1

    def num_cases(self, num_cases=None):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self.orig_num_cases = num_cases
            return self

    def num_subdivisions(self, num_subdivisions=None):
        if num_subdivisions is None:
            return self._num_subdivisions
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')
            self._num_subdivisions = num_subdivisions
            return self


class SparseProductStrategy(ContinuationStrategy):
    """
    Defines the bisection continuation strategy.
    """
    strategy_name = 'sparse_product'

    def __init__(self, num_subdivisions=((1,), (0,)), sol=None):
        ContinuationStrategy.__init__(self)
        self.sol = sol
        self.sols = []
        self._num_cases = None
        self._num_subdivisions = num_subdivisions
        self.division_ctr = 0
        self.vars = {}  # dictionary of values
        self.ctr = 0  # iteration counter

        self.const = functools.partial(self.set, param_type='const')
        self.constant = self.const

        self.last_sol = None
        self.orig_num_cases = None

        self.case_list = []

    def __str__(self):
        return str(self.vars)

    def next(self, ignore_last_step=False):
        if self.ctr == 0 or self.gammas[-1].converged:
            # Reset division counter
            self.division_ctr = 0
            return super(SparseProductStrategy, self).next(False)

        if self.ctr == 1:
            logging.error('Initial guess should converge for automated continuation to work.')
            raise RuntimeError('Initial guess does not converge.')

        return super(SparseProductStrategy, self).next(True)

    def reset(self):
        """Resets the internal step counter to zero"""
        self.ctr = 0
        self.last_sol = None

    def set(self, name, target, param_type):
        """
        Sets the target value for the specified parameter
        """
        self.vars[name] = ContinuationVariable(name, target)
        return self

    def init(self, sol, bvp):
        super(SparseProductStrategy, self).init(sol, bvp)

        lower_bounds = []
        upper_bounds = []

        num_vars = len(self.vars)
        for var_name in self.vars.keys():
            jj = bvp.raw['constants'].index(var_name)
            self.vars[var_name].value = sol.const[jj]
            lower_bounds.append(sol.const[jj])
            upper_bounds.append(self.vars[var_name].target)

        major_num_steps = self._num_subdivisions[0]
        minor_num_steps = self._num_subdivisions[1]

        step_list = [lower_bounds]
        major_point_cloud = [lower_bounds]
        minor_point_cloud = []

        for n in range(num_vars):
            new_maj_pnts = []
            maj_step_series = np.linspace(lower_bounds[n], upper_bounds[n], major_num_steps[n])
            for maj_point in major_point_cloud:
                maj_pnt_line = []
                for maj_step in maj_step_series:
                    new_pnt = list(maj_point)
                    new_pnt[n] = maj_step
                    maj_pnt_line.append(tuple(new_pnt))

                for maj_pnt_0, maj_pnt_1 in zip(maj_pnt_line[:-1], maj_pnt_line[1:]):
                    min_step_series = np.linspace(maj_pnt_0[n], maj_pnt_1[n], minor_num_steps[n]+1, endpoint=False)[1:]
                    for min_step in min_step_series:
                        new_point = list(maj_pnt_0)
                        new_point[n] = min_step
                        step_list.append(tuple(new_point))
                        minor_point_cloud.append(tuple(new_point))

                    step_list.append(maj_pnt_1)

                new_maj_pnts += maj_pnt_line[1:]
            major_point_cloud += new_maj_pnts

        self.num_cases(len(step_list))

        for step in step_list:
            for n, var_name in enumerate(self.vars.keys()):
                self.vars[var_name].steps.append(step[n])

    def num_cases(self, num_cases=None):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self.orig_num_cases = num_cases
            return self

    def num_subdivisions(self, num_subdivisions=None):
        if num_subdivisions is None:
            return self._num_subdivisions
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')
            self._num_subdivisions = num_subdivisions
            return self


def run_continuation_set(bvp_algorithm_, steps, solinit, bvp: Problem, pool, autoscale):
    """
    Runs a continuation set for the BVP problem.

    :param bvp_algorithm_: BVP algorithm to be used.
    :param steps: The steps in a continuation set.
    :param solinit: Initial guess for the first problem in steps.
    :param bvp: The compiled boundary-value problem to solve.
    :param pool: A processing pool, if available.
    :param autoscale: Whether or not scaling is used.
    :return: A set of solutions for the steps.
    """
    # Loop through all the continuation steps
    solution_set = []

    functional_problem = bvp.functional_problem

    # Initialize scaling
    scale = functional_problem.scale_sol
    compute_factors = functional_problem.compute_scale_factors

    # Load the derivative function into the bvp algorithm
    bvp_algorithm_.set_derivative_function(functional_problem.deriv_func)
    bvp_algorithm_.set_derivative_jacobian(functional_problem.deriv_func_jac)
    bvp_algorithm_.set_quadrature_function(functional_problem.quad_func)
    bvp_algorithm_.set_boundarycondition_function(functional_problem.bc_func)
    bvp_algorithm_.set_boundarycondition_jacobian(functional_problem.bc_func_jac)
    bvp_algorithm_.set_inequality_constraint_function(functional_problem.ineq_constraints)

    sol_guess = solinit

    if steps is None:
        logging.info('Solving OCP...')
        time0 = time.time()
        if autoscale:
            scale_factors = compute_factors(sol_guess)
            sol_guess = scale(sol_guess, scale_factors)
        else:
            scale_factors = None

        opt = bvp_algorithm_.solve(sol_guess, pool=pool)
        sol = opt['sol']

        if autoscale:
            sol = scale(sol, scale_factors, inv=True)

        solution_set = [[sol]]
        if sol.converged:
            elapsed_time = time.time() - time0
            logging.beluga('Problem converged in %0.4f seconds\n' % elapsed_time)
        else:
            logging.beluga('Problem failed to converge!\n')
    else:
        for step_idx, step in enumerate(steps):
            logging.beluga('\nRunning Continuation Step #{} ({})'.format(step_idx+1, step)+' : ')
            # logging.beluga('Number of Iterations\t\tMax BC Residual\t\tTime to Solution')
            solution_set.append([])
            # Assign solution from last continuation set
            step.reset()
            step.init(sol_guess, bvp)
            try:
                log_level = logging.getLogger()._displayLevel
            except AttributeError:
                log_level = logging.getLogger().getEffectiveLevel()

            step_len = len(step)
            continuation_progress = tqdm(
                step, disable=log_level is not logging.INFO, desc='Continuation #' + str(step_idx+1),
                ascii=True, unit='trajectory')
            for sol_guess in continuation_progress:
                continuation_progress.total = len(step)
                if step_len != continuation_progress.total:
                    step_len = continuation_progress.total
                    continuation_progress.refresh()

                logging.beluga('START \tIter {:d}/{:d}'.format(step.ctr, step.num_cases()))
                time0 = time.time()
                if autoscale:
                    scale_factors = compute_factors(sol_guess)
                    sol_guess = scale(sol_guess, scale_factors)
                else:
                    scale_factors = None

                opt = bvp_algorithm_.solve(sol_guess, pool=pool)
                sol = opt['sol']

                if autoscale:
                    sol = scale(sol, scale_factors, inv=True)

                ya = sol.y[0, :]
                yb = sol.y[-1, :]

                dp = sol.dynamical_parameters
                ndp = sol.nondynamical_parameters
                k = sol.const

                if sol.q.size > 0:
                    qa = sol.q[0, :]
                    qb = sol.q[-1, :]

                    bc_residuals_unscaled = bvp_algorithm_.boundarycondition_function(ya, qa, yb, qb, dp, ndp, k)

                else:
                    bc_residuals_unscaled = bvp_algorithm_.boundarycondition_function(ya, yb, dp, ndp, k)

                step.add_gamma(sol)

                """
                The following line is overwritten by the looping variable UNLESS it is the final iteration. It is
                required when chaining continuation strategies together. DO NOT DELETE!
                """
                sol_guess = copy.deepcopy(sol)
                elapsed_time = time.time() - time0
                logging.beluga(
                    'STOP  \tIter {:d}/{:d}\tBVP Iters {:d}\tBC Res {:13.8E}\tTime {:13.8f}'
                    .format(step.ctr, step.num_cases(), opt['niter'], max(bc_residuals_unscaled), elapsed_time))
                solution_set[step_idx].append(copy.deepcopy(sol))
                if not sol.converged:
                    logging.beluga('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))

    return solution_set