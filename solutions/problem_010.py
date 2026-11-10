"""
Project Euler Problem 10: Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

URL: https://projecteuler.net/problem=10
"""
import sys
from pathlib import Path

# Support running directly
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.primes import sum_primes_below

def solve(limit: int = 2_000_000) -> int:
    """
    Computes the sum of all prime numbers strictly below limit
    using an odd-only Sieve of Eratosthenes.

    Time Complexity: O(limit * log(log(limit)))
    Space Complexity: O(limit) bits/bytes
    """
    return sum_primes_below(limit)

if __name__ == "__main__":
    result = solve(2_000_000)
    print(f"Project Euler Problem 10 Answer: {result}")
