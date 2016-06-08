from beluga.visualization import BelugaPlot

plots = BelugaPlot('./cart120.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('x_n*x_s','y_n*y_s')                    \
                # .xlabel('t (s)').ylabel('h (km)')      \
                # .title('Altitude vs. Time')

plots.add_plot().line('t', 'sin(w)') \
    # .xlabel('t (s)').ylabel('h (km)')      \
# .title('Altitude vs. Time')

plots.add_plot().line('t', 'theta_n') \

plots.add_plot().line('t', 'p22_n*p22_s') \

plots.add_plot().line('t', 'p11_n*p11_s') \

# plots.add_plot().line('t','alfa*180/3.14')                    \
#                 .xlabel('t (s)').ylabel('alfa (degrees)')      \
#                 .title('Angle of attack vs. Time')

# plots.add_plot().line('theta*re/1000','h/1000',legend='Foo')       \
#                 .line('theta*re/1000','h/1000',legend='Bar',step=1,sol=5)   \
#                 .xlabel('Downrange (km)')                   \
#                 .ylabel('h (km)')                           \
#                 .title('Altitude vs. Downrange')

plots.render()
