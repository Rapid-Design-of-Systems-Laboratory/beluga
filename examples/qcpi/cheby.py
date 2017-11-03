import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
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
# tikz_save(output_dir+'satfcn_onesided.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
plt.savefig('cheby.eps')
plt.show()
