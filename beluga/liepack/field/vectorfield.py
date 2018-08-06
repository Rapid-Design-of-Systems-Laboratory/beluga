import numpy as np

class VectorField(object):
    def __new__(cls, *args, **kwargs):
        obj = super(VectorField, cls).__new__(cls)
        obj.domain = None
        obj.equationtype = 'general'
        obj.fm2g = None

        if len(args) > 0:
            obj.domain = args[0]

        return obj

    def __call__(self, t, y):
        return np.array(self.fm2g(t, y), dtype=np.float64)

    def get_domain(self):
        return self.domain

    def get_equationtype(self):
        return self.equationtype

    def get_fm2g(self):
        return self.fm2g

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

    def set_fm2g(self, fm2g):
        self.fm2g = fm2g
