import numpy as np
class HPA_Variable(object):
    def __init__(self,name,target,Nnodes,spacing='linear',confined=False):
        self.name = name
        self.target = target
        self.spacing = spacing #spacing of the continuation parameter
        self.confined = confined #whether or not the search can venture beyond the limits of the grid
        self.nodes = Nnodes #number of nodes along this axis of the graph
        self.value = np.nan
        self.index = np.nan # Index of state in BVP, obsolete
        self.steps = []
