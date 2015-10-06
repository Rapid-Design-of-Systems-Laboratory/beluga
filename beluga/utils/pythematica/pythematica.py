## NOTE: ONLY WORKS ON MAC
import subprocess, re
from sympy import mathematica_code as mcode
from beluga.utils import sympify2
# Credits: http://sapiensgarou.blogspot.com.br/2012/06/how-to-run-mathematica-functions-on.html
def mathematica_run(command):
    """Call the shell script which in turn calls mathematica"""
    # Fix this path to use actual root path from config
    from beluga import Beluga

    script = Beluga.config['root']+'/beluga/utils/pythematica/runMath.sh'
    p = subprocess.Popen([script,command], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode('utf-8')

def mathematica_parse(expr):
    rules = (
        (r'(\w+)\[',lambda m: m.group(0).lower()),  # Convert all function calls to lowercase
        (r'\[','('),                  # Replace square brackets with parenthesis
        (r'\]',')'),                  # Replace square brackets with parenthesis
        (r'arc(\w+)','a\\1'),         # Replace inverse trig functions
    )
    for rule,replacement in rules:
        expr,n = re.subn(rule,replacement,expr)

    return sympify2(expr)

def mathematica_solve(expr,vars):
    if isinstance(expr,list):
        m_expr = mcode(['Exp[dummyfoobar]*('+mcode(e)+') == 0' for e in expr])
    else:
        m_expr = 'Exp[dummyfoobar]*('+mcode(expr)+') == 0'

    cmd = 'Quiet[Simplify[Solve[%s,%s]]]' % (m_expr,mcode(vars)) # Suppress warnings for now
    sol_str = mathematica_run(cmd).strip()
    # print(sol_str)
    if sol_str == '{}' or "Solve[" in sol_str:  # No solution found
        return []
    else:
        # Convert solution to  dictionary
        out = [dict([varsol.split(' -> ') for varsol in s.split(', ')])
                for s in sol_str[2:-2].split('}, {')]
        # Convert solution strings to sympy expressions
        out = [dict([(var,mathematica_parse(expr)) for (var,expr) in sol.items()]) for sol in out]
        # print(out)
        return out

if __name__ == '__main__':
    from beluga.utils import pythematica
    from sympy import sympify

    # print(pythematica.mathematica_subs('-ArcCos[-((lX*v)/Sqrt[g^2*lV^2 - 2*g*lV*lY*v + (lX^2 + lY^2)*v^2])]'))
    sol_str = '{{theta -> -ArcCos[-((lX*v)/Sqrt[g^2*lV^2 - 2*g*lV*lY*v + (lX^2 + lY^2)*v^2])]}, {theta -> ArcCos[-((lX*v)/Sqrt[g^2*lV^2 - 2*g*lV*lY*v + (lX^2 + lY^2)*v^2])]}, {theta -> -ArcCos[(lX*v)/Sqrt[g^2*lV^2 - 2*g*lV*lY*v + (lX^2 + lY^2)*v^2]]}, {theta -> ArcCos[(lX*v)/Sqrt[g^2*lV^2 - 2*g*lV*lY*v + (lX^2 + lY^2)*v^2]]}}'

    out = [dict([varsol.split(' -> ') for varsol in s.split(', ')])
        for s in sol_str[2:-2].split('}, {')]
    out = [dict([(var,sympify2(mathematica_parse(expr))) for (var,expr) in sol.items()]) for sol in out]
    print(out)

    # print(pythematica.mathematica_solve(sympify('a - 5'),sympify('a')))
    # expr = [sympify('a + b - 5'),sympify('a - b + 10')]
    # v = [sympify('a'),sympify('b')]
    # print(pythematica.mathematica_solve(expr,v))

    # Example with no solution
    # expr = [sympify('a + b - 5'),sympify('a + b - 10')]
    # v = [sympify('a'),sympify('b')]
    # print(pythematica.mathematica_solve(expr,v))

    # Quadratic
    # print(pythematica.mathematica_solve(sympify('x^2 - 2*x + 3'),sympify('x')))

    # Nonlinear equation
    # expr = [sympify2('g*lamV*cos(theta) - lamX*v*sin(theta) - lamY*v*cos(theta)')]
    # print(pythematica.mathematica_solve(expr,sympify('theta')))

    # Nonlinear system of equations
    # expr = [sympify2('-0.7829*Aref*alfa*lamGAM*rho0*v*exp(-h/H)*sin(bank)/mass + 0.7829*Aref*alfa*lamPSI*rho0*v*exp(-h/H)*cos(bank)/(mass*cos(gam))'),
    # sympify2('-1.6537*Aref*alfa*lamV*rho0*v**2*exp(-h/H)/mass + 0.7829*Aref*lamGAM*rho0*v*exp(-h/H)*cos(bank)/mass + 0.7829*Aref*lamPSI*rho0*v*exp(-h/H)*sin(bank)/(mass*cos(gam))')]
    # v = [sympify2('alfa'),sympify2('bank')]
    # print(pythematica.mathematica_solve(expr,v))
