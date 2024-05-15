# minimizing a thing within a bound

import numpy as np

l = 0.1
n = 2


def f(b):
    return (100 - b) * n * (1 - np.exp(-l * b)) ** (n - 1) * l * np.exp(-l * b) - (1 - np.exp(-l * b)) ** n


def f2(b):
    sum1 = np.sum([k * (1 - np.exp(-l * b))**(k-1) * l *
                  np.exp(-l * b) for k in range(1, n+1)])
    sum2 = np.sum([(1 - np.exp(-l * b))**k for k in range(1, n+1)])

    return (100 - b) * (sum1 / n) - (sum2 / n)

def f3(b):
    return b - 5.6


def objective(x):
    return f(x) ** 2

def targets(bounds, batch_size):
    half_step = (bounds[1] - bounds[0]) / (batch_size * 2)
    return [bounds[0] + half_step * (1 + i * 2) for i in range(batch_size)]


iterations = 1000
batch_size = 100



bounds = [0, 100]

width = bounds[1] - bounds[0]

for i in range(iterations):
    points = targets(bounds, batch_size)
    lowest_point = points[np.argmin(
        [objective(b) for b in targets(bounds, batch_size)])]
    new_range = (iterations - i) / (2 * width)
    bounds = [lowest_point - new_range, lowest_point + new_range]

    print(lowest_point, end="\r")

print(lowest_point)
