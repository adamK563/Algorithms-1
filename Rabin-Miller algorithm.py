def rabin_miller(n):
    # Check if n is even or less than 2
    if n % 2 == 0 or n < 2:
        return False

    # Check if n is a power of 2
    if n & (n - 1) == 0:
        return False

    # Check if n is divisible by any prime numbers less than or equal to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # Check if n is a prime number using the Rabin-Miller algorithm
    s = n - 1
    while s % 2 == 0:
        s //= 2

    for i in range(10):
        a = random.randrange(1, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue

        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
