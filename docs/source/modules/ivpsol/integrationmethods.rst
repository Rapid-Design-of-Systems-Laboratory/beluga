IVP Integration Methods
=======================

============  ======  ======  =============  ========  ===========
Key           Order   nevals  Variable Step  Type      Description
============  ======  ======  =============  ========  ===========
E1            1       1       No             Explicit  Explicit Euler
------------  ------  ------  -------------  --------  -----------
ME2           2       2       No             Explicit  Modified Euler
------------  ------  ------  -------------  --------  -----------
HEUN2         2       2       No             Explicit  Heun's 2nd order
------------  ------  ------  -------------  --------  -----------
ODE23         2       3       Yes            Explicit  MATLAB's ode23
------------  ------  ------  -------------  --------  -----------
MOAN25        2       3       No             Explicit  Moan's 2(5)
------------  ------  ------  -------------  --------  -----------
MOAN35        3       4       No             Explicit  Moan's 3(5)
------------  ------  ------  -------------  --------  -----------
RK4           4       4       No             Explicit  The Runge-Kutta order 4 method
------------  ------  ------  -------------  --------  -----------
RK45          4       6       Yes            Explicit  Runge-Kutta 4(5)
------------  ------  ------  -------------  --------  -----------
RKF34         3       5       Yes            Explicit  Fehlberg's 3(4)
------------  ------  ------  -------------  --------  -----------
RKF43         4       5       Yes            Explicit  Fehlberg's 4(3)
------------  ------  ------  -------------  --------  -----------
RKF45A        4       6       Yes            Explicit  Fehlberg's 4(5)(a)
------------  ------  ------  -------------  --------  -----------
RKF54A        5       6       Yes            Explicit  Fehlberg's 5(4)(a)
------------  ------  ------  -------------  --------  -----------
RKF45B        4       6       Yes            Explicit  Fehlberg's 4(5)(b)
------------  ------  ------  -------------  --------  -----------
RKF54B        5       6       Yes            Explicit  Fehlberg's 5(4)(b)
------------  ------  ------  -------------  --------  -----------
DOPRI45       4       7       Yes            Explicit  Dormand-Prince 4(5)
------------  ------  ------  -------------  --------  -----------
DOPRI54       5       7       Yes            Explicit  Dormand-Prince 5(4)
------------  ------  ------  -------------  --------  -----------
BUTCHER6      6       7       No             Explicit  Butcher's 6
------------  ------  ------  -------------  --------  -----------
RKF78         7       13      Yes            Explicit  Fehlberg's 7(8)
------------  ------  ------  -------------  --------  -----------
RKF87         8       13      Yes            Explicit  Fehlberg's 8(7)
------------  ------  ------  -------------  --------  -----------
DOPRI78       7       13      Yes            Explicit  Dormand-Prince 7(8)
------------  ------  ------  -------------  --------  -----------
DOPRI87       8       13      Yes            Explicit  Dormand-Prince 8(7)
------------  ------  ------  -------------  --------  -----------
IE1           1       1       No             Implicit  Implicit Euler
------------  ------  ------  -------------  --------  -----------
GL2           2       1       No             Implicit  Gauss-Legendre 2 (implicit midpoint)
------------  ------  ------  -------------  --------  -----------
GL4           4       2       No             Implicit  Gauss-Legendre 4
------------  ------  ------  -------------  --------  -----------
GL6           6       3       No             Implicit  Gauss-Legendre 6
------------  ------  ------  -------------  --------  -----------
TRAP2         2       2       No             Implicit  Trapezoidal rule
------------  ------  ------  -------------  --------  -----------
GL4S          4       2       No             Implicit  Time-symmetric Gauss-Legendre 4
------------  ------  ------  -------------  --------  -----------
GL6S          6       3       No             Implicit  Time-symmetric Gauss-Legendre 6
------------  ------  ------  -------------  --------  -----------
LOBATTOIIIA4  4       3       No             Implicit  Lobatto III A 4
------------  ------  ------  -------------  --------  -----------
LOBATTOIIIA6  6       4       No             Implicit  Lobatto III A 6
------------  ------  ------  -------------  --------  -----------
CG23          2       3       Yes            Explicit  Crouch-Grossman 2(3)
============  ======  ======  =============  ========  ===========
