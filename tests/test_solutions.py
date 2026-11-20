import sys
from pathlib import Path
import pytest

# Ensure solutions can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from solutions import (
    problem_001,
    problem_002,
    problem_003,
    problem_008,
    problem_009,
    problem_010,
    problem_011,
    problem_012,
    problem_013,
    problem_014,
    problem_015,
    problem_016,
    problem_017,
    problem_020,
)

def test_problem_001():
    # Test example given in problem description
    assert problem_001.solve(10) == 23
    # Test full answer
    assert problem_001.solve(1000) == 233168

def test_problem_002():
    # Test small limit (2 + 8 + 34 = 44)
    assert problem_002.solve(100) == 44
    # Test full answer below 4,000,000
    assert problem_002.solve(4_000_000) == 4613732

def test_problem_003():
    # Test example given in problem description (13195 -> 29)
    assert problem_003.solve(13195) == 29
    # Test target number 600851475143 -> 6857
    assert problem_003.solve(600851475143) == 6857

def test_problem_008():
    # Test example given in problem description (4 adjacent digits -> 5832)
    assert problem_008.solve(4) == 5832
    # Test target problem (13 adjacent digits)
    assert problem_008.solve(13) == 23514624000

def test_problem_009():
    assert problem_009.solve() == 31875000

def test_problem_010():
    # Test example given in problem description (primes below 10 -> 17)
    assert problem_010.solve(10) == 17
    # Test target problem (primes below 2,000,000)
    assert problem_010.solve(2_000_000) == 142913828922

def test_problem_011():
    # Verify the target problem answer
    assert problem_011.solve() == 70600674

def test_problem_012():
    # Test example given in problem description (over 5 divisors -> 28)
    assert problem_012.solve(5) == 28
    # Test target problem (over 500 divisors)
    assert problem_012.solve(500) == 76576500

def test_problem_013():
    # Test target problem: first 10 digits of the 100 50-digit numbers sum
    assert problem_013.solve(10) == 5537376230

def test_problem_014():
    # Test example: starting with 13 generates 10 terms (starts below 20 produce 9 for 13 or similar)
    # Target problem: starting number under one million
    assert problem_014.solve(1_000_000) == 837799

def test_problem_015():
    # Test example: 2x2 grid has 6 routes
    assert problem_015.solve(2) == 6
    # Target problem: 20x20 grid
    assert problem_015.solve(20) == 137846528820



def test_problem_016():
    assert problem_016.solve() == 1366

def test_problem_017():
    # Test example: 1 to 5 -> 19
    assert problem_017.solve(5) == 19
    # Test specific word lengths from problem description
    assert len(problem_017.number_to_words(342)) == 23
    assert len(problem_017.number_to_words(115)) == 20
    # Test full target problem 1 to 1000
    assert problem_017.solve(1000) == 21124

def test_problem_020():
    assert problem_020.solve() == 648

