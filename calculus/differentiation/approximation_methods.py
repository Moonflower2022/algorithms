def f(x):
    return x ** 2 + x + 1

def derivative_f(x):
    return 2 * x + 1

# this (below) is a commonly used one

# examples:
# 1d: https://www.desmos.com/calculator/f7tinwmsne  

def central_differentation_approximation(function, x, epsilon=1e-8):
    return (function(x + epsilon) - function(x - epsilon)) / (2 * epsilon)

# most traditional one, especially in the limit definition of a derivative

def forward_differentiation_approximation(function, x, epsilon=1e-8):
    return (function(x + epsilon) - function(x)) / epsilon

# also a backward one, too lazy to write it