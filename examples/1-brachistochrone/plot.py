from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plot1 = plots.add_plot()
plot1.line('x','y')
plot1.xlabel('x(t)')
plot1.ylabel('y(t)')
plot1.title('Trajectory time history')

plot2 = plots.add_plot()
plot2.line('t','180/pi*theta')
plot2.xlabel('t (s)')
plot2.ylabel('theta (degrees)')
plot2.title('Control time history')

plots.render()
