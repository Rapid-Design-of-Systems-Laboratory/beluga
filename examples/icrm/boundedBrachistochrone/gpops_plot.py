from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill, GPOPS
# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
gpops_ds = GPOPS('./brachisto_eps1.mat',states=('x','y','v','xi'),controls=('theta','ue1'))
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('x','y',label='GPOPS Solution', sol=-1, step=-1, datasource=gpops_ds)               \
                .line('x','-1.0-x',label='Constraint1',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory')

plots.add_plot().line('t','theta*180/3.14',datasource=gpops_ds)                    \
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')

plots.add_plot().line('t','lamX',datasource=gpops_ds)                    \
                .xlabel('t (s)').ylabel('lamX')      \
                .title('lamX')
plots.render()
