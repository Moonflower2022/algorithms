import random
from math import gcd
from generator import generate_prime
from power_algorithm import power_modulus

def generate_coprime(n):
    ret = random.randint(3, n - 1)
    while gcd(ret, n) != 1:
        ret = random.randint(3, n - 1)

    return ret

def extended_gcd(a, b):
    # Initialize variables
    x0, y0 = 0, 1  # Coefficients for the initial pair
    x1, y1 = 1, 0  # Coefficients for the next pair
    
    while a != 0:
        # Perform integer division and find remainder
        quotient, remainder = divmod(b, a)
        
        # Update coefficients using the current quotient
        new_x = x0 - quotient * x1
        new_y = y0 - quotient * y1
        
        # Update variables for the next iteration
        b, a = a, remainder
        x0, y0, x1, y1 = x1, y1, new_x, new_y
    
    # Return the final coefficients
    return x0, y0

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return x, y

p = generate_prime(2 ** 49, 2 ** 50, 20)
print("p:", p)
q = generate_prime(2 ** 50, 2 ** 51, 20)
print("q:", q)

n = p * q
print("n:", n)
totient_n = int((p - 1) * (q - 1) / gcd(p - 1, q - 1)) # assuming p and q are positive
print("totient_n:", totient_n)

e = generate_coprime(totient_n) # 2 ** 16 + 1
print("e:", e)

print("gcd(totient_n, e):", gcd(totient_n, e))

# d * e - k * totient_n = gcd(totient_n, e)

d, _ = egcd(e, totient_n)
print("d:", d)

plain_text = "hi my name is harrison!!!!! :)"
print("plain_text:", plain_text)


print("power_modulus(4, e*d % totient_n, n):", power_modulus(4, e*d % totient_n, n))
