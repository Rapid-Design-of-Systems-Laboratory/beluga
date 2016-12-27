#==============================================================================#
# Demonstrates the Heuristic Path Algorithm (HPA) for continiation.
# Author: Justin Mansell (2016)
#==============================================================================#
import numpy as np
import itertools
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation

#User defined parameters
"""These are the parameters that could expected to be supplied by the user.
   This implementation assumes that there are only two continuation variables
   but is made to generalize as easily as possible to any number of variables"""
w = 0.99 #Heuristic weighting (w=0: BFS, w=0.5: A*, w=1.0: DFS)
gridsteps = np.array([15, 15]) #Number of steps between the start and end coordinates for each variable
#NOTE: the start node will always be (0,0,...,0) and the goal node will alway be
#the gridsteps vector. However, the algorithm should not be consntrained to the
#resulting rectangular grid. It should be able to explore nodes anywhere if it
#needs to.

#Function and class definitions
"""Defines the node class and associated functions"""

class node:

    #Constructor function
    def __init__(self, ind, par = []):
        self.ind = ind #index coordinates of the node on the grid
        self.par = par #the node's parent (node object)
        self.g = 0
        self.h = 0
        self.f = 0
        self.conv = 1 #Whether or not this node converged

    #Function for printing a node object
    def __repr__(self):
        return repr((self.ind, self.f))

#Cost to move between nodes
def PathCost(ni, nf):
    """The incremental cost to go from node ni to an adjacent node nf"""
    #ni, nf = node objects
    return 1.0 #Path cost is just the cardinality length between nodes for now

#Heuristic function
def Heuristic(n):
    """Expected cost to reach the goal node from node n"""
    #Cardinal length to reach goal, plus a small constribution of the actual
    #distance to favor more obvious choices in the case of a tie between f's.
    return max(abs(n.ind - goal.ind))+0.01*np.linalg.norm(n.ind-goal.ind)

def converge(n):
    """Function to represent non-converging areas of the continuation space"""
    centre1 = [9,10]
    centre2 = [6,2]
    centre3 = [2,12]
    r1 = 4
    r2 = 4
    r3 = 4
    if (n.ind[0]-centre1[0])**2 + (n.ind[1]-centre1[1])**2 < r1**2:
        return 0
    if (n.ind[0]-centre2[0])**2 + (n.ind[1]-centre2[1])**2 < r2**2:
        return 0
    if (n.ind[0]-centre3[0])**2 + (n.ind[1]-centre3[1])**2 < r3**2:
        return 0
    #if n.ind[0]>gridsteps[0] or n.ind[1]>gridsteps[1]:
    #    return 0
    else:
        return 1

#Heuristic path search
def HPA(open_list, closed_list):
    """Expands a node on the frontier according to the value function"""

    #Verify that we haven't already solved the problem
    if bool(goal.par)==True:# and goal.conv == 1:
        return open_list,closed_list

    open_list = sorted(open_list, key=lambda n: n.f, reverse=True)
    q = open_list.pop() #Node in open_list with the smallest f


    #Check the convergence of the 'q' sub-problem
    q.conv = converge(q)
    if q.conv == 0:
        closed_list.append(q)
        return open_list, closed_list

    #Check if q is the final problem
    if max(abs(q.ind - goal.ind)) == 0:
        print('Solved final problem!')
        goal.par = q.par
        closed_list.append(q)
        return open_list, closed_list

    #Generate successors
    successors = []
    for direction in delta:
        new_ind = q.ind + direction
        successors.append(node(new_ind,q))

    for successor in successors:
        skip = 0 #skip flag
        #if max(abs(successor.ind - goal.ind)) == 0:
        #    goal.par = q #Set goal's parent to q
        #    closed_list.append(q)
        #    print('Found goal!')
        #    return open_list, closed_list #Found the goal...we're done

        successor.g = q.g + PathCost(q,successor)
        successor.h = Heuristic(successor)
        if max(abs(successor.ind - goal.ind)) == 0:
            successor.f == -1 #Set value function to negative so it is always prefered
        else: successor.f = (1-w) * successor.g + w * successor.h #Value function

        for n in open_list: #Make sure node is not in the open list already
            if max(abs(n.ind - successor.ind)) == 0:# and n.f < successor.f:
                skip = 1
                break
        for n in closed_list: #Make sure node is not in the closed list already
            if max(abs(n.ind - successor.ind)) == 0:# and n.f < successor.f:
                skip = 1
                break

        #NOTE: In the 'if' statements above I have commented out the n.f < successor.f
        #parts because in continuation we don't really care about finding the shortest
        #continuation path. We want to avoid computing the same optimal control sub-
        #problem twice. The only reason we might compute the same sub-problem a second
        #time is if we find a better local minimum...but that is a problem for another
        #day.

        if skip == 1:
            continue #Check to see if we need to skip this successor
        else:
            open_list.append(successor)

    closed_list.append(q) #We have generated all successors, done with q

    return open_list, closed_list

#Initialization
start = node(gridsteps*0.0) #Starting node
goal = node(gridsteps) #Goal node
delta = list(itertools.product([-1,0,1],repeat=len(gridsteps))) #Generate possible directions
delta.remove(tuple([0]*len(gridsteps))) #Get rid of the 0 vector as a possible direction
open_list = [start]
closed_list = []


#STATIC PLOT
fig_static = plt.figure(1)
xpts = np.linspace(0,gridsteps[0],gridsteps[0]+1)
ypts = np.linspace(0,gridsteps[1],gridsteps[1]+1)
x_all = []
y_all = []
x_div = []
y_div = []
for x in xpts:
    for y in ypts:
        x_all.append(x)
        y_all.append(y)
        n = node([x,y])
        if converge(n) == 0:
            x_div.append(x)
            y_div.append(y)
plt.scatter(x_all, y_all,s=60,facecolors='none',edgecolors='k',marker='o')
plt.scatter(x_div, y_div,s=60,c='r',marker='x')

#while not goal.par:  #While the goal has no parent node
#    open_list, closed_list = HPA(open_list, closed_list) #Solve HPA search problem
#staticplot = plt.figure()
#ax = plt.axes(xlim=(-1,gridsteps[0]+1),ylim=(-1,gridsteps[1]+1))
#plt.scatter([n.ind[0] for n in closed_list],[n.ind[1] for n in closed_list],s=60,facecolors='none',edgecolors='k',marker='o') #All visited nodes
#plt.scatter([n.ind[0] for n in open_list],[n.ind[1] for n in open_list],s=60,facecolors='none',edgecolors='k',marker='o') #All candidate nodes
#plt.scatter([n.ind[0] for n in closed_list if n.conv==1],[n.ind[1] for n in closed_list if n.conv==1],s=60,c='b',marker='o') #All sub-problems that converged
#plt.scatter([n.ind[0] for n in closed_list if n.conv==0],[n.ind[1] for n in closed_list if n.conv==0],s=60,c='r',marker='x') #All sub-problems that diverged
#plt.scatter([start.ind[0],goal.ind[0]],[start.ind[1],goal.ind[1]],s=60,c='r',marker='s') #Start and end nodes_searched
#plt.show()

#Animation
fig = plt.figure(2)

def init():
    """Refreshes the plot and problem"""
    global open_list, closed_list, ax
    fig.clf()
    ax = plt.axes(xlim=(-5,gridsteps[0]+10),ylim=(-5,gridsteps[1]+10))
    plt.xlabel('Continuation Parameter 1')
    plt.ylabel('Continuation Parameter 2')
    plt.scatter([start.ind[0],goal.ind[0]],[start.ind[1],goal.ind[1]],s=60,c='r',marker='s') #Start and end nodes_searched
    open_list = [start]
    closed_list = []
    goal.par = []
    return

def animate(i):
    """Draws a single frame of the animation"""
    global open_list, closed_list, ax
    #ax = plt.axes(xlim=(-1,gridsteps[0]+1),ylim=(-1,gridsteps[1]+1))
    open_list, closed_list = HPA(open_list, closed_list)
    plt.scatter([n.ind[0] for n in [closed_list[-1]]],[n.ind[1] for n in [closed_list[-1]]],s=60,facecolors='none',edgecolors='k',marker='o') #All visited nodes
    plt.scatter([n.ind[0] for n in open_list],[n.ind[1] for n in open_list],s=60,facecolors='none',edgecolors='k',marker='o') #All candidate nodes
    plt.scatter([n.ind[0] for n in [closed_list[-1]] if n.conv==1],[n.ind[1] for n in [closed_list[-1]] if n.conv==1],s=60,c='b',marker='o') #All sub-problems that converged
    plt.scatter([n.ind[0] for n in [closed_list[-1]] if n.conv==0],[n.ind[1] for n in [closed_list[-1]] if n.conv==0],s=60,c='r',marker='x') #All sub-problems that diverged
    for n in [closed_list[-1]]:
        if bool(n.par)==False: continue
        a = n.par #ancestor
        ax.annotate('',xy=n.ind,xycoords='data',xytext=a.ind,textcoords='data',
                    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
    return

anim = animation.FuncAnimation(fig, animate, frames=50, init_func = init, interval=300, repeat=False)
#plt.show()
#quit()

#Save animated gif
anim.save('Search.gif', dpi=200, writer = 'imagemagick')
#plt.show()

#plt.scatter([n.ind[0] for n in closed_list],[n.ind[1] for n in closed_list],s=60,c='g',marker='o')
#plt.scatter([n.ind[0] for n in open_list],[n.ind[1] for n in open_list],s=60,facecolors='none',edgecolors='k',marker='o')
















#END
