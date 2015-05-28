from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from utils.keyboard import keyboard
from optim import NecessaryConditions

# from string import *

# from optimalControlClasses import eom

# from classes.classes_necessary_conditions import AugmentedCost


def compute_necessary_conditions(problem):
    """Perform variational calculus calculations on optimal control problem."""
    
    # Initialize necessary conditions object
    nec_cond = NecessaryConditions()    
    
    ## Create costate list
    for i in range(len(problem.state)):
        nec_cond.costate.append(problem.state[i].make_costate())
    
    ## Initial point calculations
    # Build initial point augmented cost string by looping through constraints
    aug_cost_init = problem.cost['init'].expr
    ind = 0
    for i in range(len(problem.constraint)):
        if problem.constraint[i].type is 'init':
            ind += 1
            aug_cost_init += ' + ' + problem.constraint[i].make_aug_cost(ind)
    nec_cond.aug_cost['init'] = aug_cost_init
    
    # Compute initial costate conditions
    for i in range(len(problem.state)):
        nec_cond.bc.init.append(
            diff(parse_expr('-' + '(' + aug_cost_init + ')'),
            symbols(problem.state[i].state_var)))
    
    ## Terminal point calculations
    # Build terminal point augmented cost string by looping through constraints
    aug_cost_term = problem.cost['term'].expr
    ind = 0
    for i in range(len(problem.constraint)):
        if problem.constraint[i].type is 'term':
            ind += 1
            aug_cost_term += ' + ' + problem.constraint[i].make_aug_cost(ind)
    nec_cond.aug_cost['term'] = aug_cost_term
    
    # Compute terminal costate conditions
    for i in range(len(problem.state)):
        nec_cond.bc.term.append(diff(parse_expr(aug_cost_term),
            symbols(problem.state[i].state_var)))
    
    ## Unconstrained arc calculations
    # Construct Hamiltonian
    nec_cond.ham.free = problem.cost['path'].expr
    for i in range(len(problem.state)):
        nec_cond.ham.free += ' + ' + nec_cond.costate[i] + '*' + \
            problem.state[i].process_eqn
    
    # Compute costate process equations
    for i in range(len(problem.state)):
        nec_cond.ham.make_costate_rate(problem.state[i].state_var)
    
    # Compute unconstrained control partial
    for i in range(len(problem.control)):
        nec_cond.ham.make_ctrl_partial(problem.control[i].var)
    
    # Compute unconstrained control law (need to add singular arc and bang/bang smoothing, numerical solutions)
    for i in range(len(problem.control)):
        nec_cond.ham.make_ctrl(problem.control[i].var, i)
    
    # Determine order that controls should be computed
    
    
# 	% Determine control write order to function. Select expression with fewest control variables first.
# 	controlsInExpression = zeros(1,oc.num.controls);
# 	for ctrExpression = 1 : 1 : oc.num.controls
# 	for ctrControl = 1 : 1 : oc.num.controls
# 	
# 		if ~isempty(strfind(char(oc.control.unconstrained.expression{ctrExpression}(1)),char(oc.control.var(ctrControl))))
# 			controlsInExpression(ctrExpression) = controlsInExpression(ctrExpression) + 1;
# 		end
# 	
# 	end
# 	end
# 
# 	% Sort controls starting with those with fewest appearances in control equations
# 	[~,oc.control.unconstrained.writeOrder] = sort(controlsInExpression);
    
    return nec_cond

    
    