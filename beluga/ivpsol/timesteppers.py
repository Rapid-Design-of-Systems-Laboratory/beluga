import abc
import numpy as np
# from beluga.liepack.domain.liealgebras import LieAlgebra
import copy
import csv
import os
from beluga.utils import keyboard

# The following math import statements appear to be unused, but they are required on import of the specific
# methods since an eval() is called
from math import sqrt

class Method(object):
    """
    Class containing information on various integration methods. It's primary purpose is not to perform explicit
    calculations, but rather to load and store saved schemes.
    """

    def __new__(cls, name):
        """
        Created a new Method object.

        :param name: Name of a method.
        :return: Method object.
        """
        obj = super(Method, cls).__new__(cls)
        obj.name = name
        obj.data = None
        return obj

    def __init__(self, method):
        self.loadmethods()

        method = method.upper()
        self.name = method
        self.RKtype = self.data[method]['type']
        self.RKa = np.array(self.data[method]['a'], dtype=np.float64)
        self.RKb = np.array(self.data[method]['b'], dtype=np.float64)
        self.RKbhat = np.array(self.data[method]['bhat'], dtype=np.float64)
        self.RKc = np.array(self.data[method]['c'], dtype=np.float64)
        self.RKord = int(self.data[method]['order'])
        self.RKns = int(self.data[method]['n'])

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
        Kj = [np.zeros(y.data.shape)]*self.method.RKns
        Yr = [copy.copy(y) for _ in range(self.method.RKns)]
        if self.method.RKtype == 'explicit':
            Kj[0] = vf(t0, y.data)
            for ii in range(self.method.RKns - 1):
                U = sum([elem*dt*coeff for elem, coeff in zip(Kj[:ii+1], self.method.RKa[ii+1, :ii+1])])
                Yr[ii+1].left(U, self.coordinate)
                K = vf(t0 + dt*self.method.RKc[ii+1], Yr[ii+1])
                Kj[ii+1] = K

        else:
            raise NotImplementedError

        Ulow = sum([Kval*dt*coeff for Kval, coeff in zip(Kj, self.method.RKb)])
        ylow = copy.copy(y)
        ylow.left(Ulow, self.coordinate)
        errest = -1

        yhigh = None
        if self.variablestep:
            if sum(self.method.RKbhat) == 0:
                raise NotImplementedError(self.method.name + ' does not support variable stepsize.')

            Uhigh = sum([Kval*dt*coeff for Kval, coeff in zip(Kj, self.method.RKbhat)])
            yhigh = copy.copy(y)
            yhigh.left(Uhigh, self.coordinate)
            errest = np.linalg.norm(ylow.data - yhigh.data)

        return ylow, yhigh, errest
