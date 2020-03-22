def primes(limit):
    """
    Create a boolean array "prime[0..n]" and initialize
    all entries it as true. A value in prime[i] will
    finally be false if i is Not a prime, else true.
    """
    prime = [True for i in range(limit + 1)]

    prime[0] = False
    prime[1] = False
    p = 2

    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p] is True:

            # Update all multiples of p
            for i in range(p * 2, limit + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    return [x for x in range(limit + 1) if prime[x]]
