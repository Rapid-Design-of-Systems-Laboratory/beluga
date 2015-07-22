from beluga.visualization import BelugaPlot

plots = BelugaPlot('/Users/tantony/dev/mjgrant-beluga/examples/data.dill',default_step=1,default_sol=10)

plots.add_plot().line('t','h/1000')                    \
                .xlabel('t (s)').ylabel('h (km)')      \
                .title('Altitude vs. Time')

plots.add_plot().line('theta*re/1000','h/1000',legend='Foo')       \
                .line('theta*re/1000','h/1000',legend='Bar',step=1,sol=5)   \
                .xlabel('Downrange (km)')                   \
                .ylabel('h (km)')                           \
                .title('Altitude vs. Downrange')

plots.render()
