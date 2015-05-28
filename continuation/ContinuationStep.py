from .ContinuationVariable import ContinuationVariable
import numpy as np
class ContinuationStep(object):
    """Defines one continuation step in continuation set"""
    
    def __init__(self, num_cases = 1,vars=[], bvp=None):
        self.bvp = bvp
        self.num_cases = num_cases
        self.vars = {}  # dictionary of values
        self.ctr  = 0   # iteration counter
        
    def reset(self):
        self.ctr = 0
    
    def get_ctr(self):
        return self.ctr
        
    def set_bvp(self, bvp):
        self.bvp = bvp
        # Iterate through all types of variables
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                # Look for the variable name from continuation in the BVP
                if var_name not in bvp.aux_vars[var_type].keys():
                    raise ValueError('Variable '+var_name+' not found in boundary value problem')

                # Set current value of each continuation variable
                self.vars[var_type][var_name].value = bvp.aux_vars[var_type][var_name]
                # Calculate update steps for continuation process
                self.vars[var_type][var_name].steps = np.linspace(self.vars[var_type][var_name].value,
                                                                  self.vars[var_type][var_name].target,
                                                                  self.num_cases)
    
    def set(self, var_type,name,target):
        if var_type not in self.vars.keys():
            self.vars[var_type] = {}
        
        # Create continuation variable object
        self.vars[var_type][name] = ContinuationVariable(name,target)
        
    def terminal(self, name,target):
        self.set('terminal',name,target)
        
    def initial(self, name,target):
        self.set('initial',name,target)
    
    def const(self, name,target):
        self.set('const',name,target)
    
    def constraint(self, name,target):
        self.set('constraint',name,target)
        
    def next(self):
        if self.bvp is None:
            raise ValueError('No boundary value problem associated with this object')

        if self.ctr >= self.num_cases:
            raise StopIteration('No more iterations left')
            
        # Update auxiliary variables using previously calculated step sizes    
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                self.bvp.aux_vars[var_type][var_name] = self.vars[var_type][var_name].steps[self.ctr]

        self.ctr += 1
        return self.bvp

    def complete(self):
        return self.ctr >= self.num_cases
        
    def update_var(self):
        pass