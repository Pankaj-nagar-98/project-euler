"""
Project Euler Problem 17: Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

URL: https://projecteuler.net/problem=17
"""

ONES: dict[int, str] = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
}

TENS: dict[int, str] = {
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety",
}

def number_to_words(n: int) -> str:
    """
    Converts an integer n (1 <= n <= 1000) into British English words
    without spaces or hyphens.
    """
    if n == 1000:
        return "onethousand"

    words = ""
    hundreds = n // 100
    remainder = n % 100

    if hundreds > 0:
        words += ONES[hundreds] + "hundred"
        if remainder > 0:
            words += "and"

    if remainder > 0:
        if remainder < 20:
            words += ONES[remainder]
        else:
            words += TENS[remainder // 10]
            if remainder % 10 > 0:
                words += ONES[remainder % 10]

    return words

def number_letter_counts(limit: int = 1000) -> int:
    """
    Computes total letters used to write numbers from 1 to limit inclusive.
    Time Complexity: O(limit)
    Space Complexity: O(1)
    """
    return sum(len(number_to_words(i)) for i in range(1, limit + 1))

def solve(limit: int = 1000) -> int:
    """
    Solves Project Euler Problem 17.
    Default: limit = 1000
    """
    return number_letter_counts(limit)

if __name__ == "__main__":
    result = solve(1000)
    print(f"Project Euler Problem 17 Answer: {result}")
