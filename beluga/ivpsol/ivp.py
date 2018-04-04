class ivp(object):
    def __new__(cls):
        obj = super(ivp, cls).__new__(cls)
        obj.eoms = None
        obj.boundary_conditions = None
        obj.quadratures = None
        obj.sol = sol()
        obj.algorithm = None
        obj.path_cost = None
        obj.terminal_cost = None
        return obj


class sol(object):
    def __new__(cls):
        obj = super(sol, cls).__new__(cls)
        obj.x = None
        obj.y = None
        obj.quads = None
        obj.params = None
        obj.consts = None
        obj.iter = None
        obj.time = None
        obj.residual = None
        return obj
