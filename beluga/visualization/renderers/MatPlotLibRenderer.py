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

    def plot(self,f,x_data,y_data,x_label,y_label,title_txt=None):
        """
        Adds a line plot using the given data to the specified figure
        """
        fh = self._get_figure(f);
        plot(x_data,y_data,figure=fh)
        xlabel(x_label,figure=fh)
        ylabel(y_label,figure=fh)
        title(title_txt,figure=fh)

    def subplot(self,f,index,x_data,y_data,x_label,y_label,title=None):
        """
        Adds a subplot to the specified figure
        """
        pass

if __name__ == '__main__':
    r = MatPlotLibRenderer()
    f = r.create_figure();
    print(f)
    r.plot(f,range(10),range(10),'x','y','blahahaa')
    r.show_figure(f)
