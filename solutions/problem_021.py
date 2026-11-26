"""
Project Euler Problem 21: Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

URL: https://projecteuler.net/problem=21
"""


def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of proper divisors of n (all positive divisors excluding n itself).
    """
    if n <= 1:
        return 0

    total = 1
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            j = n // i
            if j != i:
                total += j
    return total


def find_amicable_numbers(limit: int = 10000) -> list[int]:
    """
    Find all amicable numbers strictly less than the given limit.
    """
    # Precompute proper divisor sums for numbers up to limit
    # We use a cache/memo for any values that might exceed limit
    cache: dict[int, int] = {}

    def get_d(x: int) -> int:
        if x not in cache:
            cache[x] = sum_proper_divisors(x)
        return cache[x]

    amicable: list[int] = []
    for a in range(2, limit):
        b = get_d(a)
        if b != a and get_d(b) == a:
            amicable.append(a)

    return amicable


def solve(limit: int = 10000) -> int:
    """
    Evaluate the sum of all amicable numbers under limit.
    """
    return sum(find_amicable_numbers(limit))


if __name__ == "__main__":
    result = solve(10000)
    print(f"Project Euler Problem 21 Answer: {result}")
