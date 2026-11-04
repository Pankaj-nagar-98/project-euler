"""
Project Euler Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

URL: https://projecteuler.net/problem=3
"""
import sys
from pathlib import Path

# Support running directly
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.primes import prime_factors

def largest_prime_factor(n: int) -> int:
    """
    Finds the largest prime factor of n by repeated trial division.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    # Using the optimized wheel factorization utility
    factors = prime_factors(n)
    return factors[-1] if factors else n

def solve(n: int = 600851475143) -> int:
    return largest_prime_factor(n)

if __name__ == "__main__":
    result = solve(600851475143)
    print(f"Project Euler Problem 3 Answer: {result}")
