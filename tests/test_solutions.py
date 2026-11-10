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
    problem_016,
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


def test_problem_016():
    assert problem_016.solve() == 1366

def test_problem_020():
    assert problem_020.solve() == 648

