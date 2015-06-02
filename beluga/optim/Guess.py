from beluga.utils import ode45
class Guess(object):
    """Generates the initial guess from a variety of sources"""
    def __init__(self):
        pass

    @classmethod
    def fromfile(cls,filename):
        """Generates initial guess by loading an existing data file"""
        raise NotImplementedError("Method not implemented yet!")

    @classmethod
    def auto(cls,problem,x0,direction='forward',time_integrate=0.1):
        """Generates initial guess by forward/reverse integration"""

        # Add time of integration to states
        x0.append(time_integrate)
        # x1, y1 = ode45(SingleShooting.ode_wrap(deriv_func, paramGuess, aux), [x[0],x[-1]], y0g)
        # sol = Solution(x1,y1.T,paramGuess)

        pass
