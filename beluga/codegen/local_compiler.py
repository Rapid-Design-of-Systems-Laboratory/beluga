import sympy
from beluga.codegen.codegen import jit_compile_func, tuplefy


class LocalCompiler:
    def __init__(self):
        self.symbolic_locals = dict()
        self.function_locals = dict()

    def __repr__(self):
        return 'LocalCompiler:\n    Symbolic Locals: ' + str(self.symbolic_locals) \
               + '\n    Function Locals: ' + str(self.function_locals)

    def add_symbolic_local(self, name, local):
        if name in self.symbolic_locals.keys():
            raise UserWarning('{} is already defined'.format(name))
        self.symbolic_locals[name] = local
        return self.symbolic_locals

    def sympify(self, expr):
        return sympy.sympify(expr, locals=self.symbolic_locals)

    def add_function_module(self, name, function):
        self.function_locals[name] = function
        return self.function_locals

    # noinspection PyTypeChecker
    def lambdify(self, args, sym_func, additional_modules=None, array_inputs=True, complex_numbers=False):

        default_modules = ['numpy', 'math']
        if additional_modules is None:
            modules = [self.function_locals] + default_modules
        else:
            modules = [{**self.function_locals, **additional_modules}] + default_modules

        tup_func = tuplefy(sym_func)
        lam_func = sympy.lambdify(args, tup_func, modules)
        jit_func = jit_compile_func(lam_func, len(args), func_name=repr(sym_func),
                                    complex_numbers=complex_numbers, array_inputs=array_inputs)
        return jit_func
