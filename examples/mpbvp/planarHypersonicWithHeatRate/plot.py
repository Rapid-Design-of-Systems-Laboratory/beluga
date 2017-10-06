from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('theta*180/3.14','h/1000')                    \
                .xlabel('Downrange (km)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('t','alfa*180/3.14')                    \
                .xlabel('t (s)').ylabel('alfa (degrees)')      \
                .title('Angle of attack vs. Time')


plots.add_plot().line('t','lamV')                    \
                .xlabel('t (s)').ylabel('lamV')      \
                .title('lamV vs. Time')

rho = 'rho0*exp(-h/H)'
Cl  = '(1.5658*alfa + -0.0000)'
Cd  = '(1.6537*alfa**2 + 0.0612)'

D   = '(0.5*'+rho+'*v**2*'+Cd+'*Aref)'
L   = '(0.5*'+rho+'*v**2*'+Cl+'*Aref)'

plots.add_plot().line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/10000') \
                .xlabel('t (s)').ylabel('Heat-rate')      \
                .title('Heat-rate vs. Time')

# plots.add_plot().line('theta*re/1000','h/1000',label='Foo')       \
#                 .line('theta*re/1000','h/1000',label='Bar',step=1,sol=5)   \
#                 .xlabel('Downrange (km)')                   \
#                 .ylabel('h (km)')                           \
#                 .title('Altitude vs. Downrange')

plots.render()
