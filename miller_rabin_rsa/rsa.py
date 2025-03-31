import random
from math import gcd
from generator import generate_prime
from power_algorithm import power_modulus


def generate_coprime(n):
    ret = random.randint(3, n - 1)
    while gcd(ret, n) != 1:
        ret = random.randint(3, n - 1)

    return ret


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


def str_to_int(plain_text):
    return int.from_bytes(plain_text.encode(), "big")


def int_to_str(num):
    return num.to_bytes((num.bit_length() + 7) // 8, "big").decode()


def main():
    p = generate_prime(2**255, 2**256)
    print("p:", p)
    q = generate_prime(2**256, 2**257)
    print("q:", q)

    n = p * q
    print("n:", n)
    totient_n = int(
        (p - 1) * (q - 1) // gcd(p - 1, q - 1)
    )  # assuming p and q are positive
    print("totient_n:", totient_n)

    e = generate_coprime(totient_n)  # 2 ** 16 + 1
    print("e:", e)

    print("gcd(totient_n, e):", gcd(totient_n, e))

    d = modinv(e, totient_n)
    print("d:", d)

    print("de % totient_n:", (d * e) % totient_n)

    plain_text = "hi my name is harrison!!!!! :)"
    print("plain_text:", plain_text)

    hashed = str_to_int(plain_text)
    print("hashed:", hashed)

    encrypted = power_modulus(hashed, e, n)
    print("encrypted = hashed ^ e % n:", encrypted)

    decrypted = power_modulus(encrypted, d, n)
    print("decrypted: encrypted ^ d % n:", decrypted)

    decoded = int_to_str(decrypted)
    print("decoded:", decoded)


if __name__ == "__main__":
    main()
