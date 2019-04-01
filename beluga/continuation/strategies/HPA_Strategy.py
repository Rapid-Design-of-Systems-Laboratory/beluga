#==============================================================================#
# Author: Justin Mansell (2016)
# Description: Continuation using a heuristic path algorithm (HPA).
#==============================================================================#
# from beluga.continuation.HPA_Variable import HPA_Variable
import numpy as np
import itertools
import logging
import copy

#Define a new class for nodes along the continuation path
class node:

    #Constructor function
    def __init__(self, ind, val, par = []):
        self.ind = ind #graph coordinates of the node
        self.par = par #the node's parent node
        self.val = val #values of the continuation variables at the node
        self.g = 0
        self.h = 0
        self.f = 0
        self.bvp = None #BVP object associated with this node

    #Function for printing a node object (for debugging only)
    def __repr__(self):
        return repr((self.ind, self.val, self.f))

class HPA_Strategy(object):
    """Defines one continuation step in continuation set"""
    # A unique short name to select this class
    name = 'HPA'

    def __init__(self, hweight=0.75, max_steps = 100, no_diag = False, vars=[], bvp=None):
        self.bvp = bvp
        self.hweight = hweight #Heuristic weight factor (f = (1-w)*g + w*h)
        self.max_steps = max_steps #Maximum number of continuation steps
        self._num_cases = max_steps
        self.confines = [] #List of confined options
        self.no_diag = no_diag #Allow diagonal moves?
        self.vars = {}  # dictionary of variables
        self.ctr  = 0   # iteration counter
        self.last_bvp = None
        self.last_node = None
        self.convars = [] #Ordered list of coninuation variables
        self.init_vals = [] #List of initial values for continuation variables
        self.target_vals = [] # "    target values  "      "    "       "
        self.graphdims = [] #Number of nodes along the axis of each cont. var.
        self.spacings = [] #Variable spacing (log or linear) for each cont. var.
        self.start_node = None
        self.goal_node = None
        self.goal_attempts = 0 #Number of attempts at solving the goal node
        self.moves = [] #List of possible move directions
        self.open_list = [] #List of frontier nodes
        self.closed_list = [] #List of attempted nodes

    def reset(self):
        """Resets the graph search"""
        self.ctr  = 0
        self.last_bvp = None
        self.last_node = None
        self.convars = []
        self.init_vals = []
        self.target_vals = []
        self.graphdims = []
        self.spacings = []
        self.start_node = None
        self.goal_node = None
        self.goal_attempts = 0
        self.moves = []
        self.open_list = []
        self.closed_list = []

    def clear(self):
        """Clears all the previously set continuation variables"""
        self.vars = {}
        self.reset()

    def set_bvp(self, bvp):
        self.bvp = bvp

        #Graph properites stored in lists to preserve order of the continuation vars.
        convars = [] #List of variable names for the continuation variables
        init_vals = [] #List of initial values for each continuation variable
        graphdims = [] #List of graph dimenions
        spacings = [] #List of parameter spacing for each dimension
        target_vals = [] #List of target values for each continuation variable
        #confined = [] #Which variables are confined to the grid

        # Initialize strategy parameters
        for var_type in self.vars.keys():
            for var_name in self.vars[var_type].keys():
                # Look for the variable name from continuation in the BVP
                if var_name not in bvp.solution.aux[var_type].keys():
                    raise ValueError('Variable '+var_name+' not found in boundary value problem')

                #Load continuation variable data
                self.convars.append(var_name)
                self.init_vals.append(bvp.solution.aux[var_type][var_name])
                self.graphdims.append(self.vars[var_type][var_name].nodes)
                self.spacings.append(self.vars[var_type][var_name].spacing)
                self.target_vals.append(self.vars[var_type][var_name].target)
                self.confines.append(self.vars[var_type][var_name].confined)

        self.start_node = node(np.zeros(len(self.graphdims)),self.init_vals)
        self.start_node.bvp = bvp #Initialize the bvp
        self.goal_node = node(self.graphdims-np.ones(len(self.graphdims)),self.target_vals) #Might be unnecessary
        self.open_list = []
        self.last_node = self.start_node

        #Warning
        if len(self.graphdims)<2: raise ValueError('HPA continuation not appropriate for continuation on a single variable. Use manual or bisection strategy instead.')

        #Generate the possible move direcitons
        moves = list(itertools.product([-1,0,1],repeat=len(self.graphdims))) #Generate possible directions
        moves.remove(tuple([0]*len(self.graphdims))) #Get rid of the 0 vector as a possible direction
        if self.no_diag is True: moves = [d for d in moves if not np.linalg.norm(d)>1] #Get rid of diagonal directions
        self.moves = moves

    def set(self, var_type,name,target,nodes,spacing='linear',confined=False):
        if var_type not in self.vars.keys():
            self.vars[var_type] = {}

        # Create continuation variable object
        self.vars[var_type][name] = HPA_Variable(name,target,nodes,spacing,confined)
        return self

    def terminal(self, name,target,nodes,spacing='linear',confined=False):
        self.set('terminal',name,target,nodes,spacing,confined)
        return self

    def initial(self, name,target,nodes,spacing='linear',confined=False):
        self.set('initial',name,target,nodes,spacing,confined)
        return self

    def const(self, name,target,nodes,spacing='linear',confined=False):
        self.set('const',name,target,nodes,spacing,confined)
        return self

    # def constraint(self, name,target):
    #     self.set('constraint',name,target)
    #     return self

    def __iter__(self):
        """Define class as being iterable"""
        return self

    def __next__(self):
        return self.next()

    #Basically a dummy function to make Beluga.py happy. We don't know what
    #the steps will be a-priori in graph search.
    def num_cases(self,num_cases=None, spacing='linear'):
        if num_cases is None:
            return self._num_cases
        else:
            if self.ctr > 0:
                raise RuntimeError('Cannot set num_cases during iteration')

            self._num_cases = num_cases
            self._spacing   = spacing
            return self

    #Cost to move between nodes
    def PathCost(self, ni, nf):
        """The incremental cost to go from one node to an adjacent node"""
        #ni, nf = node objects
        return 1.0 #Path cost is just the cardinality length between nodes

    #Heuristic function
    def Heuristic(self, n):
        """Expected cost to reach the goal node from node n"""
        #Cardinal length to reach goal, plus a small constribution of the actual
        #distance to favor more obvious choices in the case of a tie between nodes.
        return max(abs(n.ind - self.goal_node.ind))+ \
                                0.01*np.linalg.norm(n.ind-self.goal_node.ind)

    def ind2vals(self, ind):
        """"Converts a node index into values for the continuation variables"""
        vals = []
        for i,var in enumerate(self.convars):
            if self.spacings[i] == 'linear':
                vals.append((self.target_vals[i] - self.init_vals[i])* \
                                  ind[i]/(self.graphdims[i]-1) + self.init_vals[i])

            if self.spacings[i] == 'log':
                vals.append(self.init_vals[i]*(self.target_vals[i]/ \
                                self.init_vals[i])**(ind[i]/(self.graphdims[i]-1)))

        return vals

    def next(self, ignore_last_step = False):
        """Generator class to create BVPs for the continuation step iterations
        """

        if self.bvp is None:
            raise ValueError('No boundary value problem associated with this object')

        if max(abs(self.last_node.ind - self.goal_node.ind)) == 0 and self.last_node.bvp.solution.converged:
            raise StopIteration #Solved original problem!

        if self.ctr >= self.max_steps:
            raise ValueError('Exceeded maximum number of continuation steps')

        #Check convergence of last bvp
        if not ignore_last_step and self.last_bvp is not None \
            and not self.last_bvp.solution.converged and \
            max(abs(self.last_node.ind - self.goal_node.ind)) != 0:

            #NOTE:If the node we attempted was the goal node, we don't want to
            #add it to closed_list, otherwise HPA would never attempt it again.
            #We already popped the goal node off of open_list, so if we do nothing
            #HPA will explore a subproblem adjacent to the goal node. In doing so,
            #HPA will generate the goal node again as a successor, but this time
            #the goal node will have a different parent (and thus have a new chance)
            #at being solved.

            #Problem diverged, so we don't want to expand any successors from it
            self.closed_list.append(self.last_node)

        #Last problem converged or goal node was attempted but failed; generate new nodes
        else:
            if max(abs(self.last_node.ind - self.goal_node.ind)) != 0:
                self.closed_list.append(self.last_node) #Don't close the goal
            else: self.goal_attempts += 1 #Goal attempted but failed

            #Generate successors to last_node
            successors = []
            for direction in self.moves:
                new_ind = self.last_node.ind + direction
                new_vals = self.ind2vals(new_ind)
                successors.append(node(new_ind,new_vals,self.last_node))

            for successor in successors:
                skip = 0 #skip flag

                #Compute the value function of each successor
                successor.g = self.last_node.g + self.PathCost(self.last_node,successor)
                successor.h = self.Heuristic(successor)
                successor.f = (1-self.hweight)*successor.g + self.hweight*successor.h

                #Make sure node is not in open_list or closed_list already
                for n in self.open_list:
                    if max(abs(n.ind - successor.ind)) == 0:
                        skip = 1
                        break
                for n in self.closed_list:
                    if max(abs(n.ind - successor.ind)) == 0:
                        skip = 1
                        break

                #Make sure node is not outside of the grid, if this isn't allowed
                for ii,grid_confine in enumerate(self.confines):
                    if grid_confine == True:
                        if successor.ind[ii]>self.graphdims[ii]-1 or successor.ind[ii]<0: skip=1

                #Add successors to the frontier and assign bvp objects
                if skip == 1:
                    continue #Check to see if we need to skip this successor
                else:
                    #Assign a bvp object to each valid successor
                    successor.bvp = copy.deepcopy(successor.par.bvp)
                    for var_type in self.vars:
                        for var_name in self.vars[var_type]:
                            successor.bvp.solution.aux[var_type][var_name] = successor.val[self.convars.index(var_name)]
                    self.open_list.append(successor) #Add successor to the frontier
        #We have now updated the frontier with successors to the last bvp

        #Generate a new bvp from a node on the frontier
        if not self.open_list:
            raise ValueError('No new nodes left to explore')
        if self.goal_attempts >= len(self.moves):
            raise ValueError('Surrounded the goal node but could not solve it')

        self.open_list = sorted(self.open_list, key=lambda n: n.f, reverse=True)
        q = self.open_list.pop() #Pick the node with the smallest f
        print('Attemping node:',q.ind,'from node',q.par.ind)
        print('Node values:',self.convars,q.val)
        print('Attempts at the goal:',self.goal_attempts)

        #Clean up and return the new bvp
        self.ctr += 1
        self.last_node = q
        self.bvp = q.bvp #Update the bvp
        self.last_bvp = self.bvp
        return self.bvp

        #IDEA:
        #Show the costate guesses in between steps to see how much the solution has changed.


class HPA_Variable(object):
    def __init__(self,name,target,Nnodes,spacing='linear',confined=False):
        self.name = name
        self.target = target
        self.spacing = spacing #spacing of the continuation parameter
        self.confined = confined #whether or not the search can venture beyond the limits of the grid
        self.nodes = Nnodes #number of nodes along this axis of the graph
        self.value = np.nan
        self.index = np.nan # Index of state in BVP, obsolete
        self.steps = []
