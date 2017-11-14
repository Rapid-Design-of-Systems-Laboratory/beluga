from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print('Usage: python plot.py <n>')
    sys.exit(1)

# plots = BelugaPlot('./data-3v-s15.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plot1 = plots.add_plot().line('xbar','ybar',label='traj1')
n = int(sys.argv[1])

for i in range(2, n+1):
    plot1.line(f'xbar{i}',f'ybar{i}',label=f'traj{i}')
plot1.line('xc+rc*cos(2*pi*t/tf)','yc+rc*sin(2*pi*t/tf)')
plot1.postprocess(lambda r,f,p: plt.axis('equal'))
plots.render()
