import numpy as np
import numexpr as ne
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
        self.var_dict = None

    def prepare(self, problem_data):
        """
        Creates the dictionary required to evaluate expressions over the solution
        """
        #TODO: Write test for prepare()
        #TODO: Make state_list a part of the Solution object
        variables  = [(state,np.array(self.y[idx,:]))
                        for idx,state in enumerate(problem_data['state_list'])]
        # Add auxiliary variables and their values (hopefully they dont clash)
        variables += [(var,self.aux[aux['type']][var])
                        for aux in problem_data['aux_list']
                        for var in aux['vars']]
        self.var_dict = dict(variables)

    def evaluate(self,expr):
        """
        Evaluates an expressions involving the variables in this solution

        The caller is responsible for calling the prepare() method first
        """
        #TODO: Write test for evaluate()
        return ne.evaluate(expr,self.var_dict)
