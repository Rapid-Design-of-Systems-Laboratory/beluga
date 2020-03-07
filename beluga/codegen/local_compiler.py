import sympy
from beluga.codegen.codegen import jit_compile_func, tuplefy


class LocalCompiler:
    def __init__(self):
        self.sym_locals = dict()
        self.func_locals = dict()

    def __repr__(self):
        return 'LocalCompiler:\n\tSymbolic Locals: ' + str(self.sym_locals) \
               + '\n\tFunction Locals: ' + str(self.func_locals)

    def __deepcopy__(self, memodict=None):
        return self

    def add_symbolic_local(self, name, local=None):
        if local is None:
            local = sympy.Symbol(name)
        self.sym_locals[name] = local
        return self.sym_locals

    def sympify(self, expr):
        return sympy.sympify(expr, locals=self.sym_locals)

    def add_function_local(self, name, function):
        self.func_locals[name] = function
        return self.func_locals

    # noinspection PyTypeChecker
    def lambdify(self, args, sym_func, additional_modules=None, array_inputs=True, complex_numbers=False):

        default_modules = ['numpy', 'math']
        if additional_modules is None:
            modules = [self.func_locals] + default_modules
        else:
            modules = [{**self.func_locals, **additional_modules}] + default_modules

        tup_func = tuplefy(sym_func)
        lam_func = sympy.lambdify(args, tup_func, modules)
        jit_func = jit_compile_func(lam_func, len(args), func_name=repr(sym_func),
                                    complex_numbers=complex_numbers, array_inputs=array_inputs)
        return jit_func
