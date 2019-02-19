import time
import sympy
import platform
from fractions import Fraction as R
from scipy.special import comb
import signal
import os
import sys
import shutil
import tempfile
import subprocess
import importlib
# import theano
from functools import partial
import warnings
import numpy as np
import sympy as sm

# https://stackoverflow.com/a/22348885/538379
if platform.system() == 'Windows':
    class timeout:
        def __init__(self, seconds=1, error_message='Timeout'):
            self.seconds = seconds
            self.error_message = error_message
        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_message)
        def __enter__(self):
            pass
        def __exit__(self, type, value, traceback):
            pass
else:
    class timeout:
        def __init__(self, seconds=1, error_message='Timeout'):
            self.seconds = seconds
            self.error_message = error_message
        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_message)
        def __enter__(self):
            signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(self.seconds)
        def __exit__(self, type, value, traceback):
            signal.alarm(0)

# Source: http://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python
_tstart_stack = []

def Bernoulli(num):
    B = [R(1,1)]
    def Sum(m):
        total = R(0,1)
        for k in range(0,m):
            total += int(comb(m, k, exact=False)) * R(B[k], m-k+1)
        return 1 - total
    m = 1
    while m <= num:
        B.append(Sum(m))
        m += 1
    return float(B[-1])

class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name,)
        print('Elapsed: %s' % (time.time() - self.tstart))

# Sympify that ignores some built in names
__ignored_sym_func = ['rad', 're']
__ignored_sym = dict((sym, sympy.Symbol(sym)) for sym in __ignored_sym_func)
def sympify(expr, *args, **kwargs):
    """Allows using sympy on expressions with 'reserved' keywords"""
    return sympy.sympify(expr, locals=__ignored_sym, *args, **kwargs)

# Source: http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
def static_var(varname, value):
    """Decorator that defines a static variable inside a function"""
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


def fix_carets(expr):
    """Converts carets to exponent symbol in string"""
    import re as _re
    caret = _re.compile('[\^]')
    return caret.sub('**',expr)

module_counter = 0

def openmp_installed():
    """Returns true if openmp is installed, false if not.
    Modified from:
    https://stackoverflow.com/questions/16549893/programatically-testing-for-openmp-support-from-a-python-setup-script
    """
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(tmpdir)

    filename = r'test.c'
    contents = r"""\
#include <omp.h>
#include <stdio.h>
int main() {
    #pragma omp parallel
    printf("Hello from thread %d, nthreads %d\n",
           omp_get_thread_num(), omp_get_num_threads());
}"""

    with open(filename, 'w') as f:
        f.write(contents)

    compiler = os.getenv('CC', 'cc')

    exit = 1
    try:
        with open(os.devnull, 'w') as fnull:
            exit = subprocess.call([compiler, '-fopenmp', filename],
                                   stdout=fnull, stderr=fnull)
    except:
        raise
    finally:  # cleanup even if compilation fails
        os.chdir(curdir)
        shutil.rmtree(tmpdir)

    return True if exit == 0 else False

_c_template = """\
#include <math.h>
#include "{file_prefix}_h.h"
void {routine_name}(double matrix[{matrix_output_size}], {input_args})
{{
{eval_code}
}}
"""

_h_template = """\
void {routine_name}(double matrix[{matrix_output_size}], {input_args});
"""

_cython_template = """\
import numpy as np
from cython.parallel import prange
cimport numpy as np
cimport cython
cdef extern from "{file_prefix}_h.h"{head_gil}:
    void {routine_name}(double matrix[{matrix_output_size}], {input_args})
@cython.boundscheck(False)
@cython.wraparound(False)
def {routine_name}_loop(np.ndarray[np.double_t, ndim=2] matrix, {numpy_typed_input_args}):
    cdef int n = matrix.shape[0]
    cdef int i
    for i in {loop_sig}:
        {routine_name}(&matrix[i, 0], {indexed_input_args})
    return matrix.reshape(n, {num_rows}, {num_cols})
"""

_setup_template = """\
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
extension = Extension(name="{file_prefix}",
                      sources=["{file_prefix}.pyx",
                               "{file_prefix}_c.c"],
                      extra_compile_args=[{compile_args}],
                      extra_link_args=[{link_args}],
                      include_dirs=[numpy.get_include()])
setup(name="{routine_name}",
      ext_modules=cythonize([extension]))
"""

def ufuncify_matrix(args, expr, const=None, tmp_dir=None, parallel=False):
    """Returns a function that evaluates a matrix of expressions in a tight
    loop.
    Parameters
    ----------
    args : iterable of sympy.Symbol
        A list of all symbols in expr in the desired order for the output
        function.
    expr : sympy.Matrix
        A matrix of expressions.
    const : tuple, optional
        This should include any of the symbols in args that should be
        constant with respect to the loop.
    tmp_dir : string, optional
        The path to a directory in which to store the generated files. If
        None then the files will be not be retained after the function is
        compiled.
    parallel : boolean, optional
        If True and openmp is installed, the generated code will be
        parallelized across threads. This is only useful when expr are
        extremely large.
    """

    # TODO : This is my first ever global variable in Python. It'd probably
    # be better if this was a class attribute of a Ufuncifier class. And I'm
    # not sure if this current version counts sequentially.
    global module_counter

    matrix_size = expr.shape[0] * expr.shape[1]

    file_prefix_base = 'ufuncify_matrix'
    file_prefix = '{}_{}'.format(file_prefix_base, module_counter)

    if tmp_dir is None:
        codedir = tempfile.mkdtemp(".ufuncify_compile")
    else:
        codedir = os.path.abspath(tmp_dir)

    if not os.path.exists(codedir):
        os.makedirs(codedir)

    taken = False
    while not taken:
        try:
            open(os.path.join(codedir, file_prefix + '.pyx'), 'r')
        except IOError:
            taken = True
        else:
            file_prefix = '{}_{}'.format(file_prefix_base, module_counter)
            module_counter += 1

    d = {'routine_name': 'eval_matrix',
         'file_prefix': file_prefix,
         'matrix_output_size': matrix_size,
         'num_rows': expr.shape[0],
         'num_cols': expr.shape[1]}

    if parallel:
        if openmp_installed():
            openmp = True
        else:
            openmp = False
            msg = ('openmp is not installed or not working properly, request '
                   'for parallel execution ignored.')
            warnings.warn(msg)

    if parallel and openmp:
        d['loop_sig'] = "prange(n, nogil=True)"
        d['head_gil'] = " nogil"
        d['compile_args'] = "'-fopenmp'"
        d['link_args'] = "'-fopenmp'"
    else:
        d['loop_sig'] = "range(n)"
        d['head_gil'] = ""
        d['compile_args'] = ""
        d['link_args'] = ""

    matrix_sym = sm.MatrixSymbol('matrix', expr.shape[0], expr.shape[1])

    sub_exprs, simple_mat = sm.cse(expr, sm.numbered_symbols('z_'))

    sub_expr_code = '\n'.join(['double ' + sm.ccode(sub_expr[1], sub_expr[0])
                               for sub_expr in sub_exprs])

    matrix_code = sm.ccode(simple_mat[0], matrix_sym)

    d['eval_code'] = '    ' + '\n    '.join((sub_expr_code + '\n' +
                                             matrix_code).split('\n'))

    c_indent = len('void {routine_name}('.format(**d))
    c_arg_spacer = ',\n' + ' ' * c_indent

    input_args = ['double {}'.format(sm.ccode(a)) for a in args]
    d['input_args'] = c_arg_spacer.join(input_args)

    cython_input_args = []
    indexed_input_args = []
    for a in args:
        if const is not None and a in const:
            typ = 'double'
            idexy = '{}'
        else:
            typ = 'np.ndarray[np.double_t, ndim=1]'
            idexy = '{}[i]'

        cython_input_args.append('{} {}'.format(typ, sm.ccode(a)))
        indexed_input_args.append(idexy.format(sm.ccode(a)))

    cython_indent = len('def {routine_name}_loop('.format(**d))
    cython_arg_spacer = ',\n' + ' ' * cython_indent

    d['numpy_typed_input_args'] = cython_arg_spacer.join(cython_input_args)

    d['indexed_input_args'] = ',\n'.join(indexed_input_args)

    files = {}
    files[d['file_prefix'] + '_c.c'] = _c_template.format(**d)
    files[d['file_prefix'] + '_h.h'] = _h_template.format(**d)
    files[d['file_prefix'] + '.pyx'] = _cython_template.format(**d)
    files[d['file_prefix'] + '_setup.py'] = _setup_template.format(**d)

    workingdir = os.getcwd()
    os.chdir(codedir)

    try:
        sys.path.append(codedir)
        for filename, code in files.items():
            with open(filename, 'w') as f:
                f.write(code)
        cmd = [sys.executable, d['file_prefix'] + '_setup.py', 'build_ext', '--inplace']
        subprocess.call(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        # subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cython_module = importlib.import_module(d['file_prefix'])
    finally:
        module_counter += 1
        sys.path.remove(codedir)
        os.chdir(workingdir)
        if tmp_dir is None:
            shutil.rmtree(codedir)

    return getattr(cython_module, d['routine_name'] + '_loop')
