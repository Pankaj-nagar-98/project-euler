"""
Project Euler Problem 20: Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1.
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""
import math

def factorial_digit_sum(n: int = 100) -> int:
    fact = math.factorial(n)
    return sum(int(digit) for digit in str(fact))

def solve() -> int:
    return factorial_digit_sum(100)

if __name__ == "__main__":
    result = solve()
    print(f"The sum of the digits in the number 100! is: {result}")
