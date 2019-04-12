import numpy as np


class Flow(object):
    def __new__(cls, *args, **kwargs):
        """
        Creates a new Flow object.

        :param argument 1: Timestepper object
        :param argument 2: Vectorfield object
        :param kwargs: Additional parameters accepted by the solver.
        :return: Flow object.

        +------------------------+-----------------+-----------------+
        | Valid kwargs           | Default Value   | Valid Values    |
        +========================+=================+=================+
        | small                  | 0.5             |  > 0            |
        +------------------------+-----------------+-----------------+
        | large                  | 2.0             |  > 0            |
        +------------------------+-----------------+-----------------+
        | pessimist              | 0.5             |  > 0            |
        +------------------------+-----------------+-----------------+
        | accept                 | 1.2             |  > 0            |
        +------------------------+-----------------+-----------------+
        | tol                    | 1e-6            |  > 0            |
        +------------------------+-----------------+-----------------+
        | dt_max                 | 1.0             |  > 0            |
        +------------------------+-----------------+-----------------+
        | newexact               | 1               |  > 0            |
        +------------------------+-----------------+-----------------+
        | numstep                | 8               |  > 0            |
        +------------------------+-----------------+-----------------+
        | tstart                 | 0.0             |  float          |
        +------------------------+-----------------+-----------------+
        | tend                   | 1.0             |  float          |
        +------------------------+-----------------+-----------------+
        | stepsize               | 2.0             |  > 0            |
        +------------------------+-----------------+-----------------+
        | localss                | 10              |  > 0            |
        +------------------------+-----------------+-----------------+
        | globalss               | 10              |  > 0            |
        +------------------------+-----------------+-----------------+
        | disp                   | False           |  bool           |
        +------------------------+-----------------+-----------------+
        | variablestep           | False           |  bool           |
        +------------------------+-----------------+-----------------+
        """

        obj = super(Flow, cls).__new__(cls)

        obj.small = kwargs.get('small', 0.5)
        obj.large = kwargs.get('large', 2.0)
        obj.pessimist = kwargs.get('pessimist', 0.9)
        obj.accept = kwargs.get('accept', 1.2)
        obj.tol = kwargs.get('tol', 1e-6)
        obj.dt_max = kwargs.get('dt_max', 1.0)

        obj.newexact = kwargs.get('newexact', 1)
        obj.numstep = kwargs.get('numstep', 8)
        obj.tstart = kwargs.get('tstart', 0.0)
        obj.tend = kwargs.get('tend', 1.0)
        obj.stepsize = kwargs.get('stepsize', 2.0)
        obj.localss = kwargs.get('localss', 10)
        obj.globalss = kwargs.get('globalss', 10)
        obj.disp = kwargs.get('disp', False)

        obj.variablestep = kwargs.get('variablestep', False)

        if len(args) > 0:
            obj.timestepper = args[0]
        else:
            obj.timestepper = None

        if len(args) > 1:
            obj.vectorfield = args[1]
        else:
            obj.timestepper = None

        return obj

    def newstepsize(self, dt_old, errest):
        method = self.timestepper.method
        dt = self.pessimist * (self.tol / errest)**(1/(method.RKord+1))*dt_old
        dt = min((dt, self.large*dt_old))
        dt = max((dt, self.small*dt_old))
        dt_new = min(dt, self.dt_max)

        if (self.accept*self.tol - errest) > 0:
            accepted = True
        else:
            accepted = False

        return dt_new, accepted

    def __call__(self, y, t0, tf, dt):
        """
        :param y: states
        :param t0: initial time
        :param tf: final time
        :param dt: time step
        :return:
        """

        self.timestepper.variablestep = self.variablestep
        yi = [y]
        ti = np.zeros((1,))
        if t0 + dt > tf:
            dt = tf - t0

        accepted = False
        rejected = 0
        errest = 0
        n = 0
        converged = False
        while not converged:
            if ti[-1] + dt >= tf:
                dt = tf - ti[-1]
                converged = True

            while not accepted:
                ylow, yhigh, errest = self.timestepper(self.vectorfield, yi[-1], ti[-1], dt)

                if self.variablestep is True:
                    if errest == -1:
                        errest = np.linalg.norm(ylow.data - yhigh.data)

                    [dt_new, accepted] = self.newstepsize(dt, errest)
                else:
                    accepted = True
                    yhigh = ylow
                    dt_new = dt

                if not accepted:
                    dt = dt_new
                    rejected += 1

            ti = np.hstack((ti, ti[-1] + dt))
            yi.append(yhigh)
            accepted = False
            rejected = 0
            dt = dt_new

        return ti, yi
