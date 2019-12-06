from beluga.utils.numerical_derivatives import gen_num_diff
from beluga.optimlib.special_functions import custom_functions
import sympy
import math


def f(x, y, z):
    return x ** 2 * math.exp(y) / z


df = gen_num_diff(f, order=(2, 2, 2), step_size=1e-6, method='c_diff')

func_dict = dict()

x, y, z = sympy.symbols('x, y, z')
fs = custom_functions.CustomFunction(f, [x, y, z], func_dict=func_dict)
df = fs.diff(x).diff(y).diff(z)

fg = custom_functions.CustomFunctionGenerator(f)

