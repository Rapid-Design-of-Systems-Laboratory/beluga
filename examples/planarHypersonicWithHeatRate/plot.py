from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('theta*re/1000','h/1000')                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('t','alfa*180/3.14')                    \
                .xlabel('t (s)').ylabel('alfa (degrees)')      \
                .title('Angle of attack vs. Time')

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
Cd  = '(1.6537*alfa**2 + 0.0612)'

D   = '(0.5*'+rho+'*v**2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v**2*'+Cl+'*Aref)'

plots.add_plot().line('t','sqrt('+D+'**2+'+L+'**2)/(mass*g0)') \
                .xlabel('t (s)').ylabel('G-Loading')      \
                .title('G-Loading vs. Time')
# plots.add_plot().line('theta*re/1000','h/1000',legend='Foo')       \
#                 .line('theta*re/1000','h/1000',legend='Bar',step=1,sol=5)   \
#                 .xlabel('Downrange (km)')                   \
#                 .ylabel('h (km)')                           \
#                 .title('Altitude vs. Downrange')

plots.render()
