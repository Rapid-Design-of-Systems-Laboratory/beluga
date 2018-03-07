from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=0)
mpbvp_ds = Dill('../../mpbvp/planarHypersonicWithHeatRate/data_1200.dill')
plots = BelugaPlot('./data_1200_2deg15km_ep4.dill',default_sol=-1,default_step=-1, renderer='matplotlib')


plots.add_plot().line('theta*180/3.14','h/1000',label='ICRM Solution')                    \
                .xlabel('Downrange (deg)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange') \
                .line('theta*180/3.14','h/1000',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1) \

plots.add_plot().line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000',label='ICRM Solution') \
                .line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1) \
                .xlabel('t (s)').ylabel('Heat-rate')      \
                .title('Heat-rate vs. Time')

# plots.add_plot().line('t','theta*180/3.14',label='ICRM Solution')                    \
#                 .line('t','theta*180/3.14',label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1)\
#                 .line('t','theta*180/3.14',label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1)\
#                 .xlabel('t (s)').ylabel('theta (degrees)')      \
#                 .title('Control history')
#
# plots.add_plot().line('t','lamY', label='ICRM Solution')                    \
#                 .line('t','lamY', label='MPBVP Solution', datasource=mpbvp_ds, step=-1, sol=-1)\
#                 .line('t','lamY', label='Unconstrained Solution', datasource=mpbvp_ds, step=0, sol=-1) \
#                 .xlabel('t (s)').ylabel('lamY')      \
#                 .title('lamY')

plots.render()
