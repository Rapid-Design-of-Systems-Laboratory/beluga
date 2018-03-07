from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('t','x')                    \
                .xlabel('t (s)').ylabel('x(t)')      \
                .title('Position vs. Time')
#
# plots.add_plot().line('t','(_xlim - (2*_xlim/(1+exp((2/_xlim)*xi11))))')                    \
#                 .xlabel('t (s)').ylabel('psi(t)')      \
#                 .title('psi1 vs. Time')

plots.add_plot().line('t','u')                    \
                .xlabel('t (s)').ylabel('u(t)')      \
                .title('Control history')

plots.add_plot().line('t','v')                    \
                .xlabel('t (s)').ylabel('v(t)')      \
                .title('v vs. t')

plots.add_plot().line('t','xi12')                    \
                .xlabel('t (s)').ylabel('xi12(t)')      \
                .title('xi12 vs. t')
plots.render()
