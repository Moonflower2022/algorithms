import pandas as pd
import random
from math import isqrt, gcd

# def generate_prime():
    

# def miller_rabin(n,  ):
#     a = generate_coprime(n)

def miller_rabin1(n, s):
    if n == 1 or n == 4:
        return False
    if n < 4:
        return n > 1
    for _ in range(s):
        a = random.randint(1, n - 1)
        if a ** (n - 1) % n == 1:
            return False
    return True


def generate_coprime(n):
    coprime = random.randint(2, n - 1)
    while gcd(n, coprime) != 1:
        coprime = random.randint(2, n - 1)

    return coprime
    
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

count = 20

miller_rabin_tested = [miller_rabin1(i, 5) for i in range(count)]
normal_tested = [is_prime(i) for i in range(count)]

# Create a DataFrame from the arrays
df = pd.DataFrame({'i': [i for i in range(count)], 'normal_test': normal_tested, 'miller_rabin_test': miller_rabin_tested})

# Display the DataFrame
print(df)