from matplotlib import pyplot as plt
from matplotlib.widgets import CheckButtons


def plot_values(signal_values):
    return zip(*enumerate(signal_values))


def draw_plots(signals_descriptions):
    def on_click(label):
        plot = plots[label]
        plot.set_visible(not plot.get_visible())
        fig.canvas.draw()
    plots = {}
    plt.subplots_adjust(bottom=0.25)
    fig = plt.figure(1)
    plt.subplots_adjust(left=0.2)
    for signal_values, signal_label, visibility in signals_descriptions:
        x_points, y_points = plot_values(signal_values)
        line, = plt.plot(x_points, y_points)
        plots[signal_label] = line
    checkboxes_axes = plt.axes([0.05, 0.4, 0.12, 0.15])
    checkboxes = CheckButtons(
        checkboxes_axes,
        [x.label for x in signals_descriptions],
        [x.visibility for x in signals_descriptions]
    )
    checkboxes.on_clicked(on_click)
    plt.figlegend(list(plots.values()), [x.label for x in signals_descriptions], loc='lower center')
    # need to hide after figlegend to use real colors for legend
    for _, label, visibility in signals_descriptions:
        plots[label].set_visible(visibility)
    plt.show()
