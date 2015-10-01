import subprocess
from sympy import mathematica_code as mcode
# Credits: http://sapiensgarou.blogspot.com.br/2012/06/how-to-run-mathematica-functions-on.html
def mathematica_run(command):
    """Call the shell script which in turn calls mathematica"""
    # Fix this path to use actual root path from config
    from beluga import Beluga

    script = Beluga.config['root']+'/beluga/utils/py2matica/runMath.sh'
    p = subprocess.Popen([script,command], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

def mathematica_solve(expr,vars):
    if isinstance(expr,list):
        m_expr = mcode([mcode(e)+' == 0' for e in expr])
    else:
        m_expr = mcode(expr)+' == 0'

    cmd = 'Solve[%s,%s]' % (m_expr,mcode(vars))
    sol_str = mathematica_run(cmd).decode('utf-8').strip()
    out =  [dict([varsol.split(' -> ') for varsol in s.split(', ')])
                for s in sol_str[2:-2].split('}, {')]
    return out

if __name__ == '__main__':
    from beluga.utils import py2matica
    from sympy import sympify

    print(py2matica.mathematica_solve(sympify('a - 5'),sympify('a')))
    expr = [sympify('a + b - 5'),sympify('a - b + 10')]
    v = [sympify('a'),sympify('b')]
    print(py2matica.mathematica_solve(expr,v))
    print(py2matica.mathematica_solve(sympify('x^2 - 2*x + 3'),sympify('x')))
