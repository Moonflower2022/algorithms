import autograd.numpy as np
from autograd import grad

np.random.seed(42)
matrix = np.random.rand(10, 10)
vector = np.random.rand(10)

# R^10 -> R
def objective(x):
    return sum(np.dot(matrix, x) + vector) ** 2

gradient = grad(objective)

current_point = np.zeros(10)

tolerance = 0.00000000000000001

# learning_rate = 0.001
learning_rate_options = [1 / (2 ** i) for i in range(10)]
iterations = 0

while objective(current_point) > tolerance:
    iterations += 1
    # current_point -= gradient(current_point) * learning_rate

    learning_rate_results = [objective(current_point - gradient(current_point) * learning_rate) for learning_rate in learning_rate_options]
    current_point -= gradient(current_point) * learning_rate_options[np.argmin(learning_rate_results)]


print("solution:", current_point)
print("objective(solution):", objective(current_point))
print("iterations:", iterations)