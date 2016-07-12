import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from beluga.visualization import BelugaPlot2 as Bp2

out = Bp2.load_dill('cart123')
num_sol = len(out['solution'][-1])

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
x = Bp2.retrieve('x_s*x_n', out, step=-1, sol=0)
y = Bp2.retrieve('y_s*y_n', out, step=-1, sol=0)
l, = plt.plot(x, y, lw=2)
ax.axis([0,250,-8,8])


class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % num_sol
        x = Bp2.retrieve('x_s*x_n', out, step=-1, sol=i)
        y = Bp2.retrieve('y_s*y_n', out, step=-1, sol=i)
        l.set_xdata(x)
        l.set_ydata(y)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % num_sol
        x = Bp2.retrieve('x_s*x_n', out, step=-1, sol=i)
        y = Bp2.retrieve('y_s*y_n', out, step=-1, sol=i)
        l.set_xdata(x)
        l.set_ydata(y)
        plt.draw()

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()