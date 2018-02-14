from beluga.visualization.renderers import BaseRenderer
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
        has_legend = False
        num_lines = sum(1 for line in p.plot_data for d in line['data'] )
        if p.colormap is not None:
            cm_subsection = np.linspace(0.0, 1.0, num_lines)
            colors = [ p.colormap(x) for x in cm_subsection ]
        else:
            colors = [None]*num_lines

        i = 0
        ax3d = None
        for line in p.plot_data:
            has_legend = has_legend or (line['label'] is not None)
            override_color = None
            if isinstance(line['style'], dict):
                override_color = line['style'].pop('color', None)

            if line['type'] == 'line3d':
                fig = self._get_figure(f)
                if ax3d is None:
                    ax3d = fig.add_subplot(111, projection='3d')

            for dataset in line['data']:
                # Allow overriding colormap fom style vector
                if override_color is not None:
                    line_color = override_color
                else:
                    line_color = colors[i]

                if line['type'] == 'line3d':
                    if(len(dataset['x_data'])!=len(dataset['y_data'])):
                        continue

                    if isinstance(line['style'], str):
                        ax3d.plot3D(dataset['x_data'],dataset['y_data'],dataset['z_data'],line['style'],label=line['label'],figure=fh, color=line_color,)
                    elif isinstance(line['style'], dict):
                        ax3d.plot3D(dataset['x_data'],dataset['y_data'],dataset['z_data'],label=line['label'],figure=fh, color=line_color,**line['style'])
                else:
                    if(len(dataset['x_data'])!=len(dataset['y_data'])):
                        continue

                    if isinstance(line['style'], str):
                        plot(dataset['x_data'],dataset['y_data'],line['style'],label=line['label'],figure=fh, color=line_color,)
                    elif isinstance(line['style'], dict):
                        plot(dataset['x_data'],dataset['y_data'],label=line['label'],figure=fh, color=line_color,**line['style'])
                i += 1
        if has_legend:
            fh.gca().legend()
        if p._xlabel is not None:
            xlabel(p._xlabel,figure=fh)
        if p._ylabel is not None:
            ylabel(p._ylabel,figure=fh)
        if p._title is not None:
            title(p._title,figure=fh)
        grid(True)

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
