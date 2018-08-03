import numpy as np

class LieGroup(object):
    def __new__(cls, *args, **kwargs):
        obj = super(LieGroup, cls).__new__(cls)
        if len(args) == 0:
            obj.field = 'R'
            obj.shape = None
            obj.data = None
        elif len(args) == 1 and isinstance(args[0], LieGroup):
            obj = args[0]
        elif len(args) == 1 and isinstance(args[0], int):
            obj.field = 'R'
            obj.shape = args[0]
            obj.data = None
        elif len(args) == 2:
            obj.field = 'R'
            obj.shape = args[0]
            obj.data = args[1]

        return obj

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = np.array(data, dtype=np.float64)

class lgso(LieGroup):
    pass

class lgrn(LieGroup):
    pass
