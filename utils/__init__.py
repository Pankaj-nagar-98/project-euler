"""
Project Euler utility functions and helpers.
"""
from .timing import benchmark
from .primes import is_prime, prime_factors

__all__ = ["benchmark", "is_prime", "prime_factors"]
