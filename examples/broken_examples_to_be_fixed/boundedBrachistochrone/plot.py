from beluga.visualization import BelugaPlot

# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='Solution')               \
                .line('x','y',label='Unconstrained', step=0, sol=-1) \
                .line('x','-1.0-x',label='Constraint1',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')
# .line('x','-2-0.75*x',label='Constraint2',step=-1,sol=-1) \
plots.add_plot().line('t','theta*180/3.14')                    \
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')

plots.add_plot().line('t','lamX')                    \
                .xlabel('t (s)').ylabel('lamX')      \
                .title('lamX')

plots.render()
