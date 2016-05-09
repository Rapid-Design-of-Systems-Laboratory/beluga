from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1)

plots.add_plot().line('t','x')                    \
                .xlabel('t (s)').ylabel('x(t)')      \
                .title('Position vs. Time')

plots.add_plot().line('t','(lim - (2*lim/(1+exp((2/lim)*xi11))))')                    \
                .xlabel('t (s)').ylabel('psi(t)')      \
                .title('psi1 vs. Time')

plots.add_plot().line('t','lim*v')                    \
                .xlabel('t (s)').ylabel('lim*v(t)')      \
                .title('Control history')

plots.add_plot().line('t','v')                    \
                .xlabel('t (s)').ylabel('v(t)')      \
                .title('v vs. t')

plots.add_plot().line('t','xi12')                    \
                .xlabel('t (s)').ylabel('xi12(t)')      \
                .title('xi12 vs. t')
plots.render()
