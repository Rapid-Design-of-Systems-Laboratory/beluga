from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
mpbvp_ds = Dill('../../mpbvp/boundedBrachistochrone/data.dill')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='ICRM Solution', sol=-1, step=-1)               \
                .line('x','y',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1)\
                .line('x','y',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1)\
                .line('x','-1.0-x',label='Constraint1',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','theta*180/3.14',label='ICRM Solution')                    \
                .line('t','theta*180/3.14',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1)\
                .line('t','theta*180/3.14',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1)\
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')

plots.render()
