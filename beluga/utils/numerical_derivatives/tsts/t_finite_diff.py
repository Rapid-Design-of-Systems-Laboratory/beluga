from numba import njit, float64

from beluga.utils.numerical_derivatives.finite_diff import gen_fin_diff


@njit(float64(float64,))
def func0(x):
    return x**2 - x + 2


diff = gen_fin_diff(func0)
