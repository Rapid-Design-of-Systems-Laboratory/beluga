import dill
import matplotlib.pyplot as plt

class BelugaPlot2:
    # def __init__(self):
    #     pass

    @staticmethod
    def load_dill(name='data.dill'):
        with open('./' + name + '.dill', 'rb') as f:
            out = dill.load(f)
        return out

    @staticmethod
    def retrieve(var, out, step=-1, sol=-1):
        data = out['problem_data']
        sol = out['solution'][step][sol]

        sol.prepare(data)

        x = sol.evaluate(var)
        return x

    @staticmethod
    def decorate(ax, x=None, y=None,
                     xaxis=None, yaxis=None, axis=None,
                     title=None, xlabel=None, ylabel=None, grid_on=True):

        ax.set_title(title)

        if xlabel is None:
            ax.set_xlabel(x)
        else:
            ax.set_xlabel(xlabel)

        if ylabel is None:
            ax.set_ylabel(y)
        else:
            ax.set_ylabel(ylabel)

        if axis is not None:
            ax.axis(axis)
        elif xaxis is not None:
            ax.xlim(xaxis)
        elif yaxis is not None:
            ax.ylim(yaxis)

        ax.grid(grid_on)

    def ez_plot_dill(self, x=None, y=None, file='data', step=-1, sol=-1,
                     ax=None, color='Blue',
                     xaxis=None, yaxis=None, axis=None,
                     title=None, xlabel=None, ylabel=None, grid_on=True):

        out = self.load_dill(file)

        x_num = self.retrieve(x, out, step, sol)
        y_num = self.retrieve(y, out, step, sol)

        if title is None:
            title = y + ' vs. ' + x

        if ax is None:
            fig = plt.figure(title)
            ax = plt.gca()

        ax.plot(x_num, y_num, color=color)

        self.decorate(ax, x, y, xaxis, yaxis, axis, title, xlabel, ylabel, grid_on)

        return ax

    def plot_cont_step(self, x=None, y=None, file='data', step=-1, sols='all',
                       ax=None, colormap='Set1',
                       xaxis=None, yaxis=None, axis=None,
                       title=None, xlabel=None, ylabel=None, grid_on=True):

        out = self.load_dill(file)

        if sols == 'all':
            num_sol = len(out['solution'][step])
            sols = range(0,num_sol)
        else:
            num_sol = len(sols)


        if title is None:
            title = y + ' vs. ' + x

        if ax is None:
            fig = plt.figure(title)
            ax = plt.gca()

        for sol, n in zip(sols, range(0,num_sol)):
            x_num = self.retrieve(x, out, step, sol)
            y_num = self.retrieve(y, out, step, sol)
            ax.plot(x_num, y_num, color=plt.cm.get_cmap(colormap)(n/(num_sol-1)))

        self.decorate(ax, x, y, xaxis, yaxis, axis, title, xlabel, ylabel, grid_on)

        return ax
