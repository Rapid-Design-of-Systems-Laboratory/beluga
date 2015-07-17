from beluga.visualization.renderers import Renderer

class MatPlotLibRenderer(Renderer):
    """
    A renderer class that implements matplotlib
    """
    def create_figure(self):
        """
        Creates a new figure and returns a handle
        """
        pass

    def add_line_plot(self,figure,x_data,y_data,x_label,y_label,title=None):
        """
        Adds a line plot using the given data to the specified figure
        """
        pass

    def add_sub_plot(self,figure,index,x_data,y_data,x_label,y_label,title=None):
        """
        Adds a subplot to the specified figure
        """
        pass
