import numpy as np
import numexpr as ne
class Solution(object):
    x = None
    y = None
    p = None
    nOdes = 0
    def __init__(self, x=None, y=None, parameters=None, aux=None, state_list=None):
        "x,y and parameters should be vectors"
        if x is not None and y is not None:
            self.x = np.array(x)
            self.y = np.array(y)
        else:
            self.x = self.y = None
        if parameters is not None:
            self.parameters = np.array(parameters)
        else:
            self.parameters = None
        # if y is not None:
        #     self.nOdes = self.y.shape[0] # Number of rows of y = number of ODEs
        # else:
        #     self.nOdes = 0

        self.aux = aux
        self.state_list = state_list
        self.var_dict = None

    def prepare(self, problem_data):
        """
        Creates the dictionary required to evaluate expressions over the solution
        """
        #TODO: Write test for prepare()
        #TODO: Make state_list a part of the Solution object

        variables = [(aux_name,aux_val)
                for aux_type in self.aux
                if isinstance(self.aux[aux_type],dict)
                for (aux_name,aux_val) in self.aux[aux_type].items()
                ]
        # Have to do in this order to override state values with arrays
        variables += [(state,np.array(self.y[idx,:]))
                        for idx,state in enumerate(problem_data['state_list'])]

        variables += [('t',self.x*self.y[-1,1])]
        self.var_dict = dict(variables)

    def evaluate(self,expr):
        """
        Evaluates an expressions involving the variables in this solution

        The caller is responsible for calling the prepare() method first
        """
        #TODO: Write test for evaluate()
        return ne.evaluate(expr,self.var_dict)
