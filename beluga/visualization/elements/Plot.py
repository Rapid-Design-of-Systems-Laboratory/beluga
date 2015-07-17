class Plot(object):
    """
    Represents a single plot with axes, labels, expressions to evaluate etc.
    """
    def __init__(self, sol = 0, iteration = 0):
        self.sol_index = sol
        self.iter_index = iteration

    def xlabel(self, label):
        self.xlabel_str = label
        return self

    def ylabel(self, label):
        self.ylabel_str = label
        return self

    def x(self, expr):
        self.x_expr_str = expr
        return self

    def y(self, expr):
        self.y_expr_str = expr
        return self

    def render(self, problem_data, solutions):
        """
        Takes in problem and solution data and renders the plot using matplotlib
        """
        sol = solutions[self.sol_index][self.iter_index]
        variables  = [(state,max(abs(sol.y[idx,:])))
                        for idx,state in enumerate(self.problem_data['state_list'])]

        # Add auxiliary variables and their values (hopefully they dont clash)
        variables += [(var,bvp.aux_vars[aux['type']][var])
                        for aux in self.problem_data['aux_list']
                        for var in aux['vars']
                        if aux['type'] not in Scaling.excluded_aux]
        pass
