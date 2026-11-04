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
