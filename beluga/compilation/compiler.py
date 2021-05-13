import sympy
from collections import OrderedDict
from typing import Hashable, Union

from .jit import jit_compile_func
from ..utils.helper_functions import tuplefy


class Compiler:
    def __init__(self):
        self.sym_locals = dict()
        self.func_locals = dict()

    def __repr__(self):
        return 'Compiler: Sym: ' + str(self.sym_locals) + ' Func: ' + str(self.func_locals)

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
    def lambdify(self, args, sym_func, additional_modules=None, complex_numbers=False):

        default_modules = ['numpy', 'math']
        if additional_modules is None:
            modules = [self.func_locals] + default_modules
        else:
            modules = [{**self.func_locals, **additional_modules}] + default_modules

        tup_func = tuplefy(sym_func)
        lam_func = sympy.lambdify(args, tup_func, modules)
        jit_func = jit_compile_func(lam_func, args, func_name=repr(sym_func), complex_numbers=complex_numbers)
        return jit_func


class CompilerManager:

    compiler_stack = OrderedDict()
    active_compiler = None

    @classmethod
    def set_compiler(cls, compiler: Union[Compiler, Hashable, None] = None) -> Compiler:
        if compiler is cls.active_compiler and compiler is not None:
            pass

        elif compiler in cls.compiler_stack.keys():
            cls.active_compiler = cls.compiler_stack[compiler]

        elif compiler in cls.compiler_stack.values():
            cls.active_compiler = compiler

        elif len(cls.compiler_stack) == 0:
            if isinstance(compiler, Compiler):
                cls.active_compiler = cls.add_compiler(compiler=compiler)
            else:
                cls.active_compiler = cls.add_compiler(compiler_id=compiler)

        else:
            cls.active_compiler = list(cls.compiler_stack.values())[-1]

        return cls.active_compiler

    @classmethod
    def add_compiler(cls, compiler_id: Union[Hashable, None] = None, compiler: Union[Compiler, None] = None)\
            -> Compiler:

        if compiler_id is None:
            compiler_id = cls._generate_unused_id()

        if compiler is None:
            compiler = Compiler()

        cls.compiler_stack[compiler_id] = compiler

        return compiler

    @classmethod
    def del_compiler(cls, compiler: Union[Compiler, Hashable, None] = None):
        current_compiler = cls.active_compiler

        if compiler in cls.compiler_stack.keys():
            compiler_to_delete = cls.compiler_stack[compiler]
            del cls.compiler_stack[compiler]

        elif compiler in cls.compiler_stack.values():
            compiler_to_delete = compiler
            for id_i, comp_i in cls.compiler_stack.items():
                if comp_i is compiler_to_delete:
                    del cls.compiler_stack[id_i]
        else:
            raise KeyError('Compiler {}  was not found'.format(compiler))

        if compiler_to_delete is current_compiler:
            cls.active_compiler = None

    @classmethod
    def _generate_unused_id(cls) -> int:
        keys = cls.compiler_stack.keys()
        for idx in range(len(keys) + 1):
            if idx not in keys:
                return idx

    @classmethod
    def _check_active_compiler(cls):
        if cls.active_compiler is None:
            cls.set_compiler()

    @classmethod
    def get_active_compiler(cls):
        return cls.active_compiler

    @classmethod
    def sympify(cls, expr):
        cls._check_active_compiler()
        return cls.active_compiler.sympify(expr)

    @classmethod
    def lambdify(cls, args, sym_func, additional_modules=None, complex_numbers=False):
        cls._check_active_compiler()
        return cls.active_compiler.lambdify(args, sym_func,
                                            additional_modules=additional_modules, complex_numbers=complex_numbers)

    @classmethod
    def add_symbolic_local(cls, name, local=None):
        return cls.active_compiler.add_symbolic_local(name, local=local)

    @classmethod
    def add_function_local(cls, name, function):
        return cls.active_compiler.add_function_local(name, function)


set_compiler = CompilerManager.set_compiler
get_active_compiler = CompilerManager.get_active_compiler
del_compiler = CompilerManager.del_compiler

sympify = CompilerManager.sympify
lambdify = CompilerManager.lambdify
add_symbolic_local = CompilerManager.add_symbolic_local
add_function_local = CompilerManager.add_function_local
