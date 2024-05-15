import autograd.numpy as np
from autograd.differential_operators import elementwise_grad as egrad

def f(x):
    return np.sin(x) + 1 + x - np.power(x, 2)
func_desc = r"\sin(x)+1+x-x^{2}"

derivative = egrad(f)

def offsets(x):
    top = f(x)/derivative(x)
    bottom = 1 - f(x)/derivative(x) * np.array([sum(1/(element - other_element) for other_element in np.delete(x, x == element)) for element in x])
    return top/bottom

num_roots = 2
assert num_roots > 1 # doesnt work for n = 1, use something else for that case
approximations = np.random.uniform(-10, 10, num_roots)
iterations = 1000

for i in range(iterations):
    print(approximations)
    approximations -= offsets(approximations)

print("approximations:", approximations)
print("f(approximations):", f(approximations))