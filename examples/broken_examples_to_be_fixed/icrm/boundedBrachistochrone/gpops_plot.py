from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill, GPOPS

gpops_ds = GPOPS('./brachisto_eps5.mat',states=('x','y','v','xi','tf'),controls=('theta','ue1'))
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot(mesh_size=None).line('x','y',label='ICRM Solution', sol=-1, step=-1) \
                .line('x','y',label='GPOPS Solution', style='o',sol=-1, step=-1, datasource=gpops_ds)          \
                .line('x','-1.0-x',label='Constraint1',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)') \
                .title('Trajectory')

plots.add_plot(mesh_size=None).line('t','ue1',label='ICRM') \
                .line('t','ue1',label='GPOPS',datasource=gpops_ds,style='o') \
                .xlabel('t (s)').ylabel('theta (degrees)') \
                .title('Control history')

plots.add_plot(mesh_size=None).line('t','theta*180/3.14',label='ICRM') \
                .line('t','theta*180/3.14',label='GPOPS',datasource=gpops_ds,style='o') \
                .xlabel('t (s)').ylabel('theta (degrees)') \
                .title('Control history')

plots.add_plot(mesh_size=None).line('t','lamX')\
                .line('t','lamY')\
                .line('t','lamV')\
                .line('t','lamXI11')\
                .line('t','lamX',datasource=gpops_ds,style='o') \
                .line('t','lamY',datasource=gpops_ds,style='o') \
                .line('t','lamV',datasource=gpops_ds,style='o') \
                .line('t','lamXI',datasource=gpops_ds,style='o') \
                .xlabel('t (s)').ylabel('lambda') \
                .title('lamX')
plots.render()
