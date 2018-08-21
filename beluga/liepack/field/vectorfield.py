import numpy as np
from beluga.utils import keyboard
from beluga.liepack.domain.liealgebras import LieAlgebra
from beluga.liepack import group2algebra

class VectorField(object):
    """
    A VectorField class.

    :param args:
    :param kwargs:
    :return:

    +------------------------+-----------------+-------------------------+
    | Valid kwargs           | Default Value   | Valid Values            |
    +========================+=================+=========================+
    | evaltype               | 'M'             | {'M', 'vector'}         |
    +------------------------+-----------------+-------------------------+

    """
    def __new__(cls, *args, **kwargs):
        obj = super(VectorField, cls).__new__(cls)
        obj.evaltype = kwargs.get('evaltype', 'M')
        obj.domain = None
        obj.equationtype = 'general'
        obj.M2g = None

        if len(args) > 0:
            obj.domain = args[0]

        return obj

    def __call__(self, t, y):
        g = group2algebra(y.shape)
        algebra_shape = y.shape.shape

        if self.evaltype == 'M':
            return g(algebra_shape, np.array(self.M2g(t, y), dtype=np.float64))
        elif self.evaltype == 'vector':
            return np.array(self.M2g(t, y.get_vector()), dtype=np.float64)

    def get_domain(self):
        return self.domain

    def get_equationtype(self):
        return self.equationtype

    def get_M2g(self):
        return self.M2g

    def set_domain(self, domain):
        self.domain = domain

    def set_equationtype(self, equationtype):
        equationtype = equationtype.lower()
        if equationtype == 'l':
            equationtype = 'linear'
        elif equationtype == 'g':
            equationtype = 'general'

        if (equationtype != 'linear') and (equationtype != 'general'):
            raise NotImplementedError

        self.equationtype = equationtype

    def set_M2g(self, M2g):
        self.M2g = M2g
