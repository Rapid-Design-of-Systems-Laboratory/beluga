from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill

# plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)
ds = Dill('./data2.dill')
# ds2 = Dill('./phu_2k5_eps4.dill')
plots = BelugaPlot(datasource=ds,default_sol=-1,default_step=-1, renderer='matplotlib')
# plots = BelugaPlot('./phu_2k5_eps4.dill',default_sol=-1,default_step=-1, renderer='bokeh')
#
# plots.add_plot().line_series('theta*re/1000','h/1000', step=-1, skip=3)                    \
#                 .xlabel('Downrange (km)').ylabel('h (km)')      \
#                 .title('Altitude vs. Downrange')

plots.add_plot().line('theta*re/1000','h/1000',datasource=ds,label='DS1')                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')
#                .line('theta*re/1000','h/1000',datasource=ds2,label='DS2')                   \
#
# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

plots.add_plot().line_series('v/1000','h/1000', step=-1, skip=1)                    \
                .xlabel('v (km/s)').ylabel('h (km)')      \
                .title('Altitude vs. Velocity')

plots.add_plot().line_series('t','alfa*180/3.14', step=-1, skip=1)                    \
                .xlabel('t (s)').ylabel('alfa (degrees)')      \
                .title('Angle of attack vs. Time')

# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

plots.render()
