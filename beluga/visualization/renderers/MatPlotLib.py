from beluga.visualization.renderers import BaseRenderer
from matplotlib.pyplot import *
from beluga.utils import keyboard

class MatPlotLib(BaseRenderer):
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

    def show_all(self):
        """
        Show all rendered figures
        """
        show()

    def render_plot(self,f,p):
        """
        Adds a line plot using the given data to the specified figure
        """
        fh = self._get_figure(f);
        fh.hold(True)
        has_legend = False

        for line in p.plot_data:
<<<<<<< HEAD
            has_legend = has_legend or (line['label'] is not None)
            for dataset in line['data']:
                plot(dataset['x_data'],dataset['y_data'],label=line['label'],figure=fh)
=======
            has_legend = has_legend or (line['legend'] is not None)
            for dataset, ind in zip(line['data'], range(len(line['data']))):
                # Determine coloring
                if line['color'] is not None:
                    _color = line['color']
                elif line['type'] == 'line_series':
                    _color = cm.get_cmap('jet')(ind/(len(line['data'])-1))
                else: # use default color
                    _color = 'b'

                plot(dataset['x_data'],dataset['y_data'],label=line['legend'],figure=fh,color=_color)

>>>>>>> RDSL/master
        if has_legend:
            fh.gca().legend()
        if p._xlabel is not None:
            xlabel(p._xlabel,figure=fh)
        if p._ylabel is not None:
            ylabel(p._ylabel,figure=fh)
        if p._title is not None:
            title(p._title,figure=fh)
        if p._grid_on:
            fh.gca().grid(p._grid_on)
        if p._xlim is not None:
            fh.gca().set_xlim(p._xlim)
        if p._ylim is not None:
            fh.gca().set_ylim(p._ylim)

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
