import dill
import matplotlib.pyplot as plt
import numpy as np

#Load data
f = open('data.dill','rb')
out=dill.load(f)
f.close()
solution_set = out['solution'][-1]
tf=out['solution'][-1][-1].y[8,-1]
tsol=out['solution'][-1][-1].x*tf
hsol=out['solution'][-1][-1].y[0,:]
thetta=out['solution'][-1][-1].y[1,:]
vsol=out['solution'][-1][-1].y[2,:]
alfasol=out['solution'][-1][-1].u[0,:]

#Plot
plt.figure(1)
plt.plot(thetta*6378,hsol/1000,'k')
axes = plt.gca()
axes.set_xlim([0,thetta[-1]*6378])
plt.xlabel('Downrange (km)')
plt.ylabel('Altitude (km)')
plt.title('Warhead Path')
#plt.savefig('Pathfapprox.png')
plt.savefig('PathS.png')

plt.figure(2)
plt.plot(tsol,vsol/1000,'g')
plt.xlabel('Time since release (s)')
plt.ylabel('Velocity (km/s)')
plt.title('Warhead Velocity')
#plt.savefig('Velfapprox.png')
plt.savefig('VelS.png')

plt.figure(3)
plt.plot(tsol,alfasol*180/np.pi,'b')
plt.xlabel('Time since release (s)')
plt.ylabel('Angle of Attack (deg)')
plt.title('Control Profile')
#plt.savefig('Controlfapprox.png')
plt.savefig('ControlS.png')
plt.show()



#END
