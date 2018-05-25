from beluga.ivpsol import trajectory

class ivp(object):
    '''
    Object representing a formally constructed initial value problem.
    '''
    def __new__(cls):
        obj = super(ivp, cls).__new__(cls)
        obj.equations_of_motion = None
        obj.quadratures = None
        obj.boundary_conditions = None
        obj.sol = trajectory()
        return obj
