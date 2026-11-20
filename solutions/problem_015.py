"""
Project Euler Problem 15: Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

URL: https://projecteuler.net/problem=15
"""

import math

def count_lattice_paths(width: int = 20, height: int = 20) -> int:
    """
    Computes the number of unique paths on a width x height grid
    from top-left (0, 0) to bottom-right (width, height) moving only right and down.

    Any valid path consists of exactly `width` right moves and `height` down moves,
    for a total of `width + height` moves.
    The total number of routes is given by the binomial coefficient:
        C(width + height, width) = (width + height)! / (width! * height!)

    Time Complexity: O(min(width, height))
    Space Complexity: O(1)
    """
    return math.comb(width + height, width)

def solve(grid_size: int = 20) -> int:
    """
    Solves Project Euler Problem 15 for a square grid of size grid_size x grid_size.
    Default: grid_size = 20
    """
    return count_lattice_paths(grid_size, grid_size)

if __name__ == "__main__":
    result = solve(20)
    print(f"Project Euler Problem 15 Answer: {result}")
