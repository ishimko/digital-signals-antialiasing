
from random import choice
from math import sin, pi

def test_signal(harmonic_index, N, B1, B2):
    assert B1 > B2

    def sine(i, j=1):
        return sin((2 * pi * i * j) / N)

    return B1 * sine(harmonic_index) + sum(B2 * choice([-1, 1]) * sine(harmonic_index, j) for j in range(50, 71))
