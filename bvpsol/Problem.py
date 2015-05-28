
class Problem(object):
    """
    Defines a boundary value problem
    """
    def __init__(self, deriv_func, bc_func, states = [], const_names = [], constraint_names = [], initial_bc = [], terminal_bc = [], const = [], constraint = []):
        self.deriv_func  = deriv_func
        self.bc_func = bc_func

        self.aux_vars = {"initial": initial_bc, "terminal": terminal_bc, "const": const, "constraint":constraint, "states":states}
        # self.aux_var_names = {"states":states, "initial": states,"terminal": states, "const": const_names, "constraint":constraint_names}

    # Update BVP using continuation variable list
    def update(self, continuation_vars):
        for var_type in continuation_vars.keys():
            # for i in range(len(continuation_vars[var_type])):
            for var_name in continuation_vars[var_type].keys():
                # # Look for the variable name from continuation vars in the BVP
                # var_name = continuation_vars[key][i].name # Variable name
                # if var_name not in bvp.aux_var_names[key]:
                #     raise ValueError('Variable '+var_name+' not found in boundary value problem')
                #
                # # Set current value of each continuation variable
                # # from given BVP
                # index = bvp.aux_var_names[key].index(var_name)
                self.aux_vars[var_type][var_name] = continuation_vars[var_type][var_name].value
                # # Get saved index
                # index = continuation_vars[var_type][i].index
                # # Update BVP variable from given continuation step
                # self.aux_vars[var_type][index] = continuation_vars[var_type][i].value