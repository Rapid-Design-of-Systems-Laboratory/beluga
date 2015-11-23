from mock import *
from beluga.utils import pythematica
from beluga.utils import sympify2

# Check for 'Mathematica cannot find a valid password.'
def test_mathematica_run():
    """"Tests the function that runs mathematica commands"""
    test_cases = (
        ('2+2','4\n'),
        ('Solve[x-5==0,x]','{{x -> 5}}\n')
    )
    for test_in,test_out in test_cases:
        out = pythematica.mathematica_run(test_in)
        assert out == test_out

def test_mathematica_solve():
    """"Tests the function that solves equations using mathematica"""
    fn = pythematica.mathematica_solve

    # Linear equation
    assert(fn(sympify2('a - 5'),sympify2('a')) == [{'a':5}])

    # # Linear system
    # expr = [sympify2('a + b - 5'),sympify2('a - b + 10')]
    # v = [sympify2('a'),sympify2('b')]
    # assert(fn(expr,v) == [{'a': -5/2, 'b': 15/2}])

    # No Solution
    expr = [sympify2('a + b - 5'),sympify2('a + b - 10')]
    v = [sympify2('a'),sympify2('b')]
    assert(fn(expr,v) == [])

    # # Quadratic
    # sol3 = [{'x': sympify2('1 - sqrt(2)*I')}, {'x': sympify2('1 + sqrt(2)*I')}]
    # assert(fn(sympify2('x^2 - 2*x + 3'),sympify2('x')) == sol3)

    # # Trigonometric function (from Brachistochrone problem)
    # expr = [sympify2('g*lamV*cos(theta) - lamX*v*sin(theta) - lamY*v*cos(theta)')]
    # soln = [{'theta': sympify2('-acos(-lamX*v/sqrt(g**2*lamV**2 - 2*g*lamV*lamY*v + v**2*(lamX**2 + lamY**2)))')},
    #         {'theta': sympify2('acos(-lamX*v/sqrt(g**2*lamV**2 - 2*g*lamV*lamY*v + v**2*(lamX**2 + lamY**2)))')},
    #         {'theta': sympify2('-acos(lamX*v/sqrt(g**2*lamV**2 - 2*g*lamV*lamY*v + v**2*(lamX**2 + lamY**2)))')},
    #         {'theta': sympify2('acos(lamX*v/sqrt(g**2*lamV**2 - 2*g*lamV*lamY*v + v**2*(lamX**2 + lamY**2)))')}]
    # assert(fn(expr,sympify2('theta')) == soln) # For some reason direct comparison works here

    # System of nonlinear equations from 3DOF problem
    expr = [sympify2('-0.7829*Aref*alfa*lamGAM*rho0*v*exp(-h/H)*sin(bank)/mass + 0.7829*Aref*alfa*lamPSI*rho0*v*exp(-h/H)*cos(bank)/(mass*cos(gam))'),
    sympify2('-1.6537*Aref*alfa*lamV*rho0*v**2*exp(-h/H)/mass + 0.7829*Aref*lamGAM*rho0*v*exp(-h/H)*cos(bank)/mass + 0.7829*Aref*lamPSI*rho0*v*exp(-h/H)*sin(bank)/(mass*cos(gam))')]
    v = [sympify2('alfa'),sympify2('bank')]
    expected_sol = [{'bank': sympify2('-1.0*acos(0.5*sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
            'alfa': sympify2('sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877) - 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('acos(0.5*sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877) - 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('-1.0*acos(-0.5*sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877) + 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('acos(-0.5*sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(-2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877) + 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('-1.0*acos(-0.5*sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877) - 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('acos(-0.5*sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877) - 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(-0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('-1.0*acos(0.5*sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877) + 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')},

        {'bank': sympify2('acos(0.5*sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0))'),
        'alfa': sympify2('sqrt(2.0*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 2.0)*(lamGAM**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) + 0.1183558081877) + 0.236711616375401*lamGAM**2*lamPSI**2*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0)*sec(gam)**2 + lamPSI**4*(0.1183558081877*sqrt(-4.0*lamGAM**2*lamPSI**2*sec(gam)**2/(lamGAM**4 + 2.0*lamGAM**2*lamPSI**2*sec(gam)**2 + lamPSI**4*sec(gam)**4) + 1.0) - 0.1183558081877)*sec(gam)**4)/(lamGAM*lamV*v*(lamGAM**2 - 1.0*lamPSI**2*sec(gam)**2))')}]
    sol = fn(expr,v)
    for s,e_s in zip(sol,expected_sol):
        for ctrl,expr in s.items():
            assert str(expr) == str(e_s[ctrl])


def test_mathematica_parse():
    """"Tests the function that solves equations using mathematica"""

    fn = pythematica.mathematica_parse
    assert(fn('ArcCos[a+b]')         == sympify2('acos(a+b)'))
    assert(fn('Sqrt[ArcSin[a+b*c]]') == sympify2('sqrt(asin(a+b*c))'))
    assert(fn('a+b^2+c*Sin[x]')      == sympify2('a+b^2+c*sin(x)'))


#[{alfa: 0.0, bank: -2.0*atan((lamPSI*tan(0.5*gam)**2 + lamPSI - sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2))/(lamGAM*tan(0.5*gam)**2 - lamGAM))}, {alfa: 0.0, bank: -2.0*atan((lamPSI*tan(0.5*gam)**2 + lamPSI + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2))/(lamGAM*tan(0.5*gam)**2 - lamGAM))}, {alfa: 0.473423232750801*lamGAM*cos(2.0*atan(-lamGAM*tan(0.5*gam)**2/(lamPSI*tan(0.5*gam)**2 + lamPSI) + lamGAM/(lamPSI*tan(0.5*gam)**2 + lamPSI) + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2)/(lamPSI*tan(0.5*gam)**2 + lamPSI)))/(lamV*v) - 0.473423232750801*lamPSI*sin(2.0*atan(-lamGAM*tan(0.5*gam)**2/(lamPSI*tan(0.5*gam)**2 + lamPSI) + lamGAM/(lamPSI*tan(0.5*gam)**2 + lamPSI) + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2)/(lamPSI*tan(0.5*gam)**2 + lamPSI)))/(lamV*v*cos(gam)), bank: 2.0*atan((lamGAM*tan(0.5*gam)**2 - lamGAM - sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2))/(lamPSI*tan(0.5*gam)**2 + lamPSI))}, {alfa: 0.473423232750801*lamGAM*cos(2.0*atan(lamGAM*tan(0.5*gam)**2/(lamPSI*tan(0.5*gam)**2 + lamPSI) - lamGAM/(lamPSI*tan(0.5*gam)**2 + lamPSI) + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2)/(lamPSI*tan(0.5*gam)**2 + lamPSI)))/(lamV*v) + 0.473423232750801*lamPSI*sin(2.0*atan(lamGAM*tan(0.5*gam)**2/(lamPSI*tan(0.5*gam)**2 + lamPSI) - lamGAM/(lamPSI*tan(0.5*gam)**2 + lamPSI) + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2)/(lamPSI*tan(0.5*gam)**2 + lamPSI)))/(lamV*v*cos(gam)), bank: 2.0*atan((lamGAM*tan(0.5*gam)**2 - lamGAM + sqrt(lamGAM**2*tan(0.5*gam)**4 - 2.0*lamGAM**2*tan(0.5*gam)**2 + lamGAM**2 + lamPSI**2*tan(0.5*gam)**4 + 2.0*lamPSI**2*tan(0.5*gam)**2 + lamPSI**2))/(lamPSI*tan(0.5*gam)**2 + lamPSI))}]
## Solution for 3DOF problem from Sympy
