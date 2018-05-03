import numpy as np
import dill
import scipy.io

fname = 'phu_2k5_eps4'
f = open(fname+'.dill', 'rb')
out = dill.load(f)
f.close()
sol_array = out['solution'][-1]

mat_array = []
for sol in sol_array:
    new_x = np.linspace(sol.x[0],sol.x[-1],512)
    sol.interpolate(new_x, overwrite=True)
    sol.__dict__['state_list'] = []
    sol.__dict__['var_dict'] = {}
    mat_array.append(sol.__dict__)
#
# from beluga.utils import keyboard
# keyboard()
scipy.io.savemat(fname+'.mat', mdict={'sol_array':mat_array})
