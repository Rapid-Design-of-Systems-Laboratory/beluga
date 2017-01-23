#Writes data.dill output to a text file
#import numpy as np
import dill

f = open('data.dill','rb')
out=dill.load(f)
f.close()

xout=out['solution'][-1][-1].y[0,:]
yout=out['solution'][-1][-1].y[1,:]

#tout=[out['solution'][-1][1].x]
#xout=[out['solution'][-1][1].y[0,:]]
#yout=[out['solution'][-1][1].y[1,:]]
#lengths=[len(tout[0])]
#for i in range(2,7):
#    tout.append(out['solution'][-1][i].x)
#    xout.append(out['solution'][-1][i].y[0,:])
#    yout.append(out['solution'][-1][i].y[1,:])
#    lengths.append(len(tout[-1]))


f = open('DillData00.txt','w')
for i in range(len(xout)):
    f.write('{0} {1}\n'.format(xout[i],yout[i]))



#for i in range(max(lengths)):
#    for j in range(6):
#        try:
#            f.write('{0} {1} '.format(xout[j][i],yout[j][i]))
#        except:
#            f.write('{0} {1} '.format(xout[j][-1],yout[j][-1]))
#        if j==5:
#            f.write('\n')

f.close()