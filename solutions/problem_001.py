"""
Project Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

URL: https://projecteuler.net/problem=1
"""

def sum_multiples_below(limit: int, k: int) -> int:
    """
    Computes sum of multiples of k below limit using the arithmetic progression formula:
    S = k * (m * (m + 1)) // 2, where m = (limit - 1) // k.
    Runs in O(1) constant time.
    """
    m = (limit - 1) // k
    return k * m * (m + 1) // 2

def solve(limit: int = 1000) -> int:
    """
    Using the Principle of Inclusion-Exclusion:
    Sum = S(3) + S(5) - S(15)
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return (
        sum_multiples_below(limit, 3)
        + sum_multiples_below(limit, 5)
        - sum_multiples_below(limit, 15)
    )

if __name__ == "__main__":
    result = solve(1000)
    print(f"Project Euler Problem 1 Answer: {result}")

