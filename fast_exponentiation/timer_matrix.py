from implementations import *
from numpy.linalg import matrix_power
from scipy.linalg import fractional_matrix_power
from sympy import Matrix
from decimal import getcontext
import torch
import numpy as np
import timeit

# TODO: more sanity checks with https://www.calculator.net/matrix-calculator.html


def evaluate(exp_funciton, base, exponent, iterations):
    total_time = timeit.timeit(lambda: exp_funciton(base, exponent), number=iterations)
    return total_time


getcontext().prec = 100000

if __name__ == "__main__":
    functions = [
        fast_matrix_pow,
        matrix_power,
        fractional_matrix_power,
        # jax_matrix_power,
        iterative_matrix_pow,
    ]

    base_array = [[1, 1], [1, 0]]

    M = np.matrix(base_array, dtype=Decimal)
    exponent = 2000
    iterations = 20000

    print(f"correct: {iterative_matrix_pow(M, exponent)}")

    for function in functions:
        print(f"{function.__name__}: {evaluate(function, M, exponent, iterations)}")
        print(function(M, exponent)[1, 0])

    # print(f"sympy with base_matrix_pow: {evaluate(base_matrix_pow, Matrix(base_array), exponent, iterations)}")
    # print(f"torch: {evaluate(torch_matrix_pow, torch.tensor(base_array, dtype=torch.float32).to(device), exponent, iterations)}")
