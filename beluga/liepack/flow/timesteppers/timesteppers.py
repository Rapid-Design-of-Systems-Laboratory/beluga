import abc
import numpy as np
# from beluga.liepack.domain.liealgebras import LieAlgebra
import copy
import csv
import os

# The following math import statements appear to be unused, but they are required on import of the specific
# methods since an eval() is called
from math import sqrt

class Method(object):
    def __new__(cls, name):
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
    def __new__(cls, *args, **kwargs):
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


class RK(TimeStepper):
    def __call__(self, vf, y, t0, dt):
        Kj = [np.zeros(y.data.shape)]*self.method.RKns
        Yr = [copy.copy(y)]*self.method.RKns
        if self.method.RKtype == 'explicit':
            if vf.get_equationtype() == 'linear':
                for ii in range(self.method.RKns):
                    Kj[ii] = np.array(vf(t0 + self.method.RKc[ii]*dt, Yr[ii]), dtype=np.float64)
            else:
                for ii in range(self.method.RKns):
                    Yr[ii] = copy.copy(y)
                    for jj in range(ii):
                        Yr[ii].left(dt*self.method.RKa[ii,jj]*Kj[jj], self.coordinate)
                    Kj[ii] = np.array(vf(t0 + self.method.RKc[ii]*dt, Yr[ii]), dtype=np.float64)

        else:
            raise NotImplementedError

        ylow = copy.copy(y)

        for ii in range(self.method.RKns):
            ylow.left(dt*self.method.RKb[ii]*Kj[ii], self.coordinate)

        errest = -1

        yhigh = None
        if self.variablestep:
            yhigh = copy.copy(y)
            for ii in range(self.method.RKns):
                yhigh.left(dt*self.method.RKbhat[ii]*Kj[ii], self.coordinate)

            raise NotImplementedError
            errest = dist(ylow, yhigh)

        return ylow, yhigh, errest



