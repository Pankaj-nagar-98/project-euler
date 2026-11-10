"""
Prime number utilities and factorization algorithms.
"""
from typing import List

def is_prime(n: int) -> bool:
    """Checks whether an integer n is prime in O(sqrt(n)) time."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # 6k +/- 1 wheel optimization
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True

def prime_factors(n: int) -> List[int]:
    """Returns all prime factors of n in ascending order."""
    factors: List[int] = []
    
    # Extract factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # Extract factor 3
    while n % 3 == 0:
        factors.append(3)
        n //= 3

    # 6k +/- 1 wheel factorization
    d = 5
    step = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += step
            step = 6 - step  # Alternates between 2 and 4

    if n > 1:
        factors.append(n)
        
    return factors

def sieve_primes(limit: int) -> List[int]:
    """
    Generates all primes strictly below limit using an odd-only Sieve of Eratosthenes.
    Time Complexity: O(limit * log(log(limit)))
    Space Complexity: O(limit)
    """
    if limit <= 2:
        return []
    size = limit // 2
    sieve = bytearray([1]) * size
    sieve[0] = 0  # 1 is not prime

    root = int(limit**0.5)
    for i in range(1, (root + 1) // 2):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            step = p
            num_steps = (size - 1 - start) // step + 1
            sieve[start:size:step] = b"\x00" * num_steps

    primes = [2]
    primes.extend(2 * i + 1 for i, is_p in enumerate(sieve) if is_p)
    return primes

def sum_primes_below(limit: int) -> int:
    """
    Computes the sum of all primes strictly below limit.
    Optimized for memory and speed with an odd-only bytearray sieve.
    """
    if limit <= 2:
        return 0
    if limit == 3:
        return 2

    size = limit // 2
    sieve = bytearray([1]) * size
    sieve[0] = 0

    root = int(limit**0.5)
    for i in range(1, (root + 1) // 2):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            step = p
            num_steps = (size - 1 - start) // step + 1
            sieve[start:size:step] = b"\x00" * num_steps

    return 2 + sum(2 * i + 1 for i, is_p in enumerate(sieve) if is_p)

