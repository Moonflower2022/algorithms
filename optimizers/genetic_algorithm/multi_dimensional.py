import numpy as np

def mutate(x):
    return x + (np.random.random(x.shape) - 0.5)

def reproduce(x, n):
    return [mutate(x) for _ in range(n)]

def naturally_select(points, top_n):
    evaluations = [(point, objective(point)) for point in points]

    sorted_points = sorted(evaluations, key=lambda pair: pair[1])[:top_n]
    
    return [pair[0] for pair in sorted_points]

def get_best(points):
    return points[np.argmin([objective(point) for point in points])]

np.random.seed(42)
matrix = np.random.rand(10, 10)
vector = np.random.rand(10)

# R^10 -> R
def objective(x):
    return sum(np.dot(matrix, x) + vector) ** 2

points = reproduce(np.zeros(10), 200)
best_point = get_best(points)

tolerance = 0.00001
iterations = 0

while objective(best_point) > tolerance:
    iterations += 1
    points = naturally_select(points, 20)
    points = [offspring for point in points for offspring in reproduce(point, 20)]
    best_point = get_best(points)
    print(objective(best_point))

print("solution:", best_point)
print("objective(solution):", objective(best_point))
print("iterations:", iterations)