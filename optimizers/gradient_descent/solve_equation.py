# finds one solution to one variable equations in the form of f(x) = 0
# if there are overflow/convergence problems change the starting point

import autograd.numpy as np
from autograd import elementwise_grad

l = 0.1
n = 3

def f(x):
    return (100 - x) * n * (1 - np.exp(-l * x)) ** (n - 1) * l * np.exp(-l * x) - (1 - np.exp(-l * x)) ** n


def objective(x):
    return f(x) ** 2

gradient = elementwise_grad(objective)

point = np.array([30.])

iterations = 100000
learning_rate = 0.001


for i in range(iterations):
    point = point - learning_rate * gradient(point)

print("solution:", point)
print("error; f(x)^2:", objective(point))
print("f(x):", f(point))