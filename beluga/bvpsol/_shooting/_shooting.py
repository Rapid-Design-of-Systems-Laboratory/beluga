import numpy as np

EPS = np.finfo(float).eps

def estimate_fun_jac(fun, x, y, p, f0=None):
    """Estimate derivatives of an ODE system rhs with forward differences.

    Returns
    -------
    df_dy : ndarray, shape (n, n, m)
        Derivatives with respect to y. An element (i, j, q) corresponds to
        d f_i(x_q, y_q) / d (y_q)_j.
    df_dp : ndarray with shape (n, k, m) or None
        Derivatives with respect to p. An element (i, j, q) corresponds to
        d f_i(x_q, y_q, p) / d p_j. If `p` is empty, None is returned.
    """
    n = y.shape[0]
    if f0 is None:
        f0 = fun(x, y, p)

    nf = len(f0)

    dtype = y.dtype

    df_dy = np.empty((nf, n), dtype=dtype)
    h = EPS**0.5 * (1 + np.abs(y))
    for i in range(n):
        y_new = y.copy()
        y_new[i] += h[i]
        hi = y_new[i] - y[i]
        f_new = fun(x, y_new, p)
        df_dy[:, i] = (f_new - f0) / hi

    k = p.shape[0]
    if k == 0:
        df_dp = None
    else:
        df_dp = np.empty((nf, k), dtype=dtype)
        h = EPS**0.5 * (1 + np.abs(p))
        for i in range(k):
            p_new = p.copy()
            p_new[i] += h[i]
            hi = p_new[i] - p[i]
            f_new = fun(x, y, p_new)
            df_dp[:, i] = (f_new - f0) / hi

    return df_dy, df_dp


def estimate_bc_jac(bc, ya, qa, yb, qb, p, bc0=None):
    """Estimate derivatives of boundary conditions with forward differences.

    Returns
    -------
    dbc_dya : ndarray, shape (n + k, n)
        Derivatives with respect to ya. An element (i, j) corresponds to
        d bc_i / d ya_j.
    dbc_dyb : ndarray, shape (n + k, n)
        Derivatives with respect to yb. An element (i, j) corresponds to
        d bc_i / d yb_j.
    dbc_dp : ndarray with shape (n + k, k) or None
        Derivatives with respect to p. An element (i, j) corresponds to
        d bc_i / d p_j. If `p` is empty, None is returned.
    """
    n = ya.shape[0]
    nq = qa.shape[0]
    k = p.shape[0]

    if bc0 is None:
        bc0 = bc(ya, qa, yb, qb, p)

    dtype = ya.dtype

    dbc_dya = np.empty((n, n + nq + k), dtype=dtype)
    h = EPS**0.5 * (1 + np.abs(ya))
    for i in range(n):
        ya_new = ya.copy()
        ya_new[i] += h[i]
        hi = ya_new[i] - ya[i]
        bc_new = bc(ya_new, qa, yb, qb, p)
        dbc_dya[i] = (bc_new - bc0) / hi
    dbc_dya = dbc_dya.T

    dbc_dqa = np.empty((nq, n + nq + k), dtype=dtype)
    h = EPS**0.5 * (1 + np.abs(qa))
    for i in range(nq):
        qa_new = qa.copy()
        qb_new = qb.copy()
        qa_new[i] += h[i]
        qb_new[i] += h[i]
        bc_new = bc(ya, qa_new, yb, qb_new, p)
        dbc_dqa[i] = (bc_new - bc0) / hi
    dbc_dqa = dbc_dqa.T

    h = EPS**0.5 * (1 + np.abs(yb))
    dbc_dyb = np.empty((n, n + nq + k), dtype=dtype)
    for i in range(n):
        yb_new = yb.copy()
        yb_new[i] += h[i]
        hi = yb_new[i] - yb[i]
        bc_new = bc(ya, qa, yb_new, qb, p)
        dbc_dyb[i] = (bc_new - bc0) / hi
    dbc_dyb = dbc_dyb.T

    if k == 0:
        dbc_dp = None
    else:
        h = EPS**0.5 * (1 + np.abs(p))
        dbc_dp = np.empty((k, n + nq + k), dtype=dtype)
        for i in range(k):
            p_new = p.copy()
            p_new[i] += h[i]
            hi = p_new[i] - p[i]
            bc_new = bc(ya, qa, yb, qb, p_new)
            dbc_dp[i] = (bc_new - bc0) / hi
        dbc_dp = dbc_dp.T

    return dbc_dya, dbc_dyb, dbc_dp


def make_stmode(odefn, n, step_size=1e-6):
    xh = np.eye(n)*step_size

    def _stmode_fd(_xx, u, p, aux):
        """ Finite difference version of state transition matrix """
        k = p.size
        ff = np.empty((n, n + k))
        phi = _xx[n:].reshape((n, n + k))
        xx = _xx[0:n]  # Just states

        # Compute Jacobian matrix, F using finite difference
        fx = np.squeeze([odefn(xx, u, p, aux)])

        for i in range(n):
            fxh = odefn(xx + xh[i, :], u, p, aux)
            ff[:, i] = (fxh-fx) / step_size

        for i in range(k):
            p[i] += step_size
            fxh = odefn(xx, u, p, aux)
            ff[:, i + n] = (fxh - fx) / step_size
            p[i] -= step_size

        phi_dot = np.dot(np.vstack((ff, np.zeros((k, k + n)))),
                         np.vstack((phi, np.hstack((np.zeros((k, n)), np.eye(k))))))[:n, :]
        return np.hstack((fx, np.reshape(phi_dot, (n * (n + k)))))

    return _stmode_fd


def wrap_functions(fun, bc, fun_jac, bc_jac, aux, k, dtype):
    """Wrap functions for unified usage in the solver."""

    fun_jac_p, fun_jac_wrapped, bc_jac_wrapped = None, None, None

    if k == 0:
        def fun_p(x, y, _):
            return np.asarray(fun(x, y), dtype)

        def bc_wrapped(ya, qa, yb, qb, _):
            return np.asarray(bc(ya, qa, [], yb, qb, [], _, [], aux), dtype)

        if fun_jac is not None:
            def fun_jac_p(x, y, _):
                return np.asarray(fun_jac(x, y), dtype), None

        if bc_jac is not None:
            def bc_jac_wrapped(ya, yb, _):
                dbc_dya, dbc_dyb = bc_jac(ya, yb)
                return (np.asarray(dbc_dya, dtype),
                        np.asarray(dbc_dyb, dtype), None)
    else:
        def fun_p(x, y, p):
            return np.asarray(fun(x, y, p), dtype)

        def bc_wrapped(ya, qa, yb, qb, p):
            _p = p[:k]
            _ndp = p[k:]
            return np.asarray(bc(ya, qa, [], yb, qb, [], _p, _ndp, aux), dtype)

        if fun_jac is not None:
            def fun_jac_p(x, y, p):
                df_dy, df_dp = fun_jac(x, y, p)
                return np.asarray(df_dy, dtype), np.asarray(df_dp, dtype)

        if bc_jac is not None:
            def bc_jac_wrapped(ya, yb, p):
                dbc_dya, dbc_dyb, dbc_dp = bc_jac(ya, yb, p)
                return (np.asarray(dbc_dya, dtype), np.asarray(dbc_dyb, dtype),
                        np.asarray(dbc_dp, dtype))

    fun_wrapped = fun_p

    if fun_jac is not None:
        fun_jac_wrapped = fun_jac_p

    return fun_wrapped, bc_wrapped, fun_jac_wrapped, bc_jac_wrapped
