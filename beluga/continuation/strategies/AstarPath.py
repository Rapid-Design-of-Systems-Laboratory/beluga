#===============================================================================
# PROGRAM: "AstarPath.py"
# LOCATION: beluga>examples>Mansell
# Author: Justin Mansell (2016)
#
# Description: Finds the optimal path through terrain using a cost function,
#              J = (1-w)*tf + /wT(x,y)dl using the Astar graph search.
#===============================================================================
import numpy as np
from PIL import Image
from scipy import interpolate
from scipy import integrate
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

#Problem Parameters
w = 0.75 #Terrain cost weighting factor
V = 1.0 #Speed
elev = 1.0 #Elevation
conv = 1.0 #Time cost conversion factor for terrain
start = np.array([5.5,0.5])
goal = np.array([8,9.0])
#start = np.array([0.5,2.8])
#goal = np.array([9.0,0.5])
GridSize = [50, 50]

#Create new class for nodes in the graph
class node:

    def __init__(self,ind):
        self.name = ''
        self.ind = ind #index of the node on the grid
        self.cor = np.array([GridX[ind[0]],GridY[ind[1]]]) #coordinates of node
        self.par = [] #coordinate index of the node's parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __repr__(self):
        return repr((self.ind, self.f, self.par))

#Import terrain map and create the terrain function
img=Image.open('terrain_test2.jpg')
img=np.array(img) #Convert to array
img=np.asfarray(img)/255.0 #Scale to unity scale (and convert to float - important)
img=ndimage.gaussian_filter(img,sigma=5,order=0) #Smooth image
Xcoords=np.linspace(0,10,len(img[:,0])) #North Coordinates
Ycoords=Xcoords[0:len(img[0,:])] #East Coordinates
terr_spl=interpolate.RectBivariateSpline(Xcoords,Ycoords,img,kx=3,ky=3,s=10)

#Define the terrain function
def terrain(x,y): #Functions must be defined outside of the get_problem()
    return terr_spl.ev(x,y)

#Straight line path cost (used for computing cost of each edge in graph)
def PathCost(p1,p2):
    #p1 and p2 are tuples denoting x and y coordinates
    if np.linalg.norm(p2-p1) == 0.0:
        return 0.0
    xpts = np.linspace(p1[0],p2[0],10)
    ypts = np.linspace(p1[1],p2[1],10)
    rpts = np.linspace(0,np.linalg.norm(p2-p1),10)
    T_x_y = elev*terrain(xpts,ypts) #Terrain elevation along path
    int_T_x_y = integrate.simps(conv*w*T_x_y, rpts) #Integral portion of cost
    return (1-w)*rpts[-1]/V + int_T_x_y

#Heuristic function
def Heuristic(p):
    #p is an x,y coordinate
    return np.linalg.norm(p-goal)*(1-w)/V

#A* Search Routine
def Astar(startn,goaln):
    #startn = start node object
    #goaln = goal node object
    #returns a list of the nodes searched
    delta = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] #Different directions we can go to get to a new node
    closed_list = []
    open_list = [startn]
    nodes_searched = 0
    while len(open_list) > 0:
        open_list = sorted(open_list, key=lambda n: n.f, reverse=True)
        q = open_list.pop() #Node in open_list with the smallest f

        #Generate successors
        successors = []
        for direction in delta:
            new_ind = q.ind + direction
            if (new_ind[0] < 0) or (new_ind[0] > GridSize[0]-1) or \
                (new_ind[1] < 0) or (new_ind[1] > GridSize[1]-1):
                continue #Check to make sure we aren't going off the grid
            else:
                successors.append(node(new_ind))
                successors[-1].par = q.ind #Set the parent of each successor to q

        for successor in successors:
            skip = 0 #skip flag
            if successor.ind[0] == goaln.ind[0] and \
                successor.ind[1] == goaln.ind[1]:
                goaln.par = q.ind #Set goal's parent to q
                closed_list.append(q)
                return closed_list #Found the goal...we're done

            successor.g = q.g + PathCost(q.cor,successor.cor)
            successor.h = Heuristic(successor.cor)
            successor.f = successor.g + successor.h

            for n in open_list:
                if n.ind[0] == successor.ind[0] and n.ind[1] == successor.ind[1] \
                    and n.f < successor.f:
                    skip = 1
                    break
            for n in closed_list:
                if n.ind[0] == successor.ind[0] and n.ind[1] == successor.ind[1] \
                    and n.f < successor.f:
                    skip = 1
                    break

            if skip == 1:
                continue
            else:
                open_list.append(successor)

        closed_list.append(q)
        nodes_searched += 1
        print('Nodes searched:',nodes_searched)

    return closed_list


#A* initialization
GridX = np.linspace(Xcoords[0],Xcoords[-1],GridSize[0]) #Grid X coordinates
GridY = np.linspace(Ycoords[0],Ycoords[-1],GridSize[1]) #Grid Y coordinates

start_ind = np.array([abs(GridX-start[0]).argmin(),abs(GridY-start[1]).argmin()]) #Start node index
startnode = node(start_ind)
startnode.name = 'Start'

goal_ind = np.array([abs(GridX-goal[0]).argmin(),abs(GridY-goal[1]).argmin()]) #Goal node index
goalnode = node(goal_ind)
goalnode.name = 'Goal'

#A* search
closed_list = Astar(startnode, goalnode)

#Plot the path
xpath = []
ypath = []

tracknode = goalnode
while (tracknode.ind[0] != startnode.ind[0]) or (tracknode.ind[1] != startnode.ind[1]):
    xpath.append(tracknode.cor[0])
    ypath.append(tracknode.cor[1])
    parent = [n for n in closed_list if (n.ind[0] == tracknode.par[0] and n.ind[1] == tracknode.par[1])]
    parent = sorted(parent, key=lambda n: n.f, reverse=True)
    tracknode = parent.pop() #Take the parent with the lowest f value

xpath.append(startnode.cor[0])
ypath.append(startnode.cor[1])

Y,X = np.meshgrid(Ycoords, Xcoords)
terrData=terr_spl.ev(X,Y) #Create the elevation data based on the spline fit

plt.figure(1)
plt.axis([0,Ycoords[-1],0,Xcoords[-1]])
plt.contour(Ycoords,Xcoords,terrData)
plt.xlabel('East (km)')
plt.ylabel('North (km)')
plt.plot(ypath,xpath,'r') #Plot final path
plt.scatter([startnode.cor[1],goalnode.cor[1]],[startnode.cor[0],goalnode.cor[0]],c='r')
plt.show()
