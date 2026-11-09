"""
Project Euler Problem 8: Largest Product in a Series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

URL: https://projecteuler.net/problem=8
"""

import math

THOUSAND_DIGIT_NUMBER = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

def largest_product_in_series(series: str, k: int = 13) -> int:
    """
    Finds the greatest product of k adjacent digits in the numeric string series.
    Optimized by skipping sub-windows containing '0'.
    """
    if k <= 0 or k > len(series):
        return 0

    max_product = 0
    # Split into consecutive non-zero chunks since any zero in the window yields product 0
    for chunk in series.split("0"):
        if len(chunk) < k:
            continue
        digits = [int(ch) for ch in chunk]
        
        # Initial window product
        current_product = math.prod(digits[:k])
        if current_product > max_product:
            max_product = current_product
            
        # Slide window
        for i in range(k, len(digits)):
            # Update product by dividing outgoing digit and multiplying incoming
            # Note: digits are guaranteed non-zero inside each chunk
            current_product = (current_product // digits[i - k]) * digits[i]
            if current_product > max_product:
                max_product = current_product

    return max_product

def solve(n: int = 13) -> int:
    """
    Solves Project Euler Problem 8 for n adjacent digits.
    Default: n = 13
    """
    return largest_product_in_series(THOUSAND_DIGIT_NUMBER, n)

if __name__ == "__main__":
    result = solve(13)
    print(f"Project Euler Problem 8 Answer: {result}")
