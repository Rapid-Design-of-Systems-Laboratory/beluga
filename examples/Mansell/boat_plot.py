import dill
import matplotlib.pyplot as plt
import numpy as np

f = open('data.dill','rb')
out=dill.load(f)
f.close()
xsol=out['solution'][-1][-1].y[0,:]
ysol=out['solution'][-1][-1].y[1,:]
hdgsol=out['solution'][-1][-1].y[2,:]
tf=out['solution'][-1][-1].y[6,0]
tsol=out['solution'][-1][-1].x*tf

plt.figure(1)
plt.plot(ysol,xsol)

plt.figure(2)
plt.plot(tsol,hdgsol)

plt.show()
