"""
Project Euler Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

URL: https://projecteuler.net/problem=14
"""

def longest_collatz_sequence(limit: int = 1_000_000) -> int:
    """
    Finds the starting number strictly below limit that produces the longest Collatz chain.
    
    Optimizations:
    1. Direct indexing array cache for all values below limit.
    2. Bitwise parity check and shift (n & 1, n >> 1).
    3. Combined odd transition: for odd n, 3n + 1 is guaranteed even,
       so we advance 2 steps directly to (3n + 1) // 2.
    """
    if limit <= 1:
        return 0

    cache = [0] * limit
    cache[1] = 1

    max_len = 0
    best_start = 1

    for i in range(2, limit):
        n = i
        count = 0
        while n >= limit or cache[n] == 0:
            if n & 1:
                n = (3 * n + 1) >> 1
                count += 2
            else:
                n >>= 1
                count += 1

        total_length = count + cache[n]
        cache[i] = total_length

        if total_length > max_len:
            max_len = total_length
            best_start = i

    return best_start

def solve(limit: int = 1_000_000) -> int:
    """
    Solves Project Euler Problem 14 for starting numbers below limit.
    Default: limit = 1_000_000
    """
    return longest_collatz_sequence(limit)

if __name__ == "__main__":
    result = solve(1_000_000)
    print(f"Project Euler Problem 14 Answer: {result}")
