import numpy as np
from jax.numpy.linalg import matrix_power
from decimal import Decimal
import torch


def fast_pow(a, b):
    state = (a, 1, b)
    while state[2] != 0:
        remainder = state[2] % 2
        if remainder == 0:
            state = (state[0] ** 2, state[1], state[2] / 2)
        elif remainder == 1:
            state = (state[0] ** 2, state[1] * state[0], (state[2] - 1) / 2)
    return state[1]


def fast_matrix_pow(M, exponent):
    state = (M, 1, exponent)
    while state[2] != 0:
        remainder = state[2] % 2
        if remainder == 0:
            state = (state[0] ** 2, state[1], state[2] / 2)
        elif remainder == 1:
            state = (state[0] ** 2, state[1] * state[0], (state[2] - 1) / 2)
    return state[1]


def base_matrix_pow(M, exponent):
    return M**exponent


def iterative_matrix_pow(M, exponent):
    if exponent == 0:
        return np.matrix([[1, 0], [0, 1]], dtype=Decimal)
    result = M
    for _ in range(exponent - 1):
        result = result @ M
    return result


def jax_matrix_power(M, exponent):
    return matrix_power(M, exponent)


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available() else "cpu"
)


def torch_matrix_pow(M, exponent):
    result = M
    for _ in range(exponent - 1):
        result = torch.mm(result, M)
    return result


# only works on natural numbers a, b

if __name__ == "__main__":
    print("fast_pow(0, 0):", fast_pow(0, 0))
    print("fast_pow(5, 4):", fast_pow(5, 4))
