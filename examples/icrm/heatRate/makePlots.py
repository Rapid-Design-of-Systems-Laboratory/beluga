from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill
# from beluga.visualization.renderers import ToyPlot

ds_constraint = Dill('./data-1k2-eps4-eps4.dill') # 26 steps
ds_epsHR = Dill('./data-1k2-eps6-eps4.dill') # 36 steps
ds_epsAlfa = Dill('./data-1k2-eps6-eps7.dill') # 36 steps

# toyplot = ToyPlot(backend = 'png')
# plots = BelugaPlot(datasource=ds_constraint,default_sol=-1,default_step=-1,renderer='bokeh')
plots = BelugaPlot('./data-1k2-eps4-eps4.dill',default_sol=-1,default_step=-1,renderer='matplotlib')

qdot = 'k*v**3*sqrt(rho0*exp(-h/H)/rn)'
# 90
plots.add_plot(mesh_size=512).line_series('theta*re/1000','h/1000', skip=5, datasource=ds_constraint)   \
                .xlabel('Downrange (km)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot(mesh_size=512).line_series('t','qdot/1e4', skip=5, datasource=ds_constraint)              \
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot(mesh_size=512).line_series('t','alfa*180/3.14', skip=5, datasource=ds_constraint) \
                .line('t','alfaMax*180/3.14', datasource=ds_epsAlfa) \
                .xlabel('t (s)').ylabel('Alpha (deg)')      \
                .title('Control History')

plots.add_plot(mesh_size=512).line_series('v/1000','h/1000', skip=5, datasource=ds_constraint) \
                .xlabel('Velocity (km/s)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Velocity')

# 53
plots.add_plot().line_series('theta*re/1000','h/1000', skip=2, datasource=ds_epsHR)   \
                .xlabel('Downrange (km)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line_series('t',f'{qdot}/1e4', skip=2, datasource=ds_epsHR)              \
                .line('t','qdotMax/1e4')    \
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot().line_series('t','alfa*180/3.14', skip=2, datasource=ds_epsHR) \
                .line('t','alfaMax*180/3.14', datasource=ds_epsAlfa) \
                .xlabel('t (s)').ylabel('Alpha (deg)')      \
                .title('Control History')

plots.add_plot().line_series('v/1000','h/1000', skip=2, datasource=ds_epsHR) \
                .xlabel('Velocity (km/s)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Velocity')
#
#
# # 44
plots.add_plot().line_series('theta*re/1000','h/1000', skip=2, datasource=ds_epsAlfa)   \
                .xlabel('Downrange (km)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line_series('t',f'{qdot}/1e4', skip=2, datasource=ds_epsAlfa)              \
                .line('t','qdotMax/1e4')    \
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot().line_series('t','alfa*180/3.14', skip=2, datasource=ds_epsAlfa) \
                .line('t','alfaMax*180/3.14', datasource=ds_epsAlfa) \
                .xlabel('t (s)').ylabel('Alpha (deg)')      \
                .title('Control History')

plots.add_plot().line_series('v/1000','h/1000', skip=2, datasource=ds_epsAlfa) \
                .xlabel('Velocity (km/s)').ylabel('Altitude (km)')      \
                .title('Altitude vs. Velocity')
plots.render()
