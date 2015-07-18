from beluga.visualization.renderers import Renderer
from matplotlib.pyplot import *

class MatPlotLibRenderer(Renderer):
    """
    A renderer class that implements matplotlib
    """
    def __init__(self):
        self._figures = []

    def _get_figure(self,f):
        """
        Returns Figure instance from internal list using index

        Raises:
            ValueError if invalid index is used
        """
        try:
            fh =  self._figures[f]
            if fh is None:
                raise ValueError('Invalid figure handle specified!')
            return fh
        except:
            raise ValueError('Invalid figure handle specified!')

    def create_figure(self):
        """
        Creates a new figure and returns a handle
        """
        self._figures.append(figure())
        return len(self._figures)-1

    def close_figure(self,f):
        """
        Closes a specified figure
        """
        close(self._get_figure(f))

    def show_figure(self,f,block=False):
        """
        Shows a specified figure
        """
        show(self._get_figure(f))

    def render_plot(self,f,p):
        """
        Adds a line plot using the given data to the specified figure
        """
        fh = self._get_figure(f);
        plot(p.x_data,p.y_data,figure=fh)
        if p._xlabel is not None:
            xlabel(p._xlabel,figure=fh)
        if p._ylabel is not None:
            ylabel(p._ylabel,figure=fh)
        if p._title is not None:
            title(p._title,figure=fh)

    def render_subplot(self,f,index,plot):
        """
        Adds a subplot to the specified figure
        """
        pass

if __name__ == '__main__':
    from beluga.visualization.elements import Plot
    import dill

    r = MatPlotLibRenderer()
    fig = r.create_figure()

    with open('/Users/tantony/dev/mjgrant-beluga/examples/data.dill','rb') as f:
        out = dill.load(f)

    p = Plot(0,-1)
    p.x('v/1000')
    p.y('h/1000')
    p.xlabel('v (km/s)')
    p.ylabel('h (km)')
    p.title('Altitude vs. Velocity')
    p.preprocess(out['solution'],out['problem_data'])

    r.render_plot(fig,p)
    r.show_figure(fig)
