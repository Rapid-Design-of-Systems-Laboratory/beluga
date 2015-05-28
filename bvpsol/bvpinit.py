from Solution import Solution
import numpy as np
def bvpinit(x,y,parameters=None):
    # If y is a function, evaluate y at all 'x' and return solution object
    x_val = np.array(x)
    if callable(y):
        y_val = np.array(map(y,x)).T
    else:
        y = np.array(y)
        if y.ndim == 1:
            # Convert to 2D array
            y = np.array([y]).T # Convert to column vector
            n = y.shape[0]      # Number of states
            y_val = np.tile(y,x_val.size) # Repeat across mesh
        elif y.shape[1] < x_val.size:
            raise ValueError("Number of columns in y should match number of elements in x")
        else:
            y_val = y
    
    return Solution(x_val,y_val,parameters)