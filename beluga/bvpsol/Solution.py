import numpy as np
class Solution(object):
    x = None
    y = None
    p = None
    nOdes = 0
    def __init__(self, x, y, parameters=None, aux=None):
        "x,y and parameters should be vectors"
        self.x = np.array(x)
        self.y = np.array(y)
        if parameters is not None:
            self.parameters = np.array(parameters)
        else:
            self.parameters = None
        self.nOdes = self.y.shape[0] # Number of rows of y = number of ODEs
        self.aux = aux
