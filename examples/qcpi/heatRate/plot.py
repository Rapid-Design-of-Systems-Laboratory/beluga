from beluga.visualization import BelugaPlot

# plots = BelugaPlot('./data_fpa60_ms.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

# plots.add_plot().line('theta*180/3.14','h/1000')                    \
#                 .xlabel('Downrange (deg)').ylabel('h (km)')      \
#                 .title('Altitude vs. Downrange')

plots.add_plot().line_series('t','qdot/1e4',step=2)\
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')
                # .line('t','qdotMax/1e4')    \

plots.add_plot().line_series('t','qdot/1e4',step=3)\
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot().line_series('t','qdot/1e4',step=4)\
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot().line_series('t','qdot/1e4',step=5)\
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

plots.add_plot().line_series('t','qdot/1e4',step=6)\
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

# plots.add_plot().line('t','alfa*180/3.14') \
#                 .xlabel('t (s)').ylabel('Alpha (deg)')      \
#                 .title('Control History')
#
# # plots.add_plot().line('t','gam*180/3.14') \
# plots.add_plot().line('t','v/1000') \
#                 .xlabel('t (s)').ylabel('v (km/s)')      \
#                 .title('FPA')
#
plots.render()
