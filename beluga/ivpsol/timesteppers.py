import abc
import numpy as np
import copy
import csv
import os
from beluga.liepack import *

# The following math import statements appear to be unused, but they are required on import of the specific
# methods since an eval() is called
from math import sqrt

class Method(object):
    """
    Class containing information on various integration methods. It's primary purpose is not to perform explicit
    calculations, but rather to load and store saved schemes.
    """

    def __new__(cls, *args, **kwargs):
        """
        Created a new Method object.

        :param name: Name of a method.
        :return: Method object.
        """

        obj = super(Method, cls).__new__(cls)
        obj.name = 'RK4'
        obj.data = None

        if len(args) > 0:
            obj.name = args[0].upper()

        return obj

    def __init__(self, *args, **kwargs):
        self.loadmethods()

        self.RKtype = self.data[self.name]['type']
        self.RKa = np.array(self.data[self.name]['a'], dtype=np.float64)
        self.RKb = np.array(self.data[self.name]['b'], dtype=np.float64)
        self.RKbhat = np.array(self.data[self.name]['bhat'], dtype=np.float64)
        self.RKc = np.array(self.data[self.name]['c'], dtype=np.float64)
        self.RKord = int(self.data[self.name]['order'])
        self.RKns = int(self.data[self.name]['n'])
        self.variable_step = sum(self.RKbhat) != 0

    def loadmethods(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + '/methods/RK.csv', mode='r', encoding='utf-8-sig', newline='\n') as RKfile:
            reader = csv.reader(RKfile, delimiter=',')
            num_methods = 0
            data = {}
            for row in reader:
                if num_methods == 0:
                    header = row
                else:
                    L = len(header)
                    name = row[0]
                    key = [header[1]]
                    val = [row[1]]
                    key += [_ for _ in header[2:]]
                    val += [eval(_) for _ in row[2:]]
                    data[name] = dict(zip(key, val))

                num_methods += 1
        self.data = data

    def getmethods(self):
        return self.data.keys()


class TimeStepper(object):
    """
    This class serves as a superclass for various time stepper objects. The purpose of a timestepper is to advance
    numerical solutions of ordinary differential equations a single time step per evaluation.
    """

    def __new__(cls, *args, **kwargs):
        """
        Creates a new TimeStepper object.

        :param args:
        :param kwargs:
        :return:
        """

        obj = super(TimeStepper, cls).__new__(cls)

        obj.variablestep = False

        if len(args) == 0:
            obj.coordinate = 'exp'
            obj.method = Method('RK4')

        return obj

    @abc.abstractmethod
    def __call__(self, vf, y, t0, dt):
        pass

    def getcoordinate(self):
        return self.coordinate

    def getmethod(self):
        return self.method

    def setcoordinate(self, coordinate):
        coordinate = coordinate.lower()
        if coordinate == 'exp':
            self.coordinate = 'exp'
        else:
            raise NotImplementedError

    def setmethod(self, method):
        self.method = Method(method)


class RKMK(TimeStepper):
    """
    The Runge-Kutta-Munthe-Kaas time stepper object.
    """

    def __call__(self, vf, y, t0, dt):
        """
        Advances a numerical solution.

        :param vf: Vectorfield object.
        :param y: Homogeneous space.
        :param t0: Initial time.
        :param dt: Time to advance (for fixed-step methods).
        :return: (y_low, y_high, errest) - A "low" quality and "high" quality estimate for solutions, and an error estimate.
        """
        g = group2algebra(y.shape)
        Kj = [g(y.shape.shape) for _ in range(self.method.RKns)]
        Yr = [copy.copy(y) for _ in range(self.method.RKns)]
        if self.method.RKtype == 'explicit':
            Kj[0] = vf(t0, y)
            for ii in range(self.method.RKns - 1):
                U = sum([elem*dt*coeff for elem, coeff in zip(Kj[:ii+1], self.method.RKa[ii+1, :ii+1])])
                Yr[ii+1] = Left(exp(U), y)
                K = vf(t0 + dt*self.method.RKc[ii+1], Yr[ii+1])
                Kj[ii+1] = dexpinv(U, K, order=self.method.RKord-1)

        elif self.method.RKtype == 'implicit':
            Kjold = copy.copy(Kj)
            tol = 1e-15
            max_iter = 50
            iter = 0
            iter_dist = 1 + tol
            while (iter_dist > tol) and (iter < max_iter):
                iter += 1
                for ii in range(self.method.RKns):
                    U = sum([elem*dt*coeff for elem, coeff in zip(Kjold, self.method.RKa[ii, :])])
                    K = vf(t0 + dt*self.method.RKc[ii], Left(exp(U), y))
                    Kj[ii] = dexpinv(U, K, order=self.method.RKord-1)
                iter_dist = sum(np.linalg.norm(v1.get_vector() - v2.get_vector()) for v1,v2 in zip(Kj, Kjold))
                Kjold = copy.copy(Kj)


        Ulow = sum([Kval*dt*coeff for Kval, coeff in zip(Kj, self.method.RKb)])
        ylow = Left(exp(Ulow), y)
        errest = -1
        yhigh = None

        if self.variablestep:
            if not self.method.variable_step:
                raise NotImplementedError(self.method.name + ' does not support variable stepsize.')

            Uhigh = sum([Kval*dt*coeff for Kval, coeff in zip(Kj, self.method.RKbhat)])
            yhigh = Left(exp(Uhigh), y)
            errest = np.linalg.norm(Ulow.get_vector() - Uhigh.get_vector())

        return ylow, yhigh, errest
