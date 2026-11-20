"""
Project Euler Problem 18: Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
            95 64
           17 47 82
          18 35 87 10
         20 04 82 47 65
        19 01 23 75 03 34
       88 02 77 73 07 63 67
      99 65 04 28 06 16 70 92
     41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
   53 71 44 65 25 43 91 52 97 51 14
  70 11 33 28 77 73 17 78 39 68 17 57
 91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

URL: https://projecteuler.net/problem=18
"""

TRIANGLE_DATA: str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def maximum_path_sum(triangle_str: str) -> int:
    """
    Computes the maximum path sum from top to bottom of a numerical triangle
    using bottom-up dynamic programming.

    For each cell at row r and column c:
        triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])

    Time Complexity: O(N^2) where N is the number of rows in the triangle.
    Space Complexity: O(N^2) for the grid representation.
    """
    grid = [
        [int(num) for num in line.split()]
        for line in triangle_str.strip().splitlines()
        if line.strip()
    ]
    if not grid:
        return 0

    # Bottom-up reduction
    for r in range(len(grid) - 2, -1, -1):
        for c in range(len(grid[r])):
            grid[r][c] += max(grid[r + 1][c], grid[r + 1][c + 1])

    return grid[0][0]

def solve(triangle: str = TRIANGLE_DATA) -> int:
    """
    Solves Project Euler Problem 18.
    """
    return maximum_path_sum(triangle)

if __name__ == "__main__":
    result = solve()
    print(f"Project Euler Problem 18 Answer: {result}")
