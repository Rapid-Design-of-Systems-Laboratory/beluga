from beluga.visualization.renderers import BaseRenderer

import toyplot.browser, toyplot.qt, toyplot.html, toyplot.pdf, toyplot.png, toyplot.svg
from toyplot import *

class ToyPlot(BaseRenderer):
    def __init__(self, backend = 'browser'):
        self._figures = []
        backend_list = {'browser': toyplot.browser,
                    'pdf': toyplot.pdf,
                    'png': toyplot.png,
                    'svg': toyplot.svg,
                    'html': toyplot.html}

        self.backend = backend_list[backend]
        self.fileext = '.'+backend

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
        Creates a new figure and returns a handle (index into array)
        """
        canvas = toyplot.Canvas(width=600, height=600)
        self._figures.append(canvas)
        return len(self._figures)-1

    def close_figure(self,f):
        """
        Closes a specified figure
        """
        pass
        # close(self._get_figure(f))

    def show_figure(self,f):
        """
        Shows a specified figure
        """
        if hasattr(self.backend, 'show'):
            self.backend.show(self._get_figure(f))
        else:
            filename = "figure_"+str(f+1)+self.fileext
            print('Saving to '+filename)
            self.backend.render(self._get_figure(f), filename)

    def show_all(self):
        """
        Show all rendered figures
        """
        for fh in range(len(self._figures)):
            self.show_figure(fh)

    def render_plot(self,f,p):
        """
        Adds a line plot using the given data to the specified figure
        """
        canvas = self._get_figure(f);
        axes = canvas.axes()

        label_style={"font-size":"14px", "font-weight":"bold"}
        tick_style={"font-size":"12px"}
        axes.x.label.style = label_style
        axes.y.label.style = label_style
        axes.x.ticks.labels.style = tick_style
        axes.y.ticks.labels.style = tick_style

        legends_data = []
        # has_legend = False
        for line in p.plot_data:
            # has_legend = has_legend or (line['label'] is not None)
            for dataset in line['data']:
                plt = axes.plot(dataset['x_data'], dataset['y_data'])
            # TODO: Legends for line_series may not work properly
            if line['label'] is not None:
                legends_data.append((line['label'],plt))
        # canvas.legend(legends_data);

        if p._xlabel is not None:
            axes.x.label.text = p._xlabel
        if p._ylabel is not None:
            axes.y.label.text = p._ylabel
        if p._title is not None:
            axes.label.text = p._title

    def render_subplot(self,f,index,plot):
        """
        Adds a subplot to the specified figure
        """
        pass

if __name__ == '__main__':
    from beluga.visualization.elements import Plot
    import dill

    r = ToyPlot()
    fig = r.create_figure()

    with open('/Users/tantony/dev/tantony-beluga/examples/planarHypersonic/phu_2k5_eps2.dill','rb') as f:
        out = dill.load(f)

    p = Plot(-1,-1)
    p.line('v/1000','h/1000')
    p.xlabel('v (km/s)')
    p.ylabel('h (km)')
    p.title('Altitude vs. Velocity')
    p.preprocess(out['solution'],out['problem_data'])

    r.render_plot(fig,p)
    r.show_figure(fig)

    fig = r.create_figure()
    p = Plot(-1,-1)
    p.line('theta*re/1000','h/1000')
    p.xlabel('downrange (km)')
    p.ylabel('altitude (km)')
    p.title('Altitude vs. Downrange')
    p.preprocess(out['solution'],out['problem_data'])
    r.render_plot(fig,p)
    r.show_figure(fig)
