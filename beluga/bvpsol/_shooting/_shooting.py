import numpy as np

EPS = np.finfo(float).eps

def estimate_bc_jac(bc, ya, yb, p, bc0=None):
    """Estimate derivatives of boundary conditions with forward differences.

    Returns
    -------
    dbc_dya : ndarray, shape (n + k, n)
        Derivatives with respect to ya. An element (i, j) corresponds to
        d bc_i / d ya_j.
    dbc_dyb : ndarray, shape (n + k, n)
        Derivatives with respect to yb. An element (i, j) corresponds to
        d bc_i / d ya_j.
    dbc_dp : ndarray with shape (n + k, k) or None
        Derivatives with respect to p. An element (i, j) corresponds to
        d bc_i / d p_j. If `p` is empty, None is returned.
    """
    n = ya.shape[0]
    k = p.shape[0]

    if bc0 is None:
        bc0 = bc(ya, yb, p)

    dtype = ya.dtype

    dbc_dya = np.empty((n, n + k), dtype=dtype)
    h = EPS**0.5 * (1 + np.abs(ya))
    for i in range(n):
        ya_new = ya.copy()
        ya_new[i] += h[i]
        hi = ya_new[i] - ya[i]
        bc_new = bc(ya_new, yb, p)
        dbc_dya[i] = (bc_new - bc0) / hi
    dbc_dya = dbc_dya.T

    h = EPS**0.5 * (1 + np.abs(yb))
    dbc_dyb = np.empty((n, n + k), dtype=dtype)
    for i in range(n):
        yb_new = yb.copy()
        yb_new[i] += h[i]
        hi = yb_new[i] - yb[i]
        bc_new = bc(ya, yb_new, p)
        dbc_dyb[i] = (bc_new - bc0) / hi
    dbc_dyb = dbc_dyb.T

    if k == 0:
        dbc_dp = None
    else:
        h = EPS**0.5 * (1 + np.abs(p))
        dbc_dp = np.empty((k, n + k), dtype=dtype)
        for i in range(k):
            p_new = p.copy()
            p_new[i] += h[i]
            hi = p_new[i] - p[i]
            bc_new = bc(ya, yb, p_new)
            dbc_dp[i] = (bc_new - bc0) / hi
        dbc_dp = dbc_dp.T

    return dbc_dya, dbc_dyb, dbc_dp