# Plots problem setup
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

V = 300
tfreal = 50

y0 = np.array([-0.05, 0.1, 0.15, -0.1,-0.15])*V*tfreal/1e3
yf = np.array([0.0, 0.0, 0.0, -0.05,-0.05])*V*tfreal/1e3
x0 = np.ones_like(y0)*-0.8*V*tfreal/1e3
xf = np.zeros_like(y0)
plt.figure()
ax = plt.gca()
plt.plot(x0,y0,marker='>',ms=10,lw=0.0)

for i,(x,y) in enumerate(zip(x0,y0),1):
    plt.text(x-0.45,y+0.05,str(i))
plt.plot([0.0],[0.0],'x',ms=10,mew=3,color='k')
plt.text(0.25,-0.05,'B')
plt.plot([0.0],[-0.05*V*tfreal/1e3],'x',ms=10,mew=3,color='orange')
plt.text(0.25,-0.75-0.05,'A')
ax.add_patch(Circle((-0.6*V*tfreal/1e3, 0.0), radius=0.1*V*tfreal/1e3, fill=False, hatch='/', color='r'))
plt.xlabel('$x$ [km]')
plt.ylabel('$y$ [km]')
plt.grid(True)
plt.savefig('./plots/app_scenario.pdf')
plt.show()
