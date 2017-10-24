from statistics import mean

def moving_averaged_antialiasing(values, window):
    offset = (window - 1) // 2
    values_indicies = range(len(values))
    return [mean(values[i] for i in range(j - offset, j + offset) if i in values_indicies) for j in values_indicies]


def fourth_degree_parabola_antialiasing(values):
    mul = 1 / 2431
    values_range = range(len(values))
    get_or_zero = lambda i: values[i] if i in values_range else 0
    def antialiased(i):
        return mul * (110 * get_or_zero(i - 6)
                      -198 * get_or_zero(i - 5)
                      -135 * get_or_zero(i - 4)
                      +110 * get_or_zero(i - 3)
                      +390 * get_or_zero(i - 2)
                      +600 * get_or_zero(i - 1)
                      +677 * get_or_zero(i)
                      +600 * get_or_zero(i + 1)
                      +390 * get_or_zero(i + 2)
                      +110 * get_or_zero(i + 3)
                      -135 * get_or_zero(i + 4)
                      -198 * get_or_zero(i + 5)
                      +110 * get_or_zero(i + 6))

    return [antialiased(i) for i in values_range]


def moving_median_antialiasing(values, window, removing_elements):
    assert removing_elements < window
    offset = (window - 1) // 2
    values_range = range(len(values))

    def antialiased(i):
        window_values = [values[j] for j in range(i - offset, i + offset) if j in values_range]
        window_values = sorted(window_values[removing_elements:-removing_elements])
        return mean(window_values) if window_values else 0

    return [antialiased(i) for i in values_range]
