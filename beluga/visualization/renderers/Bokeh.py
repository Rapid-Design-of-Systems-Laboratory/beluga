from beluga.visualization.renderers import BaseRenderer
from bokeh.plotting import *
from bokeh.palettes import *
from bokeh.models import HoverTool

import webbrowser

class Bokeh(BaseRenderer):
    def __init__(self, filename='plot.html'):
        self._figures = []
        self.filename = filename
        output_file(filename, title="beluga Output")


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

    def create_figure(self, width=600, height=600):
        """
        Creates a new figure and returns a handle (index into array)
        """
        self._figures.append(figure(width=width, height=height))
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
        show(self._get_figure(f))

    def show_all(self):
        """
        Show all rendered figures
        """
        p = vplot(*self._figures)
        show(p)
        # for f in self._figures:
        #
        #     show(f)
        webbrowser.open(self.filename, new=2, autoraise=True)

    def render_plot(self,f,p):
        """
        Adds a line plot using the given data to the specified figure
        """
        plot = self._get_figure(f);

        for line in p.plot_data:
            dataset = [(data['x_data'],data['y_data']) for data in line['data']]
            xlist, ylist = zip(*dataset)
            if len(dataset) < 5:
                mypalette=Spectral4[0:len(dataset)]
            else:
                mypalette=Spectral10[0:len(dataset)]
            plot.multi_line(xs=xlist, ys=ylist, line_color=mypalette)

        # NOT WORKING!
        # if p._xlabel is not None and p._ylabel is not None:
        #     hover = HoverTool(
        #         tooltips=[
        #             (p._xlabel+":", "$x"),
        #             (p._ylabel+":", "$y"),
        #         ]
        #     )
        # else:
        #     hover = HoverTool(
        #         tooltips=[
        #             ("($x, $y)")
        #         ]
        #     )
        # plot.add_tools(hover)

        if p._xlabel is not None:
            plot.xaxis.axis_label = p._xlabel
        if p._ylabel is not None:
            plot.yaxis.axis_label = p._ylabel
        if p._title is not None:
            plot.title = p._title

    def render_subplot(self,f,index,plot):
        """
        Adds a subplot to the specified figure
        """
        pass

if __name__ == '__main__':
    from beluga.visualization.elements import Plot
    import dill

    r = Bokeh()
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
