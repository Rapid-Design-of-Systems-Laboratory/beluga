#==============================================================================#
# Demonstrates the heurstically guided rapidly exploring random tree (hRRT)
# algorithm in the context of continuation.
# Author: Justin Mansell (2017)
#==============================================================================#
import numpy as np
import itertools
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rd
import copy

#Important Terms
#Coordinate Space: overlying layer where the hRRT takes place. Values from the
#actual continuation space are nondimensionalized and mapped to the coordinate
#space so that a coherent tree can be defined. Otherwise, the step size does
#not make sense because the units are different in each axis!
#Value Space: actual continuation space of the problem.

#Parameters
val_step_size = [1,0.5] #Step size in value space
step_spacing = ['linear','log']
init_vals = [0,5e-1] #Continuation parameter values before the continuation
target_vals = [15,4e-5] #Continuation parameter targets
val_lbs = [-5,1e-6] #Continuation parameter lower bounds
val_ubs = [25,1] #Continuation parameter upper bounds
prob_floor = 0.75 #Probability floor to ensure algorithm is not too biased against exploration
max_steps = 100 #Maximum number of continuation steps (included failed attempts)
goal_bias = 0.15
cor_step_size = 1 #Step size in coordinate space (should be 1)
#NOTE: lbs and ubs define the limits of the continuation (value) space

#Function and class definitions
"""Defines the node class and associated functions"""
class node:

    #Constructor function
    def __init__(self, cor, par = None):
        self.cor = np.array(cor) #coordinates of the node
        self.vals = np.array(cor2val(cor)) #continuation values of the node
        self.par = par #the node's parent (node object)
        self.g = 0 #distance traveled to this node
        self.h = None #value of the heuristic at this node
        self.m = None #quality factor of the node NOTE: kept here as a place-holder that may be useful later. In defual hRRT the quality factor of the nodes changes as new nodes are added
        self.conv = None #Whether or not this node converged
        #NOTE: in general the quality factor can be anything

    #Function for printing a node object
    def __repr__(self):
        return repr((self.cor, self.g))

    #How to determine if objects are equivalent
    def __eq__(self, other):
        return self.cor == other.cor #and self.vals == other.vals and self.conv = other.conv


def cor2val(cor):
    """Transform from coordinate space to value space"""
    val = []
    for i in range(0,len(val_lbs)):
        if step_spacing[i] == 'linear':
            val.append(cor[i]*val_step_size[i]+val_lbs[i])
        elif step_spacing[i] == 'log':
            val.append(val_lbs[i]*10**(cor[i]*val_step_size[i]))
        else:
            val.append(None)
    return val

def val2cor(val):
    """Transform from value space to coordinate space"""
    cor = []
    for i in range(0,len(val_lbs)):
        if step_spacing[i] == 'linear':
            cor.append((val[i]-val_lbs[i])/val_step_size[i])
        elif step_spacing[i] == 'log':
            cor.append(np.log10(val[i]/val_lbs[i])/val_step_size[i])
        else:
            cor.append(None)
    return cor

#Initialization
rd.seed()
init_cor = val2cor(init_vals)
target_cor = val2cor(target_vals)
cor_lbs = val2cor(val_lbs)
cor_ubs = val2cor(val_ubs)
init_node = node(init_cor)
init_node.conv = 1
target = node(target_cor)
T = [init_node]
fails = [] #List of failed nodes

#IDEA: want something like .terminal('x',[-5,25],0.5,15) ---> ('var',range,step_size,target)
#                          .const('eps',[1e-6,1],0.25,1e-4,spacing = 'log')
#If the spacing is log, then the step size is a power of 10

def Heuristic(n):
    """Estimated cost remaining to reach the goal"""
    return np.linalg.norm(n.cor-target.cor)

#TODO: introduce k-nearest approach by introducing 'k' argument
def nearest_neighbour(x, T):
    """Finds the nearest node in the tree to the state x"""
    distances = [np.linalg.norm(x-n.cor) for n in T]
    return T[distances.index(min(distances))]

def max_cost(T):
    """Finds the cost of the maximum cost node in the tree"""
    return max([n.g+Heuristic(n) for n in T])

def select_node(T):
    while True:
        if rd.random() < goal_bias: #Goal biasing
            x_rand = target.cor
        else:
            x_rand = [rd.uniform(cor_lbs[i],cor_ubs[i]) for i in range(0,len(val_lbs))]
        nearest = nearest_neighbour(x_rand, T)
        if np.linalg.norm(x_rand-nearest.cor) < cor_step_size: continue #Avoid cases where the tree sometimes grows back on itself due to x_rand being very close to nearest
        m = 1 - (nearest.g+Heuristic(nearest)-Heuristic(init_node))/(max_cost(T)-Heuristic(init_node)) #Note: non-admissible heuristic could lead to negative quality
        m = min(prob_floor,m)
        r = rd.random()
        if r < m: break
    print(nearest.g,nearest.g+Heuristic(nearest),max_cost(T),Heuristic(init_node),m)
    return x_rand,nearest

def fake_bvp(n):
    """Pretends to solve a bvp problem at the node n"""
    n.conv = 1
    return

def extend(T,x_rand,nearest):
    """Extends a new node from nearest in the direction of x_rand.
    Alternatively, if the nearest node is within a step length of the
    goal, x_rand is neglected and the step is made to the goal"""
    if np.linalg.norm(nearest.cor-target.cor) < cor_step_size: #TODO: search the entire tree to see if anything is in range of the goal
        target.par = copy.deepcopy(nearest)
        #print('ADJACENT TO TARGET')
        return target
    else:
        new_node = node(nearest.cor + cor_step_size*(x_rand-nearest.cor)/ \
                                  np.linalg.norm(x_rand-nearest.cor))
        new_node.par = copy.deepcopy(nearest)
        new_node.g = new_node.par.g + cor_step_size
        return new_node

def update_hRRT(T, fails):
    """Updates the hRRT tree by adding a new node"""
    x_rand,nearest = select_node(T) #Choose a node to extend
    candidate_node = extend(T,x_rand,nearest) #Extend a candidate node
    fake_bvp(candidate_node) #Attempt the candidate node
    if candidate_node.conv:
        return T+[candidate_node], fails
    else:
        return T, fails+[candidate_node]

#Grow the hRRT tree
for ii in range(0,max_steps):
    T, fails = update_hRRT(T, fails)
    if all(T[-1].cor == target.cor): #BUG: this is not going to work well. We aren't constrained to a grid so they will never be exactly equal
        print('Continuation completed in',ii,'steps')
        break
    elif ii==max_steps-1:
        print('Continuation could not complete within allotted steps')



#Plotting
x_pts = []
y_pts = []
for n in T:
    x_pts.append(n.cor[0])
    y_pts.append(n.cor[1])
ax = plt.axes(xlim=(cor_lbs[0],cor_ubs[0]),ylim=(cor_lbs[1],cor_ubs[1]))
plt.scatter(init_node.cor[0],init_node.cor[1],s=60,c='r',marker='o') #Plot initial node
plt.scatter(target.cor[0],target.cor[1],s=60,c='r',marker='o') #Plot goal node
plt.plot(x_pts,y_pts,'bo')
for n in T:
    if bool(n.par)==False: continue
    ax.annotate('',xy=n.cor,xycoords='data',xytext=n.par.cor,textcoords='data',
                arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
plt.show()

#print(init_node.cor)
#print(target.cor)
#print(init_node.cor-target.cor)
#print(np.linalg.norm(init_node.cor-target.cor))

#TODO: need to draw lines between ancestors, not just the list of points


#End
