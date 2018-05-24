class ivp(object):
    '''
    Object representing a formally constructed initial value problem.
    '''
    def __new__(cls):
        obj = super(ivp, cls).__new__(cls)
        obj.equations_of_motion = None
        obj.quadratures = None
        obj.boundary_conditions = None
        obj.sol = sol()
        return obj


class sol(object):
    '''
    Object representing a curve on a manifold.
    '''
    def __new__(cls):
        obj = super(sol, cls).__new__(cls)
        obj.x = None
        obj.y = None
        obj.quads = None
        obj.params = None
        obj.consts = None
        return obj
