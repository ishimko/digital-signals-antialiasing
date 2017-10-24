from collections import namedtuple

from draw import draw_plots
from antialiasing import fourth_degree_parabola_antialiasing, moving_averaged_antialiasing, moving_median_antialiasing
from signal import test_signal
from fourier import amplitude_spectrum

PlotDescription = namedtuple('PlotDescription', ['values', 'label', 'visibility', 'spectrum'])

N = 512
SIGNALS_LABELS = [
    'Original',
    'Moving averaged',
    'Fourth degree parabola',
    'Moving median'
]
AVERAGED_WINDOW = 7
MEDIAN_WINDOW = 30
REMOVING_ELEMENTS = 3
B1 = 100
B2 = 2


if __name__ == '__main__':
    random_signal_values = [test_signal(i, N, B1, B2) for i in range(N)]
    moving_averaged_values = moving_averaged_antialiasing(random_signal_values, AVERAGED_WINDOW)
    parabola_values = fourth_degree_parabola_antialiasing(random_signal_values)
    moving_median_values = moving_median_antialiasing(random_signal_values, MEDIAN_WINDOW, REMOVING_ELEMENTS)
    signals = [
        PlotDescription(
            values=random_signal_values,
            label='Original',
            visibility=True,
            spectrum = amplitude_spectrum(random_signal_values)
        ),
        PlotDescription(
            values=moving_averaged_values,
            label='Moving averaged',
            visibility=False,
            spectrum=amplitude_spectrum(moving_averaged_values)
        ),
        PlotDescription(
            values=parabola_values,
            label='Fourth degree parabola',
            visibility=False,
            spectrum=amplitude_spectrum(parabola_values)
        ),
        PlotDescription(
            values=moving_median_values,
            label='Moving median',
            visibility=False,
            spectrum=amplitude_spectrum(moving_median_values)
        )
    ]
    draw_plots(signals)
