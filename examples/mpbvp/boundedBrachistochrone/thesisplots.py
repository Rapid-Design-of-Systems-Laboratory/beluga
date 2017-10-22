from beluga.visualization import BelugaPlot

plots = BelugaPlot('./data.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

def postprocess_xy_plot(fig, plot):
    """fig: Matplotlib figure object.
    plot: Plot object."""

    print('postprocessing yeaaa!')

plots.add_plot().line_series('x','y', step=2, start=0, skip=2) \
                .line('x','-1.0-x',label='x + y + 1 = 0',step=-1,sol=-1) \
                .xlabel('x(t)').ylabel('y(t)')      \
                .title('Trajectory') \
                .postprocess(postprocess_xy_plot)
# .line('x','-2-0.75*x',label='Constraint2',step=-1,sol=-1) \
plots.add_plot().line('t','theta*180/3.14')                    \
                .line_series('t','theta*180/3.14', step=2, start=0, skip=2) \
                .xlabel('t (s)').ylabel('theta (degrees)')      \
                .title('Control history')

# plots.add_plot().line('t','lamX')                    \
#                 .xlabel('t (s)').ylabel('lamX')      \
#                 .title('lamX')

plots.render()
