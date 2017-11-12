import scipy.integrate
import numpy as np

def ode_wrap(func,*args):   # Required for odeint
    def func_wrapper(t,y):
        return func(y,t,*args)
    return func_wrapper

def ode45(f,tspan,y0,*args,**kwargs):
    """Implements interface similar to MATLAB's ode45 using scipy"""

    # return ode45_old(f,tspan,y0,*args,**kwargs)

    # if len(tspan) == 2:
    #     # TODO: Change hardcoding?
    #     tspan = np.linspace(tspan[0],tspan[1],200)
    # t0 = tspan[0]
    # t1 = tspan[1]
    # yy = scipy.integrate.odeint(ode_wrap(f,*args),y0,tspan)
    # return (tspan,yy)
    #
    if len(tspan) == 2:
        # TODO: Change hardcoding?
        tspan = np.linspace(tspan[0],tspan[1],100)
    ## Superfast option below
    abstol = kwargs.get('abstol', 1e-6)
    reltol = kwargs.get('reltol', 1e-2)
    # r = scipy.integrate.ode(f).set_integrator('vode', method='adams', atol=abstol, rtol=reltol, order=1)
    r = scipy.integrate.ode(f).set_integrator('dopri5', atol=abstol, rtol=reltol)
    r.set_initial_value(y0, tspan[0]).set_f_params(*args)
    y_out = np.zeros((len(tspan), len(y0)))

    y_out[0,:] = y0
    # ctr = 1
    for ctr, t in enumerate(tspan[1:],1):
        if not r.successful():
            break
        # dt = tspan[ctr] - tspan[ctr-1]
        dt = t - tspan[ctr-1]
        y_out[ctr, :] = r.integrate(r.t+dt)
        # ctr += 1
    if not r.successful():
        raise RuntimeError('Integration failed!')
    return tspan, y_out


# Source : http://www.sam.math.ethz.ch/~gradinar/Teaching/NumPhys/SomeTemplates/ode45.py
from numpy import double, sign, finfo, array, zeros, dot, mod, size, inf, all, max, min, abs, mat
from numpy.linalg import norm
import logging

def warning(type, string):
    logging.warning('warning: ' + type)
    logging.warning(string)

def error(type, string):
    logging.error('error: ' + type)
    logging.error(string)
    raise RuntimeError(string)  # Raise error to notify shooting solver
    # exit

# specify default arguments here:


def processOdeArgs(**kwargs):
    defaults = {'normcontrol': 'on',  # ('on','off')
                # index array describing components that should be nonnegative
                'nonnegative': None,
                # relative tolerance (can be array of same dimension as y0)
                'reltol': 1e-5,
                'abstol': 1e-5,			# absolute tolerance
                'outputsel': None,		# which components to save
                # save output every outputsave steps
                'outputsave': None,
                'initialstep': None,
                'maxstep': None,
                'mass': None,
                'stats': 'off'			# statistics
                }

    if len(kwargs) > 0:
        for i in kwargs:
            defaults[i.lower()] = kwargs[i]

    # accept True instead of 'on' for certain options
    opts = ['stats', 'normcontrol']
    for o in opts:
        if defaults[o] == True:
            defaults[o] = 'on'

    return defaults

def ode45_old(vfun, vslot, vinit, *args, **kwargs):
    # test input types etc

    # process keyword arguments
    vodeoptions = processOdeArgs(**kwargs)

    # ensure vslot and vinit are row vectors
    vslot = array(vslot, ndmin=1)
    vinit = array(vinit, ndmin=1)

    # stepsize fixed if more than 2 values in vslot
    if len(vslot) > 2:
        vstepsizefixed = True
    else:
        vstepsizefixed = False

    # reltol: relative tolerance
    if vodeoptions['reltol'] == None and not vstepsizefixed:
        vodeoptions['reltol'] = 1e-6
#		warning ('OdePkg:InvalidArgument', 'Option "reltol" not set, new value %f is used'%vodeoptions['reltol'])
    elif vodeoptions['reltol'] != None and vstepsizefixed:
        warning('OdePkg:InvalidArgument',
                'Option "reltol" will be ignored if fixed time stamps are given')

    # abstol: absolute tolerance. vector: tolerance for each component
    if vodeoptions['abstol'] == None and not vstepsizefixed:
        vodeoptions['abstol'] = 1e-6
#		warning('OdePkg:InvalidArgument', 'Option "abstol" not set, new value %f is used'%vodeoptions['abstol'])
    elif vodeoptions['abstol'] != None and vstepsizefixed:
        warning('OdePkg:InvalidArgument',
                'Option "abstol" will be ignored if fixed time stamps are given')

    # normcontrol:
    if vodeoptions['normcontrol'] == 'on':
        vnormcontrol = True
    else:
        vnormcontrol = False

    # nonnegative: indices that should be nonnegative
    if vodeoptions['nonnegative'] != None:
        if vodeoptions['mass'] == None:
            vhavenonnegative = True
        else:
            vhavenonnegative = False
            warning('OdePkg:InvalidArgument',
                    'Option "nonnegative" will be ignored if mass matrix is set')
    else:
        vhavenonnegative = False

    # outputsel: which indices to output
    if vodeoptions['outputsel'] != None:
        vhaveoutputselection = True
    else:
        vhaveoutputselection = False

    # outputsave: save solution every * steps
    if vodeoptions['outputsave'] == None:
        vodeoptions['outputsave'] = 1

    # initialstep
    if vodeoptions['initialstep'] == None and not vstepsizefixed:
        vodeoptions['initialstep'] = double(vslot[1] - vslot[0]) / 100
#		warning('OdePkg:InvalidArgument', 'Option "initialstep" not set, new value %f is used'%vodeoptions['initialstep'])

    # maxstep
    if vodeoptions['maxstep'] == None and not vstepsizefixed:
        vodeoptions['maxstep'] = double(vslot[1] - vslot[0]) / 10
#		warning ('OdePkg:InvalidArgument', 'Option "maxstep" not set, new value %f is used'%vodeoptions['maxstep'])

    # mass
    vhavemasshandle = False
    if vodeoptions['mass'].__class__.__name__ == 'ndarray':
        vmass = vodeoptions['mass']  # constant mass
    elif vodeoptions['mass'].__class__.__name__ == 'function':
        vhavemasshandle = True  # mass defined by a function handle

    # Starting the initialization of the core solver ode45
    vtimestamp = vslot[0]			# timestamp = start time
    vtimelength = len(vslot)		# length needed if fixed steps
    vtimestop = vslot[-1]			# stop time = last value
    vdirection = sign(vtimestop)  # Flag for direction to solve

    eps = finfo(double).eps
    # TODO: eps hardcoded in ode45
    # eps = 1e-16
    if not vstepsizefixed:
        vstepsize = vodeoptions['initialstep']
        vminstepsize = double(vtimestop - vtimestamp) / (1. / eps)
    else:  # If step size is given then use the fixed time steps
        vstepsize = vslot[1] - vslot[0]
        vminstepsize = sign(vstepsize) * eps

    vretvaltime = [vtimestamp]		# first timestamp output
    vretvalresult = [vinit.copy()]  # first solution output

    # 20071016, reported by Luis Randez
    # The Runge-Kutta-Fehlberg 4(5) coefficients
    # Coefficients proved on 20060827
    # See p.91 in Ascher & Petzold
    vpow = 1. / 5
    va = array([
        [0, 0, 0, 0, 0],
        [1. / 4, 0, 0, 0, 0],
        [3. / 32, 9. / 32, 0, 0, 0],
        [1932. / 2197, -7200. / 2197, 7296. / 2197, 0, 0],
        [439. / 216, -8, 3680. / 513, -845. / 4104, 0],
        [-8. / 27, 2, -3544. / 2565, 1859. / 4104, -11. / 40]])
    # 4th and 5th order b-coefficients
    vb4 = array([25. / 216, 0, 1408. / 2565, 2197. / 4104, -1. / 5, 0])
    vb5 = array(
        [16. / 135, 0, 6656. / 12825, 28561. / 56430, -9. / 50, 2. / 55])
    vc = sum(va, 1)

    # The solver main loop - stop if the endpoint has been reached
    vcntloop = 2
    vcntcycles = 1
    vu = vinit.copy()
    d = len(vinit)

    vk = zeros([6, d])

    vcntiter = 0
    while (vdirection * (vtimestamp) < vdirection * (vtimestop)) and (vdirection * (vstepsize) >= vdirection * (vminstepsize)):
        # Hit the endpoint of the time slot exactly
        if vtimestamp + vstepsize > vdirection * vtimestop:
            vstepsize = vtimestop - vdirection * vtimestamp

        # Estimate the six results using this solver
        vthetime = vtimestamp
        vtheinput = vu

        vk[0] = vfun(vthetime, vtheinput, *args)
        for j in range(1, 6):
            vthetime = vtimestamp + vc[j - 1] * vstepsize
            vtheinput = vu + vstepsize * dot(va[j][:j], vk[:j])
            vk[j] = vfun(vthetime, vtheinput, *args).T

        # Compute the 4th and the 5th order estimation
        y4 = vu + vstepsize * dot(vb4, vk)
        y5 = vu + vstepsize * dot(vb5, vk)
        # print 'vk:',vk
        # print 'y4:',y4,'y5:',y5
        if vhavenonnegative:
            vu[vodeoptions['nonnegative']] = abs(
                vu[vodeoptions['nonnegative']])
            y4[vodeoptions['nonnegative']] = abs(
                y4[vodeoptions['nonnegative']])
            y5[vodeoptions['nonnegative']] = abs(
                y5[vodeoptions['nonnegative']])
        vSaveVUForRefine = vu.copy()

        # Calculate the absolute local truncation error and the acceptable
        # error
        if not vstepsizefixed:
            if not vnormcontrol:
                vdelta = abs(y5 - y4)
                vtau = max(
                    vodeoptions['reltol'] * abs(vu), vodeoptions['abstol'])
                # print abs(vu)
            else:
                vdelta = norm(y5 - y4, inf)
                vtau = max(
                    [vodeoptions['reltol'] * max([norm(vu, inf), 1.0]), vodeoptions['abstol']])
                # print vtau
        else:  # if (vstepsizefixed == True)
            vdelta = 1
            vtau = 2

        # print 'tau:',vtau,'delta:',vdelta,'stepsize',vstepsize

        # If the error is acceptable then update the vretval variables
        if all(vdelta <= vtau):
            vtimestamp = vtimestamp + vstepsize
            vu = y5  # use higher order estimation as "local extrapolation"
            # Save the solution every vodeoptions['outputsave'] steps
            if mod(vcntloop - 1, vodeoptions['outputsave']) == 0:
                vretvaltime.append(vtimestamp)
                vretvalresult.append(vu)
            vcntloop = vcntloop + 1
            vcntiter = 0

        # Update the step size for the next integration step
        if not vstepsizefixed:
            # 20080425, reported by Marco Caliari
            # vdelta cannot be negative (because of the absolute value that
            # has been introduced) but it could be 0, then replace the zeros
            # with the maximum value of vdelta
            if size(vdelta) > 1:
                vdelta[vdelta == 0] = max(vdelta)
#			elif vdelta == 0:
#				vdelta = vtau * (0.4 ** (1. / vpow))
            # It could happen that max (vdelta) == 0 (ie. that the original
            # vdelta was 0), in that case we double the previous vstepsize
            if size(vdelta) > 1:
                vdelta[vdelta == 0] = max(vtau) * (0.4 ** (1. / vpow))

#			print 'vtau',vtau,'vdelta',vdelta

            if vdirection == 1:
                vstepsize = min(
                    [vodeoptions['maxstep'], min(0.8 * vstepsize * (vtau / vdelta) ** vpow)])
            else:
                vstepsize = max(
                    [vodeoptions['maxstep'], max(0.8 * vstepsize * (vtau / vdelta) ** vpow)])

        #	print 'stepsize:',vstepsize

        else:  # if (vstepsizefixed)
            if vcntloop <= vtimelength:
                # Quick fix
                if vcntloop == vtimelength:
                    vstepsize = vslot[vcntloop-1] - vslot[vcntloop - 2]
                else:
                    vstepsize = vslot[vcntloop] - vslot[vcntloop - 1]
            else:  # Get out of the main integration loop
                break

        # Update counters that count the number of iteration cycles
        vcntcycles = vcntcycles + 1		# Needed for cost statistics
        vcntiter = vcntiter + 1			# Needed to find iteration problems
        # Stop solving because in the last 1000 steps no successful valid value
        # has been found
        if (vcntiter >= 1000):
            error("fatal", "Solving has not been successful. The iterative integration loop exited at time t = %f before endpoint at tend = %f was reached. This happened because the iterative integration loop does not find a valid solution at this time stamp. Try to reduce the value of \"initialstep\" and/or \"maxstep\" with the command \"odeset\".\n" %
                  (vtimestamp, vtimestop))

    # Check if integration of the ode has been successful
    # print 'vdirection',vdirection
    # print 'vtimestamp',vtimestamp
    # print 'vtimestop',vtimestop
    # print 'vodeoptions[initialstep]',vodeoptions['initialstep']
    # print 'vminstepsize',vminstepsize
    # print 'maxstep',vodeoptions['initialstep']

    if vdirection * vtimestamp < vdirection * vtimestop:
        error('OdePkg:InvalidArgument', 'Solving has not been successful. The iterative integration loop exited at time t = %f before endpoint at tend = %f was reached. This may happen if the stepsize grows smaller than defined in vminstepsize. Try to reduce the value of "initialstep" and/or "maxstep" with the command "odeset".\n' %
              (vtimestamp, vtimestop))

    # Save the last step, if not already saved
    if mod(vcntloop - 2, vodeoptions['outputsave']) != 0:
        vretvaltime.append(vtimestamp)
        vretvalresult.append(vu)

    # Print additional information if option stats is set
    if vodeoptions['stats'] == 'on':
        vhavestats = True
        vnsteps = vcntloop - 2						# vcntloop from 2..end
        # vcntcycl from 1..end
        vnfailed = (vcntcycles - 1) - (vcntloop - 2) + 1
        vnfevals = 6 * (vcntcycles - 1)					# number of ode evaluations
        vndecomps = 0									# number of LU decompositions
        vnpds = 0									# number of partial derivatives
        vnlinsols = 0									# no. of solutions of linear systems
        # Print cost statistics if no output argument is given
        print('Number of successful steps %d' % vnsteps)
        print('Number of failed attempts:  %d' % vnfailed)
        print('Number of function calls:   %d' % vnfevals)
    else:
        vhavestats = False

    vretvaltime = array(vretvaltime)
    vretvalresult = array(vretvalresult)
    if vhaveoutputselection:
        vretvalresult = vretvalresult.transpose(
        )[vodeoptions['outputsel']].transpose()
    return (vretvaltime, vretvalresult)
