from functools import lru_cache
from decimal import Decimal
from scipy.linalg import fractional_matrix_power
import math
import numpy as np

# TODO:
# eigendecomposition (later)

@lru_cache(maxsize=None)
def memoized_recursive_optimized(n):
    if n > 3320:
        return 0
    if n > 2:
        return (
            memoized_recursive_optimized(n // 2 + 1)
            * memoized_recursive_optimized(n - n // 2)
            + memoized_recursive_optimized(n // 2)
            * memoized_recursive_optimized(n - n // 2 - 1)
        )
    return [0, 1, 1][n]

@lru_cache(maxsize=None)
def memoized_recursive(n):
    if n > 3320:
        return 0
    if n > 2:
        return memoized_recursive(n - 1) + memoized_recursive(n - 2)
    return [0, 1, 1][n]

def recursive(n):
    if n > 2:
        return recursive(n - 1) + recursive(n - 2)
    return [0, 1, 1][n]

def closed(n):
    if n > 1500:
        return 0

    phi = (1 + math.sqrt(5)) / 2
    
    if n > 40:
        return round((phi ** n) / math.sqrt(5))
    else:
        conjugate_phi = (1 - math.sqrt(5)) / 2
        return round((phi ** n - conjugate_phi ** n) / math.sqrt(5))

def closed_precise(n):
    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2

    # Binet's formula
    fib_n = (phi**n - psi**n) / sqrt5

    return round(fib_n)  # The result should be an integer

def iterative(n):
    if n <= 1:
        return n
    a, b = Decimal(0), Decimal(1)
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def matrix(n):
    fibonacci_matrix = np.matrix([[1, 1], [1, 0]], dtype=Decimal) # instead of Decimal, can also used dtype=object for some reason
    final_matrix = fractional_matrix_power(fibonacci_matrix, n)
    return int(final_matrix[1, 0])