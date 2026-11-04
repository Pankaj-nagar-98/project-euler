"""
Project Euler Problem 9: Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def special_pythagorean_triplet(target_sum: int = 1000):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if a * a + b * b == c * c:
                return a, b, c, a * b * c
    return None

def solve() -> int:
    triplet = special_pythagorean_triplet(1000)
    return triplet[3] if triplet else 0

if __name__ == "__main__":
    triplet = special_pythagorean_triplet(1000)
    if triplet:
        a, b, c, product = triplet
        print(f"Found triplet: a = {a}, b = {b}, c = {c}")
        print(f"Check sum: {a} + {b} + {c} = {a + b + c}")
        print(f"Product abc: {product}")
