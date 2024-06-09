import random
from math import gcd
from power_algorithm import power_modulus

def generate_coprime(n):
    coprime = random.randint(2, n - 2)
    while gcd(n, coprime) != 1:
        coprime = random.randint(2, n - 2)

    return coprime

def miller_rabin(n, tests):
    if n == 1 or n == 4:
        return False
    if n < 4:
        return n > 1

    for _ in range(tests):
        a = generate_coprime(n)
        if power_modulus(a, n - 1, n) != 1:
            return False
    return True

if __name__ == '__main__':
    print(miller_rabin(7708429831, 20))