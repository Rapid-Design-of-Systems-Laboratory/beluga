from beluga.visualization import BelugaPlot

plots = BelugaPlot('data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('x','y')                    \
                # .xlabel('t (s)').ylabel('h (km)')      \
                # .title('Altitude vs. Time')

plots.add_plot().line('t', 'u') \
    # .xlabel('t (s)').ylabel('h (km)')      \
# .title('Altitude vs. Time')

# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

# plots.add_plot().line('theta*re/1000','h/1000',legend='Foo')       \
#                 .line('theta*re/1000','h/1000',legend='Bar',step=1,sol=5)   \
#                 .xlabel('Downrange (km)')                   \
#                 .ylabel('h (km)')                           \
#                 .title('Altitude vs. Downrange')

plots.render()
