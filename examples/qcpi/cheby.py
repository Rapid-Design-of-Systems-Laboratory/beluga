import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'
output_dir = './'

def T_k(k, x):
    return np.cos(k*np.arccos(x))

x = np.linspace(-1, 1, 100)

for k in range(6):
    plt.plot(x, T_k(k, x), label=f'T_{k}(x)', lw = 2.0)

plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$T_k(x)$')
plt.legend()
# plt.savefig('cheby.eps')

N = 20
k = np.arange(N+1)
xk = np.cos(k*np.pi/N)

plt.figure()
plt.plot(xk, np.zeros_like(xk), marker='x',lw=0.0)
plt.grid(True)
plt.xlabel('$x$')
plt.savefig('cgl_nodes.eps')
plt.show()
