"""
Project Euler Problem 16: Power Digit Sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def power_digit_sum(base: int = 2, exponent: int = 1000) -> int:
    num = base ** exponent
    return sum(int(digit) for digit in str(num))

def solve() -> int:
    return power_digit_sum(2, 1000)

if __name__ == "__main__":
    result = solve()
    print(f"The sum of the digits of 2^1000 is: {result}")
