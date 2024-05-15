# finds one solution to one variable equations in the form of f(x) = 0
# if there are overflow/convergence problems change the starting point
# gradient descent method

import autograd.numpy as np
from autograd import elementwise_grad
import math

l = 0.1
n = 3

def f(x):
    return (100 - x) * n * (1 - np.exp(-l * x)) ** (n - 1) * l * np.exp(-l * x) - (1 - np.exp(-l * x)) ** n


def objective(x):
    return f(x) ** 2

gradient = elementwise_grad(objective)

point = np.array([30.])

iterations = 1000
learning_rate = 0.1

gradient_history = []

for i in range(iterations):
    new_gradient = gradient(point)
    gradient_history.append(new_gradient)
    point = point - learning_rate / math.sqrt(1e-8 + sum(g[0] ** 2 for g in gradient_history)) * new_gradient
    print(f"{i}/{iterations}: f[{point}] = {f(point)}", end="\r")
print("")
print("solution:", point)
print("f(x):", f(point))