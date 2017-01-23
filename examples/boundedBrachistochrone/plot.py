from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)

plots.add_plot().line('x','y',label='Solution')               \
                .line('x','-.5-1.5*x',label='Constraint1',step=-1,sol=-1) \
                .line('x','-2-0.75*x',label='Constraint2',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

# plots.add_plot().line('t','theta')                    \
#                 .xlabel('t (s)').ylabel('theta (degrees)')      \
#                 .title('Control history')
plots.render()
