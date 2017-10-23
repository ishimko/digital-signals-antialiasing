from collections import namedtuple

from draw import draw_plots
from signal import fourier_spectrum, \
    fourth_degree_parabola_antialiasing, \
    moving_averaged_antialiasing, \
    moving_median_antialiasing, \
    random_signal

PlotDescription = namedtuple('PlotDescription', ['values', 'label', 'visibility'])

N = 512
SIGNALS_LABELS = [
    'Original',
    'Moving averaged',
    'Fourth degree parabola',
    'Moving median'
]
AVERAGED_WINDOW = 3
MEDIAN_WINDOW = 5
B1 = 5
B2 = 8


if __name__ == '__main__':
    random_signal_values = [random_signal(i, N, B1, B2) for i in range(N)]
    signals = [
        PlotDescription(
            values=random_signal_values,
            label='Original',
            visibility=True
        ),
        PlotDescription(
            values=moving_averaged_antialiasing(random_signal_values, AVERAGED_WINDOW),
            label='Moving averaged',
            visibility=False
        ),
        PlotDescription(
            values=fourth_degree_parabola_antialiasing(random_signal_values),
            label='Fourth degree parabola',
            visibility=False
        ),
        PlotDescription(
            values=moving_median_antialiasing(random_signal_values, MEDIAN_WINDOW),
            label='Moving median',
            visibility=False
        )
    ]
    draw_plots(signals)
