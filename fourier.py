from math import sin, cos, pi, hypot, atan2

def cosine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * cos(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def sine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * sin(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def fourier_transformation(signal_values, harmonic_index, N):
    cosine = cosine_amplitude(signal_values, harmonic_index, N)
    sine = sine_amplitude(signal_values, harmonic_index, N)
    return hypot(sine, cosine)


def amplitude_spectrum(signal_values):
    N = len(signal_values)
    return [fourier_transformation(signal_values, j, N) for j in range(N // 2)]
