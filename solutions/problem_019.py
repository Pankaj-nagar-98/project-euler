"""
Project Euler Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

URL: https://projecteuler.net/problem=19
"""


def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year in the Gregorian calendar."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month: int, year: int) -> int:
    """Return the number of days in a given month and year."""
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 31


def count_sundays_on_first(start_year: int = 1901, end_year: int = 2000) -> int:
    """
    Count how many Sundays fell on the first of the month between
    1 Jan start_year and 31 Dec end_year.
    
    1 Jan 1900 was a Monday.
    We map days of the week to integers:
    0 = Sunday, 1 = Monday, 2 = Tuesday, ..., 6 = Saturday.
    """
    weekday = 1  # 1 Jan 1900 was Monday (1)

    # Step through 1900 up to start_year
    for y in range(1900, start_year):
        for m in range(1, 13):
            weekday = (weekday + days_in_month(m, y)) % 7

    # Count first-of-month Sundays in the target interval
    sunday_count = 0
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            if weekday == 0:
                sunday_count += 1
            weekday = (weekday + days_in_month(m, y)) % 7

    return sunday_count


def solve(start_year: int = 1901, end_year: int = 2000) -> int:
    """Main solver function for Project Euler Problem 19."""
    return count_sundays_on_first(start_year, end_year)


if __name__ == "__main__":
    result = solve(1901, 2000)
    print(f"Project Euler Problem 19 Answer: {result}")
