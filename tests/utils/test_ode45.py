import numpy as np
from math import *
from beluga.utils import keyboard

def compute_hamiltonian(t,X,p,aux,u):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    g = aux['const']['g']

    thetta = u[0]
    return lamX*v*cos(thetta) + g*lamV*sin(thetta) + lamY*v*sin(thetta) + 1

def compute_control(t,X,p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = X[:7]
    g = aux['const']['g']

    thetta_saved = float('inf')
    ham_saved = float('inf')

    try:
        thetta = -acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta
    try:
        thetta = acos(-((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2)))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = -acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    try:
        thetta = acos((lamX*v)/sqrt(g**2*lamV**2+2*g*lamV*lamY*v+(lamX**2+lamY**2)*v**2))
    except:
        thetta = 0
    ham = compute_hamiltonian(t,X,p,aux,[thetta])
    if ham < ham_saved:
        ham_saved = ham
        thetta_saved = thetta

    if thetta_saved == float('inf'):
        thetta_saved = 0
    return thetta_saved

def brachisto_ode(t,_X,_p,aux):
    [x,y,v,lamX,lamY,lamV,tf] = _X[:7]
    g = aux['const']['g']

    thetta = compute_control(t,_X,_p,aux)
    xdot = tf*np.array([v*cos(thetta),
                     v*sin(thetta),
                     g*sin(thetta),
                     0,
                     0,
                     -(lamX*cos(thetta) + lamY*sin(thetta)),
                     0])
    return xdot


def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)
    if function.__name__ == 'test_ode45_1':
        pass

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)


inputs = [np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1]),
          [np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1]),np.array([0.0,0.0,1.0,-0.1,-0.1,-0.1,0.1])]
          ]
outputs = [[np.array([
    [ 0.00000000e+00,   0.00000000e+00,   1.00000000e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.00000000e-01, 1.00000000e-01],
   [  1.13886027e-04,  -9.98399029e-04,   1.00974679e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.00088022e-01,
      1.00000000e-01],
   [  1.37832157e-03,  -1.15071143e-02,   1.10714479e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.00961490e-01,
      1.00000000e-01],
   [  2.88581939e-03,  -2.29661995e-02,   1.20440725e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.01822599e-01,
      1.00000000e-01],
   [  4.65734809e-03,  -3.53700441e-02,   1.30152229e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.02671244e-01,
      1.00000000e-01],
   [  6.71374704e-03,  -4.87125747e-02,   1.39847800e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.03507321e-01,
      1.00000000e-01],
   [  9.07571608e-03,  -6.29872583e-02,   1.49526252e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.04330727e-01,
      1.00000000e-01],
   [  1.17638055e-02,  -7.81871057e-02,   1.59186401e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.05141362e-01,
      1.00000000e-01],
   [  1.47984057e-02,  -9.43046746e-02,   1.68827063e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.05939126e-01,
      1.00000000e-01],
   [  1.81997378e-02,  -1.11332073e-01,   1.78447059e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.06723923e-01,
      1.00000000e-01],
   [  2.19878431e-02,  -1.29260965e-01,   1.88045211e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.07495655e-01,
      1.00000000e-01],
   [  2.57442406e-02,  -1.46160497e-01,   1.96663900e+00,  -1.00000000e-01,  -1.00000000e-01,  -1.08178965e-01,
      1.00000000e-01]])]]

outputs.append([outputs[0][0],outputs[0][0]])
def test_ode45_1():
    from beluga.utils import ode45

    x0 = inputs[0]
    tspan = np.array([0, 1.0])
    aux = {'const':{'g':-9.81}}
    [t1,x1] = ode45(brachisto_ode,tspan,x0,[],aux)

    x1_expected = outputs[0]

    assert (x1 - x1_expected < 1e-5).all()

def test_ode45_multi_1():
    from beluga.utils import ode45_multi

    x0 = inputs[0]
    tspan = np.array([0, 1.0])
    aux = {'const':{'g':-9.81}}
    [t1,x1] = ode45_multi(brachisto_ode,tspan,x0,[],aux)
    x1 = list(x1)
    x1_expected  = outputs[0]
    assert all((a-b < 1e-5).all() for (a,b) in zip(x1,x1_expected))
    # assert (x1 - x1_expected < 1e-5).all()

def test_ode45_multi_2():
    from beluga.utils import ode45_multi

    x0 = inputs[1]

    tspan = [np.array([0, 1.0]),np.array([1.0, 2.0])]
    aux = {'const':{'g':-9.81}}
    [t1,x1] = ode45_multi(brachisto_ode,tspan,x0,[],aux)

    x1 = list(x1)   # Original output is a tuple for some reason
    x1_expected  = outputs[1]

    assert all((a-b < 1e-5).all() for (a,b) in zip(x1,x1_expected))

def test_split_tspan_1():
    assert True
