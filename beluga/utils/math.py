import math
import cmath

def exp(x):
    if isinstance(x,complex):
        return cmath.exp(x)
    else:
        return math.exp(x)

def log(x):
    if isinstance(x, complex):
        return cmath.log(x)
    else:
        return math.log(x)

def log10(x):
    if isinstance(x, complex):
        return cmath.log10(x)
    else:
        return math.log10(x)

def sqrt(x):
    if isinstance(x, complex) or x < 0:
        return cmath.sqrt(x)
    else:
        return math.sqrt(x)

def sin(x):
    if isinstance(x,complex):
        return cmath.sin(x)
    else:
        return math.sin(x)

def cos(x):
    if isinstance(x,complex):
        return cmath.cos(x)
    else:
        return math.cos(x)

def tan(x):
    if isinstance(x,complex):
        return cmath.tan(x)
    else:
        return math.tan(x)

def asin(x):
    if isinstance(x,complex) or x < -1 or x > 1:
        return cmath.asin(x)
    else:
        return math.asin(x)

def acos(x):
    if isinstance(x,complex) or x < -1 or x > 1:
        return cmath.acos(x)
    else:
        return math.acos(x)

def atan(x):
    if isinstance(x,complex):
        return cmath.atan(x)
    else:
        return math.atan(x)

def sinh(x):
    if isinstance(x,complex):
        return cmath.sin(x)
    else:
        return math.sin(x)

def cosh(x):
    if isinstance(x,complex):
        return cmath.cos(x)
    else:
        return math.cos(x)

def tanh(x):
    if isinstance(x,complex):
        return cmath.tan(x)
    else:
        return math.tan(x)

def asinh(x):
    if isinstance(x,complex):
        return cmath.asin(x)
    else:
        return math.asin(x)

def acosh(x):
    if isinstance(x,complex):
        return cmath.acos(x)
    else:
        return math.acos(x)

def atanh(x):
    if isinstance(x,complex):
        return cmath.atan(x)
    else:
        return math.atan(x)
