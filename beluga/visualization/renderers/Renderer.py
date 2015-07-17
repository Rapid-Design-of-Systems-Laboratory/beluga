import abc
class Renderer(object):
    # Define class as abstract class
    __metaclass__ = abc.ABCMeta

    # Define common interface for renderer classes
    @abc.abstractmethod
    def create_figure(self):
        """
        Creates a new figure and returns a handle
        """
    @abc.abstractmethod
    def add_line_plot(self,figure,x_data,y_data,x_label,y_label,title=None):
        """
        Adds a line plot using the given data to the specified figure
        """

    @abc.abstractmethod
    def add_sub_plot(self,figure,index,x_data,y_data,x_label,y_label,title=None):
        """
        Adds a subplot to the specified figure
        """

    # Configuration
    # Movie making interface
    # Method for saving plot to file (PDF/SVG/JPEG/PNG/HTML5)
