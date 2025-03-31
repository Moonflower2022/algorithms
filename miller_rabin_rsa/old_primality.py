def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n ** (1/2)) + 1
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

if __name__ == '__main__':
    number = 1603627217
    print(f"is_prime({number}): {is_prime(number)}")