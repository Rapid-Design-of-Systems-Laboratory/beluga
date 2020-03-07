from beluga.codegen.local_compiler import LocalCompiler
import sympy

default_tol = 1e-4


class GenericVariable:
    def __init__(self, name: str, units: str, tol=default_tol):
        self.name = name
        self.sym = None
        self.units = units
        self.tol = tol
        self.sympified = False

    @staticmethod
    def check_local_compiler(local_compiler):
        pass

    def sympify(self, local_compiler: LocalCompiler = None):
        self.sym = sympy.Symbol(self.name)
        self.sympified = True

        if isinstance(local_compiler, LocalCompiler):
            local_compiler.add_symbolic_local(self.name, self.sym)
            return self
        elif local_compiler is None:
            return self
        else:
            raise TypeError('Local Compiler object must be of type LocalCompiler')


class State(GenericVariable):
    def __init__(self, name: str, eom: str, units: str, tol=default_tol):
        GenericVariable.__init__(self, name, units, tol=tol)
        self.eom = eom

    def sympify(self, local_compiler: LocalCompiler = None):
        GenericVariable.sympify(self, local_compiler=local_compiler)

        if isinstance(local_compiler, LocalCompiler):
            local_compiler.add_symbolic_local(self.name, self.sym)
            return self
        elif local_compiler is None:
            return self
        else:
            raise TypeError('Local Compiler object must be of type LocalCompiler')

