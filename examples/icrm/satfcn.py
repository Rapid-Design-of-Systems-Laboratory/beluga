import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 'x-large'
mpl.rcParams['legend.fontsize'] = 'x-large'
mpl.rcParams['xtick.labelsize'] = 'x-large'
mpl.rcParams['ytick.labelsize'] = 'x-large'
output_dir = './'

def onesided_upper(x, lim):
    return lim - np.exp(-x)

def onesided_lower(x, lim):
    return lim + np.exp(x)

def twosided(x, lb, ub):
    s = 4/(ub - lb)
    return ub - (ub-lb)/(1.0+np.exp(s*x))

x = np.linspace(-2, 2, 100)

plt.plot(x, onesided_upper(x, 1), label='One-sided SatFcn - Upper', lw = 2.0)
plt.plot(x, onesided_lower(x, -1), label='One-sided SatFcn - Lower', lw = 2.0)
plt.plot(x, np.ones_like(x)*-1, label='Lower limit', ls='dashed', color='k')
plt.plot(x, np.ones_like(x)*1, label='Upper limit', ls='dashed', color='r')
# plt.plot(x, twosided(x, -1, 1), label='Two-sided SatFcn', lw = 2.0)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$\\psi(x)$')
plt.legend()
tikz_save(output_dir+'satfcn_onesided.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
plt.show()

plt.plot(x, twosided(x, -1, 1), label='Two-sided SatFcn', lw = 2.0)
plt.plot(x, np.ones_like(x)*-1, label='Lower limit', ls='dashed', color='k')
plt.plot(x, np.ones_like(x)*1, label='Upper limit', ls='dashed', color='r')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$\\psi(x)$')
plt.legend(loc='lower right')
tikz_save(output_dir+'satfcn_twosided.tex', figureheight='\\figureheight', figurewidth='\\figurewidth')
plt.show()
