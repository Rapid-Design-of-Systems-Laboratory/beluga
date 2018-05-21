#==============================================================================#
# Demonstrates the heurstically guided rapidly exploring random tree (hRRT)
# algorithm in the context of continuation.
# Author: Justin Mansell (2017)
#==============================================================================#
import numpy as np
import itertools
from math import *
import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
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
n_processors = 4 #Maximum number of bvp problems that can be solved at once
val_step_size = [1,0.5] #Step size in value space
step_spacing = ['linear','log']
init_vals = [0,5e-1] #Continuation parameter values before the continuation
target_vals = [15,4e-5] #Continuation parameter targets
val_lbs = [-5,1e-6] #Continuation parameter lower bounds
val_ubs = [25,1] #Continuation parameter upper bounds
prob_floor = 1 #Probability floor to ensure algorithm is not too biased against exploration
max_steps = 100 #Maximum number of continuation steps (included failed attempts)
goal_bias = 0.5 #Percentage chance of moving directly towards the goal
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
        self.closed = False #Is the node on a solved path to the goal?
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
T = [init_node] #Tree only consists of the starting node initally
fails = [] #List of failed nodes
obstacles = [] #List of obstacles to cover hard spots of design space

#IDEA: want something like .terminal('x',[-5,25],0.5,15) ---> ('var',range,step_size,target)
#                          .const('eps',[1e-6,1],0.25,1e-4,spacing = 'log')
#If the spacing is log, then the step size is a power of 10

def Heuristic(n):
    """Estimated cost remaining to reach the goal"""
    return np.linalg.norm(n.cor-target.cor)

#TODO: introduce k-nearest approach by introducing 'k' argument
def nearest_neighbour(x, T):
    """Finds the nearest node in the tree to the state x"""
    distance_sorted = sorted(T, key=lambda n: np.linalg.norm(x-n.cor)) #Sort the tree based on distances
    for n in distance_sorted: #Loop through list until a live node is encountered
        if n.closed == False:
            return n

    #Did not find any live nodes in the tree
    raise ValueError('Could not find any active (non-closed) nodes in the tree.')
    return None

def max_cost(T):
    """Finds the cost of the maximum cost node in the tree"""
    return max([n.g+Heuristic(n) for n in T])

def detect_collision(n):
    """Detects a collision with any generated obstacles"""
    #NOTE: Obstacles are assumed to be circles/spheres with radius cor_step_size
    #IDEA: Better shapes to use?
    return any([np.linalg.norm(n.cor-obs) < cor_step_size for obs in obstacles])

def backtrack(n, T):
    """Traces the ancestry of a node to its origin and closes all nodes along
    the way; preventing them from spawing further nodes"""
    n.closed = True
    while n.par is not None:
        distance_sorted = sorted(T, key=lambda p: np.linalg.norm(n.par.cor-p.cor))
        if np.linalg.norm(distance_sorted[0].cor - n.par.cor) > 0: print('Warning: parent coordinates inconsistent with tree, using closest instead')
        distance_sorted[0].closed = True
        n = distance_sorted[0]
    return

def select_node(T):
    while True:
        if rd.random() < goal_bias: #Goal biasing
            x_rand = target.cor
        else:
            x_rand = [rd.uniform(cor_lbs[i],cor_ubs[i]) for i in range(0,len(val_lbs))]
        nearest = nearest_neighbour(x_rand, T)
        if np.linalg.norm(x_rand-nearest.cor) < cor_step_size: continue #Avoid cases where the tree sometimes grows back on itself due to x_rand being very close to nearest
        if len(T) == 1:
            m = 1
        else:
            m = 1 - (nearest.g+Heuristic(nearest)-Heuristic(init_node))/(max_cost(T)-Heuristic(init_node)) #Note: non-admissible heuristic could lead to negative quality
        m = max(prob_floor,m) #Should be 'min' according to paper but that doesn't make any sense
        r = rd.random()
        if r < m: break
    #print(nearest.g,nearest.g+Heuristic(nearest),max_cost(T),Heuristic(init_node),m)
    return x_rand,nearest

def too_close(candidates,n):
    """Checks whether a new node is close to another node being added.
    This prevents the tree from adding redundant (too similar) nodes"""
    return any([np.linalg.norm(n.cor - cand.cor) < cor_step_size for cand in candidates])

def fake_bvp(n):
    """Pretends to solve a bvp problem at the node n"""
    if n.cor[0]<16 and n.cor[0]>10 and n.cor[1]<8 and n.cor[1]>4:
        n.conv=False
    else:
        n.conv = True
    return

def extend(T,x_rand,nearest):
    """Extends a new node from nearest in the direction of x_rand.
    Alternatively, if the nearest node is within a step length of the
    goal, x_rand is neglected and the step is made to the goal"""
    if np.linalg.norm(nearest.cor-target.cor) < cor_step_size: #TODO: search the whole tree
        #target.par = copy.deepcopy(nearest)
        new_node = node(target.cor)
        new_node.par = nearest
        new_node.g = new_node.par.g + np.linalg.norm(nearest.cor-target.cor)
        return new_node
    else:
        new_node = node(nearest.cor + cor_step_size*(x_rand-nearest.cor)/ \
                                  np.linalg.norm(x_rand-nearest.cor))
        new_node.par = nearest
        new_node.g = new_node.par.g + cor_step_size
        return new_node

def update_hRRT(T, fails):
    """Updates the hRRT tree by adding a new node"""
    candidates = []
    while len(candidates) < n_processors:
        x_rand,nearest = select_node(T) #Choose a node to extend
        candidate_node = extend(T,x_rand,nearest) #Extend a candidate node
        if too_close(candidates,candidate_node) == True and len(T) > n_processors: continue #Reject nodes that are close to other new nodes (only use once there are enough nodes in T!)
        if detect_collision(candidate_node) == False: candidates.append(candidate_node) #Check for collisions
    for candidate_node in candidates:
        print('Attempting node:',candidate_node.vals)
        fake_bvp(candidate_node) #Attempt the candidate nodes
        if candidate_node.conv:
            T = T+[candidate_node]
        else:
            obstacles.append(np.array(candidate_node.cor)) #"Here be dragons"
            fails = fails+[candidate_node]
    return T, fails

#Grow the hRRT tree
for ii in range(0,max_steps):
    T, fails = update_hRRT(T, fails)

    #TODO: WIP
    #for j,n in enumerate(T): #Inspect the tree for any solutions
    #    if all(n.cor == target.cor):
    #        print('Solution found in',ii,'steps')
    #        #Go back through the tree and remove the nodes that lead to the solution


    if any([all(n.cor == target.cor) for n in T]):
        print('Solution found in',ii,'steps')
        break
    elif ii==max_steps-1:
        print('Continuation could not complete within allotted steps')

#STATIC Plot
fig_static = plt.figure(1)
x_pts = []
y_pts = []
for n in T:
    x_pts.append(n.cor[0])
    y_pts.append(n.cor[1])
ax = plt.axes(xlim=(cor_lbs[0],cor_ubs[0]),ylim=(cor_lbs[1],cor_ubs[1]))
plt.scatter(init_node.cor[0],init_node.cor[1],s=60,c='r',marker='o') #Plot initial node
plt.scatter(target.cor[0],target.cor[1],s=60,c='r',marker='o') #Plot goal node
plt.plot(x_pts,y_pts,'bo')
#plt.scatter([n.cor[0] for n in fails],[n.cor[1] for n in fails],s=60,c='r',marker='x') #Plot fails
plt.scatter([n.cor[0] for n in fails],[n.cor[1] for n in fails],s=60,facecolors='none',edgecolors='k',marker='o') #Plot fails
circles = [plt.Circle(obs, 1, color='r',fill=False, hatch='//') for obs in obstacles]
for circle in circles: ax.add_artist(circle) #Plot obstacles
for n in T: #Plot arrows between closed nodes
    if bool(n.par)==False: continue
    ax.annotate('',xy=n.cor,xycoords='data',xytext=n.par.cor,textcoords='data',
                arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
#plt.show() #Uncomment to show static plot

#Animation
fig_anim = plt.figure(2)
def init():
    """Refreshes the plot and problem"""
    global T, fails, obstacles, ax1, successful_branches
    fig_anim.clf()
    plt.cla()
    ax1 = plt.axes(xlim=(cor_lbs[0],cor_ubs[0]),ylim=(cor_lbs[1],cor_ubs[1]))
    plt.xlabel('Continuation Parameter 1')
    plt.ylabel('Continuation Parameter 2')
    plt.scatter([init_node.cor[0],target.cor[0]],[init_node.cor[1],target.cor[1]],s=60,c='r',marker='s') #Start and end nodes_searched
    T = [init_node]
    target.par = None
    fails = []
    obstacles = []
    rd.seed()
    successful_branches = 0
    return

def animate(i):
    global goal_bias
    """Draws a single frame of the animation"""
    global T, fails, obstacles, ax1, successful_branches
    if successful_branches < n_processors:
        T, fails = update_hRRT(T, fails)
    else:
        print('Continuation process finished')

    for n in [t for t in T if all(t.cor == target.cor)]:
        goal_bias = 0.95 #Increase the goal bias to finish off the problem
        if n.closed == False:
            print('Closed a branch')
            backtrack(n, T)
            successful_branches += 1

    x_pts = []
    y_pts = []
    x_ptsc = [] #List of closed x pts
    y_ptsc = [] #List of closed y pts
    for n in T:
        if n.closed == True:
            x_ptsc.append(n.cor[0])
            y_ptsc.append(n.cor[1])
        else:
            x_pts.append(n.cor[0])
            y_pts.append(n.cor[1])
    plt.plot(x_pts,y_pts,'bo')
    plt.plot(x_ptsc,y_ptsc,'ro')
    plt.scatter([n.cor[0] for n in fails],[n.cor[1] for n in fails],s=60,facecolors='none',edgecolors='k',marker='o') #Plot fails
    circles = [plt.Circle(obs, 1, color='r',fill=False, hatch='//') for obs in obstacles]
    for circle in circles: ax1.add_artist(circle) #Plot obstacles
    for n in T: #Plot arrows between closed nodes
        if bool(n.par)==False: continue
        ax1.annotate('',xy=n.cor,xycoords='data',xytext=n.par.cor,textcoords='data',
                    arrowprops=dict(arrowstyle='->',connectionstyle='arc3'))
    return


anim = animation.FuncAnimation(fig_anim, animate, frames=50, init_func = init, interval=300, repeat=False)
anim.save('hRRTSearch.gif', dpi=200, writer = 'imagemagick')
#End


#PROBLEMS:
#--> Secondary branches do not grow towards the goal
