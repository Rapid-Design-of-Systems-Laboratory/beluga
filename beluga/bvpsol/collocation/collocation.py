import numpy as np

def midpoint(p0, p1, dp0, dp1, t0, t1):
    return (1 / 2 * (p0 + p1).T + (t1 - t0) / 8 * (dp0 - dp1).T).T

def midpoint_derivative(p0, p1, dp0, dp1, t0, t1):
    return (-3 / 2 * (p0 - p1).T / (t1-t0) - 1 / 4 * (dp0 + dp1).T).T

def integrate(fun, base, y, u, params, c, t, val0):
    val0 = np.array([val0])
    dX = np.squeeze([base(yi, ui, params, c) for yi, ui in zip(y, u)])
    if len(dX.shape) == 1:
        dX = np.array([dX]).T
    dp0 = dX[:-1]
    dp1 = dX[1:]
    p0 = y[:-1]
    p1 = y[1:]
    t0 = t[:-1]
    t1 = t[1:]
    u0 = u[:-1]
    uf = u[1:]
    u_midpoint = (u0 + uf) / 2
    y_midpoint = midpoint(p0, p1, dp0, dp1, t0, t1)
    for ii in range(len(t)-1):
        c0 = fun(y[ii], u[ii], params, c)
        c_mid = fun(y_midpoint[ii], u_midpoint[ii], params, c)
        c1 = fun(y[ii+1], u[ii+1], params, c)
        val0 = np.vstack((val0, val0[-1] + (1/6*c0 + 4/6*c_mid + 1/6*c1)*(t[ii+1] - t[ii])))

    return val0
