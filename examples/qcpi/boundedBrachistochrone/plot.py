from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
unc_ds = Dill('../../mpbvp/boundedBrachistochrone/data.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='Solution', sol=-1, step=-1,style={'lw':2.0})               \
                .line('x','y',label='Unconstrained Solution', datasource=unc_ds, step=0, sol=-1,style={'lw':2.0})\
                .line('x','xlim-x',label='Constraint1',step=-1,sol=-1) \
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
