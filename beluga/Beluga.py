from math import *
from beluga.utils import *
from beluga.optim import *

import matplotlib.pyplot as plt
import numpy as np
import sys,os,imp,inspect,warnings

from beluga import BelugaConfig
from beluga.continuation import *
from beluga.bvpsol import algorithms

import dill, logging

class Beluga(object):
    """!
    \brief     Main class of mission design tool.
    \details   This class contains all of the information associated with the
                mission design problem.
    \author    Michael Grant
    \author    Thomas Antony
    \version   0.1
    \date      06/30/15
    \pre       First create problem file.
    \copyright Coming.
    \bug       Probably exists.
    """
    # __metaclass__ = SingletonMetaClass
    version = '0.1'
    _THE_MAGIC_WORD = object()
    instance = None

    config = BelugaConfig() # class variable globally accessible

    def __init__(self,problem,token,input_module=None):
        """!
        \brief     Initializes class of mission design tool.
        \details   Assigns problem data based on the input file.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """
        self.problem = problem
        # self.input_module = input_module

        # # Ensure user does not create an object with the Beluga class
        # if token is not self._THE_MAGIC_WORD:
        #     raise ValueError("Don't construct directly, use create() or run()")

    @classmethod
    def init_logging(cls, logging_level, display_level):
        """Initializes the logging system"""
        # Define custom formatter class that formats messages based on level
        # Ref: http://stackoverflow.com/a/8349076/538379
        class InfoFormatter(logging.Formatter):
            """Custom logging formatter to output info messages by themselves"""
            info_fmt = '%(message)s'
            def format(self, record):
                # Save the original format configured by the user
                # when the logger formatter was instantiated
                format_orig = self._fmt

                # Replace the original format with one customized by logging level
                if record.levelno == logging.INFO:
                    self._fmt = self.info_fmt
                    # For Python>3.2
                    self._style = logging.PercentStyle(self._fmt)

                # Call the original formatter class to do the grunt work
                result = logging.Formatter.format(self, record)

                # Restore the original format configured by the user
                self._fmt = format_orig
                # For Python>3.2
                self._style = logging.PercentStyle(self._fmt)

                return result

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(cls.config['logfile'])
        fh.setLevel(logging_level)
        # Set default format string based on logging level
        # TODO: Change this to use logging configuration file?
        if logging_level == logging.DEBUG:
            formatter = logging.Formatter('[%(levelname)s] %(asctime)s-%(module)s#%(lineno)d-%(funcName)s(): %(message)s')
        else:
            formatter = logging.Formatter('[%(levelname)s] %(asctime)s-%(filename)s:%(lineno)d: %(message)s')

        # Create logging handler for console output
        ch = logging.StreamHandler(sys.stdout)
        # Set console logging level and formatter
        ch.setLevel(display_level)
        formatter = InfoFormatter('%(filename)s:%(lineno)d: %(message)s')
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    @classmethod
    def run(cls, problem, logging_level=logging.INFO, display_level=logging.INFO, output_file=None):
        """!
        \brief     Returns Beluga object.
        \details   Takes a problem statement, instantiates a solver object and begins
                    the solution process.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # Get reference to the input file module
        frm = inspect.stack()[1]
        input_module = (inspect.getmodule(frm[0]))

        # Get information about input file
        info = inspect.getframeinfo(frm[0])

        # Suppress warnings
        warnings.filterwarnings("ignore")

        # Include configuration file path
        sys.path.append(cls.config.getroot())

        # TODO: Get default solver options from configuration or a defaults file
        if problem.bvp_solver is None:
            # problem.bvp_solver = algorithms.SingleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = False)
            problem.bvp_solver = algorithms.MultipleShooting(derivative_method='fd',tolerance=1e-4, max_iterations=1000, verbose = True, cached=False, number_arcs=2)

        # Set the cache directory to be in the current folder
        cache_dir = os.getcwd()+'/_cache'
        # cache_dir = os.path.dirname(info.filename)+'/_cache'
        try:
            os.mkdir(cache_dir)
        except:
            pass
        problem.bvp_solver.set_cache_dir(cache_dir)

        # Initialize logging system
        cls.init_logging(logging_level,display_level)

        # Set the output file name
        if output_file is not None:
            problem.output_file = output_file

        if isinstance(problem,Problem):
            # Create instance of Beluga class
            inst = cls(problem, cls._THE_MAGIC_WORD)
            inst.solve()
            return
            # return inst
        else:
            #TODO:Add functionality for when problem is specified by filename
            pass

    def solve(self):
        """!
        \brief     Returns Beluga object.
        \details   Starts the solution process.
        \author    Thomas Antony
        \version   0.1
        \date      06/30/15
        """

        # Initialize necessary conditions of optimality object
        # print("Computing the necessary conditions of optimality")
        logging.info("Computing the necessary conditions of optimality")
        self.nec_cond = NecessaryConditions()

        # Create corresponding boundary value problem
        bvp = self.nec_cond.get_bvp(self.problem)

        # TODO: Implement other types of initial guess depending on data type
        #       Array: Automatic?
        #       Guess object: Directly use
        #       Function handle: Call function
        #       String: Load file?

        # The initial guess is automatically stored in the bvp object
        # solinit is just a reference to it
        solinit = self.problem.guess.generate(bvp)

        # includes costates
        state_names = self.nec_cond.problem_data['state_list']
        initial_states = solinit.y[:,0] # First column
        terminal_states = solinit.y[:,-1] # Last column
        initial_bc = dict(zip(state_names,initial_states))
        terminal_bc = dict(zip(state_names,terminal_states))
        bvp.solution.aux['initial'] = initial_bc
        bvp.solution.aux['terminal'] = terminal_bc

        tic()
        # TODO: Start from specific step for restart capability
        # TODO: Make class to store result from continuation set?
        self.out = {};
        self.out['problem_data'] = self.nec_cond.problem_data;

        self.out['solution'] = self.run_continuation_set(self.problem.steps, bvp)
        total_time = toc();

        logging.info('Continuation process completed in %0.4f seconds.\n' % total_time)

        # Save data
        output = open(self.problem.output_file, 'wb')
        # dill.settings['recurse'] = True
        dill.dump(self.out, output) # Dill Beluga object only
        output.close()

        # plt.title('Solution for Brachistochrone problem')
        # plt.plot(self.out['solution'][-1][1,:]*180/pi,self.out['solution'][-1][0,:]/1000)
        plt.xlabel('theta')
        plt.ylabel('h')
        plt.show(block=False)

    # TODO: Refactor how code deals with initial guess
    def run_continuation_set(self,steps,bvp_start):
        # Loop through all the continuation steps
        solution_set = []

        # Initialize scaling
        import sys, copy
        s = self.problem.scale
        s.initialize(self.problem,self.nec_cond.problem_data)
        try:
            for step_idx,step in enumerate(steps):
                # Assign BVP from last continuation set
                step.reset()
                logging.info('\nRunning Continuation Step #'+str(step_idx+1)+' : ')

                solution_set.append(ContinuationSolution())
                if step_idx == 0:
                    step.set_bvp(bvp_start)
                else:
                    # Use the bvp & solution from last continuation set
                    step.set_bvp(steps[step_idx-1].bvp)

                for bvp in step:
                    logging.info('Starting iteration '+str(step.ctr)+'/'+str(step.num_cases()))
                    tic()

                    s.compute_scaling(bvp)
                    s.scale(bvp)

                    # sol is just a reference to bvp.solution
                    sol = self.problem.bvp_solver.solve(bvp)

                    s.unscale(bvp)
                    if sol.converged:
                        # Post-processing phase
                        # Compute control history
                        # sol.u = np.zeros((len(self.nec_cond.problem_data['control_list']),len(sol.x)))

                        # Required for plotting to work with control variables
                        sol.ctrl_expr = self.nec_cond.problem_data['control_options']
                        sol.ctrl_vars = self.nec_cond.problem_data['control_list']

                        #TODO: Make control computation more efficient
                        # for i in range(len(sol.x)):
                        #     _u = bvp.control_func(sol.x[i],sol.y[:,i],sol.parameters,sol.aux)
                        #     sol.u[:,i] = _u
                        f = lambda _t, _X: bvp.control_func(_t,_X,sol.parameters,sol.aux)
                        sol.u = np.array(list(map(f, sol.x, list(sol.y.T)))).T

                        # Update solution for next iteration
                        solution_set[step_idx].append(copy.deepcopy(bvp.solution))

                        elapsed_time = toc()
                        logging.info('Iteration %d/%d converged in %0.4f seconds\n' % (step.ctr, step.num_cases(), elapsed_time))
                    else:
                        elapsed_time = toc()
                        logging.info('Iteration %d/%d failed to converge!\n' % (step.ctr, step.num_cases()))
        except Exception as e:
            logging.error('Exception : '+str(e))
            logging.error('Stopping')

        return solution_set
