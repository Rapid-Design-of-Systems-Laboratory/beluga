from beluga.visualization import BelugaPlot
from beluga.visualization.datasources import Dill

plots = BelugaPlot('./data.dill', default_sol=-1, default_step=-1, renderer='matplotlib')

plots.add_plot().line_series('v', 'h') \
    .xlabel('v [$m/s$]').ylabel('h [m]') \
    .title('h-v Plot')

plots.add_plot().line_series('theta*180/3.14159', 'h') \
    .xlabel(r'$\theta$ [deg]').ylabel('$h$ [m]') \
    .title('Downrange')

plots.add_plot().line_series('theta*180/3.14159', 'phi*180/3.14159') \
    .xlabel(r'$\theta$ [deg]').ylabel('$\phi$ [deg]') \
    .title('Ground Track')

plots.add_plot() \
    .line('t', 'alpha') \
    .line('t', 'bank') \
    .xlabel('t (s)').ylabel('alpha (degrees)') \
    .title('Control history')

plots.add_plot().line_series('t', 'gam*180/3.14159') \
    .xlabel('t [s]').ylabel(r'$\gamma$ [deg]') \
    .title('Flight Path Angle')

plots.add_plot().line_series('t', 'lamV') \
    .xlabel('t [s]').ylabel(r'$\lambda_v$') \
    .title('$\lambda_v$')

plots.render()

