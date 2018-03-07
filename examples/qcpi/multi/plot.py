from beluga.visualization import BelugaPlot
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print('Usage: python plot.py <n>')
# plots = BelugaPlot('./data-3v-s15.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
# 872
# plots.add_plot().line('xbar*V*tfreal','ybar*V*tfreal')\
#                 .xlabel('x(t)').ylabel('y(t)')\
#                 .title('Trajectory')
plot1 = plots.add_plot().line('xbar','ybar',label='traj1')
n = 10
for i in range(2, n+1):
    plot1.line(f'xbar{i}',f'ybar{i}',label=f'traj{i}')

# plots.add_plot().line('t','psi*180/3.14')\
#                 .line('t','psi2*180/3.14')\
#                 .line('t','psi3*180/3.14')\
#                 .line('t','psi4*180/3.14')\
#                 # .line('t','psi5*180/3.14')\
#                 # .xlabel('t (s)').ylabel('psi (deg)')\
#                 # .title('Heading')
#
# plots.add_plot().line('t','abar')\
#                 .line('t','abar2')\
#                 .line('t','abar3')\
#                 .line('t','abar4')\
#                 # .line('t','abar5')\
#                 # .xlabel('t (s)').ylabel('a (rad/s)')\
#                 # .title('Control history')
#
# plots.add_plot().line('t','xi11',label='xi11')\
#                 .line('t','ybar2/0.5',label='ybar2',style='o')\
#
#
# plots.add_plot().line('t','sqrt((xbar - xbar2)**2 + (ybar - ybar2)**2)*(V*tfreal)')\
#                 .xlabel('t').ylabel('Separation (m)')\
#                 .title('Separation')


plots.render()
