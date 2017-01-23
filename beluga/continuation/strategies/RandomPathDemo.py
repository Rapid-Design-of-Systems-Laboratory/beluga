#==============================================================================#
# Computes a random walk path between two points
# Author: Justin Mansell (2016)
#==============================================================================#
import numpy as np
import random
import matplotlib.pyplot as plt

def RandomPath(Xi, Xf, minsteps, agg = 0.5):
    #Random Path generation routine.
    #INPUT: Xi = array of initial coordinates
    #       Xf = array of target coordinates
    #      agg = aggression parameter (0 < agg <= 1)
    # minsteps = minimum number of steps for the path
    #OUTPUT: X = array of step coordinates for each variable

    #-----------------------------Initialization-------------------------------#
    Xi = np.array(Xi)
    Xf = np.array(Xf)
    if len(Xi) != len(Xf): #Check that the number of variables match
        print('Error: number of input variables does not match the number of' \
        'output variables!')
        return float('NaN')
    if len(Xi) < 2:
        print('Error: need at least 2 variables!')
        return float('NaN')

    dl = np.linalg.norm(abs(Xf - Xi)/minsteps) #Compute nominal step length
    maxsteps = 1000 #Maximum number of steps
    alfa = (1 - agg) * np.pi/2.0 #Maximum angle from center line for step direction
    #--------------------------------------------------------------------------#

    #-----------------------------Generate Path--------------------------------#
    step = 0 #Step counter
    X = [Xi] #List of step coordinates
    while step < maxsteps:
        Xc = X[step] #Current location
        delX = Xf - Xc #Target vector
        if np.linalg.norm(delX) <= dl:
            X.append(Xf) #Within a step length of target. We're done.
            break

        ##Create list of angles defining the target vector
        cline = [] #List of angles to define delX vector
        if len(Xi) == 2:
            cline.append(np.arctan2(delX[1], delX[0]))
        else:
            print('Only works for 2 variables at the moment.')
            return float('NaN')

        #TODO: Generalize to any dimension
        #    for i in range(0, len(Xi)-1):
        #        delX2 = delX ** 2 #Squared components of delX
        #        if i == len(Xi) - 1: #Last angle
        #            cline.append(2*np.arctan(delX[-1]/(delX[-2] + \
        #            np.sqrt(delX2[-2]+delX2[-1]))) + np.pi/2)
        #        else: #Other angles
        #            cline.append(np.arccos(delX[i]/np.sqrt(sum(delX2[i:]))))

        ##Randomize each hyperspherical coordiante
        phi = []
        for theta in cline:
            phi.append(random.uniform(theta - alfa, theta + alfa))

        ##Compute the step
        dx = np.array([0.0] * len(Xi)) #Step length vector
        dx[0] = dl * np.cos(phi[0])
        dx[1] = dl * np.sin(phi[0])
        X.append(Xc + dx)

        #print(X)
        step = step + 1
    return X


#Create a path
apath = RandomPath([1.0, 0.5],[2.0, 2.0], 100, agg = 0.75)
ppath = RandomPath([1.0, 0.5],[2.0, 2.0], 100, agg = 0.05)
lpath = RandomPath([1.0, 0.5],[2.0, 2.0], 100, agg = 1.0)
xapath, yapath = zip(*apath)
xppath, yppath = zip(*ppath)
xlpath, ylpath = zip(*lpath)

#Plot the path
aplot, = plt.plot(xapath,yapath, 'r-')
pplot, = plt.plot(xppath,yppath, 'b-')
lplot, = plt.plot(xlpath,ylpath, 'k--')
plt.scatter([1.0, 2.0],[0.5, 2.0],c='r')
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title('Random Continuation Path')
plt.xlim([0.5,2.5])
plt.ylim([0.0,2.5])
plt.legend([pplot,aplot,lplot],['Passive','Aggressive','Linear'],loc='lower right')
plt.savefig('RandPath3.pdf')
plt.show()
