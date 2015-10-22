import sympy
__ignored_sym_func = ['rad', 're']
__ignored_sym = dict((sym, sympy.Symbol(sym)) for sym in __ignored_sym_func)


def sympify2(expr, *args, **kwargs):
    """Allows using sympy on expressions with 'reserved' keywords"""
    return sympy.sympify(expr, locals=__ignored_sym, *args, **kwargs)
