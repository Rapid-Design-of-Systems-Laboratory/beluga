from beluga.visualization import BelugaPlot

# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='Solution')               \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')
# .line('x','-2-0.75*x',label='Constraint2',step=-1,sol=-1) \
plots.add_plot().line('t','delta*180/3.14')                    \
                .xlabel('t (s)').ylabel('delta (degrees)')      \
                .title('Steering')
#
# plots.add_plot().line('t','theta*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('theta (degrees)')      \
#                 .title('Heading')
plots.render()
