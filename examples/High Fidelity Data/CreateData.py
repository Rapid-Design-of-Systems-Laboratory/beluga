#==============================================================================#
"""Creates a look-up table of aerodynamic data for a sphere-cone vehicle"""
#==============================================================================#
import numpy as np
import matplotlib.pyplot as plt

#Parameters
dc = 25 #Cone angle [deg]
rc = 0.3 #Cone base radius [m]
rn = 0.01 #Nose cone radius [m]
n_sides = 100 #Number of polygons rounding cross-section perpindicular to axis
n_round = 50 #Number of polygons rounding cross-section parallel to axis
fname = 'SphereConeTable.txt'

class plate:
    """Flat square plate object for computing aerodynamic coefficients"""

    def __init__(self,N,A):
        self.N = N #Normal vector in cartesian coords
        self.A = A #Area of the plate
        self.pos = None #position of the center of the plate in cartesian coords
        self.alfa = None #local AoA

    def __repr__(self):
        return repr((self.N,self.s,self.pos))

def sphere_cone(dc, rc, rn, n_sides, n_round):
    """Initializes a sphere-cone made from flat plates"""
    z1 = (rc - rn*np.cos(dc)) / np.tan(dc) #Height of the tangency point
    shape = []

    #Cone part
    s_base = 2 * rc * np.sin(np.pi/n_sides)
    s_tip = 2 * rn*np.cos(dc) * np.sin(np.pi/n_sides)
    for ii in range(0,n_sides):
        thta = 2*ii*np.pi/n_sides
        N = np.array([np.cos(thta),np.sin(thta),np.tan(dc)])
        A = 0.5 * (s_base + s_tip) * z1/np.cos(dc)
        shape.append(plate(N,A))

    #Sphere part
    dn_list = np.linspace(dc, np.pi/2, n_round+1)
    for j in range(0,len(dn_list)-1):
        dn = np.mean(dn_list[j:j+2])
        s_base = 2 * rn*np.cos(dn_list[j]) * np.sin(np.pi/n_sides)
        s_tip = 2 * rn*np.cos(dn_list[j+1]) * np.sin(np.pi/n_sides)
        A = 0.5 * (s_base + s_tip) * 2*rn*np.sin((np.pi/2 - dc)/(2*n_round))
        for ii in range(0,n_sides):
            thta = 2*ii*np.pi/n_sides
            N = np.array([np.cos(thta),np.sin(thta),np.tan(dn)])
            shape.append(plate(N,A))

    return shape

def compute_coeffs(shape, Aref, alfa):
    """Computes the lift and drag coefficients of the given shape at the given
    angle of attack using the given reference area"""
    alfa_vect = np.array([-np.sin(alfa),0,-np.cos(alfa)])
    Fvect = np.array([0,0,0]) #Force coefficient vector

    for panel in shape:
        panel.alfa = np.arcsin(np.dot(alfa_vect,-panel.N)/ \
                    (np.linalg.norm(alfa_vect)*np.linalg.norm(panel.N)))
        panel_Cpvect = (panel.A/Aref) * (2*np.sin(panel.alfa)**2) * (-panel.N/np.linalg.norm(panel.N))
        Fvect = Fvect + panel_Cpvect

    CN = -Fvect[0]#np.dot(Fvect,np.array([-1,0,0]))
    CA = -Fvect[2]#np.dot(Fvect,np.array([0,0,-1]))
    CL = CN * np.cos(alfa) - CA * np.sin(alfa)
    CD = CA * np.cos(alfa) + CN * np.sin(alfa)

    #return CA, CN
    return CL, CD

#Initialization
dc = dc * np.pi / 180
alfa_rng = np.linspace(-dc,dc,100)
shape = sphere_cone(dc, rc, rn, n_sides, n_round)

#Compute Newtonian Data
CLlist = []
CDlist = []
for alfa in alfa_rng:
    CL, CD = compute_coeffs(shape,np.pi*rc**2,alfa)
    CLlist.append(CL)
    CDlist.append(CD)

#Output the table (format: alfa,CL,CD)
f = open(fname, 'w+')
outdata = np.array([alfa_rng, CLlist, CDlist])
outdata = outdata.T
np.savetxt(fname, outdata, fmt = ['%f', '%f', '%f'])
f.close()

#END
