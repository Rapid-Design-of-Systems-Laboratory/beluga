from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('x','y',legend='Solution')               \
                .line('x','+_constraint1_lim-x',legend='Constraint',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','theta')                    \
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')
plots.render()
