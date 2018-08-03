import abc
import numpy as np
# from beluga.liepack.domain.liealgebras import LieAlgebra
import copy

class Method(object):
    def __new__(cls, name):
        obj = super(Method, cls).__new__(cls)
        obj.name = name
        return obj

    def __init__(self, name):
        name = name.upper()
        # TODO: Move all these schemes to a csv file or some other data file
        if name == 'E1':
            self.name = name
            self.RKa = np.array([0])
            self.RKb = np.array([1])
            self.RKc = np.array([0])
            self.RKbhat = np.array([0])
            self.RKord = 1
            self.RKns = 1
            self.RKtype = 'explicit'
        elif name == 'RK4':
            self.name = name
            self.RKa = np.array([[0, 0, 0, 0], [1/2, 0, 0, 0], [0, 1/2, 0, 0], [0, 0, 1, 0]])
            self.RKb = np.array([1/6, 1/3, 1/3, 1/6])
            self.RKc = np.array([0, 1/2, 1/2, 1])
            self.RKbhat = np.array([0, 0, 0, 0])
            self.RKord = 4
            self.RKns = 4
            self.RKtype = 'explicit'


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
                    Kj[ii] = vf(t0 + self.method.RKc[ii]*dt, Yr[ii])
            else:
                for ii in range(self.method.RKns):
                    Yr[ii] = copy.copy(y)
                    for jj in range(ii):
                        Yr[ii].left(dt*self.method.RKa[ii,jj]*Kj[jj], self.coordinate)
                    Kj[ii] = vf(t0 + self.method.RKc[ii]*dt, Yr[ii])

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



