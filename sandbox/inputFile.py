from problem import *

def inputs():
    """Brachistochrone example."""
    
    problem = Problem()
    
    # Define independent variables
    problem.indep_var = [Variable('t', 's')]
    
    # Define equations of motion
    problem.state = [State('t','x','v*cos(theta)','m'),
                     State('t','y','-v*sin(theta)','m'),
                     State('t','v','g*sin(theta)','m/s')]
    
    # Define controls
    problem.control = [Variable('theta','rad')]
    
    # Define costs
    problem.cost['path'] = Expression('1','s')
    
    # Define constraints
    problem.constraint = [Constraint('init','x-x0','m'),
                          Constraint('init','y-y0','m'),
                          Constraint('term','x-xf','m'),
                          Constraint('term','y-yf','m')]
    
    # Define constants
    problem.constant = [Value('g','9.81')]
    
    # Define quantity
    problem.quantity = [Value('tanAng','tan(theta)')]
    
    return problem