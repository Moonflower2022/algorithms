# based on https://en.wikipedia.org/wiki/Aberth_method

import autograd.numpy as np
from autograd.differential_operators import elementwise_grad as egrad

def polynomial(x):
    return np.power(x, 5) + 4 * np.power(x, 4) - 10 * np.power(x, 3) + 1

polynomial_desc = "x^{5}+4x^{4}-10x^{3}+1"
degree = 5

derivative = egrad(polynomial)

def offsets(x):
    top = polynomial(x)/derivative(x)
    bottom = 1 - polynomial(x)/derivative(x) * np.array([sum(1/(element - other_element) for other_element in np.delete(x, x == element)) for element in x])
    return top/bottom

approximations = np.random.uniform(-10, 10, degree)
iterations = 1000

for i in range(iterations):
    approximations -= offsets(approximations)

print("approximations:", approximations)
print("polynomial(approximations):", polynomial(approximations))