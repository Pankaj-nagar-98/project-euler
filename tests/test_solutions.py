import sys
from pathlib import Path
import pytest

# Ensure solutions can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from solutions import problem_001, problem_002, problem_009, problem_016, problem_020

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

def test_problem_009():
    assert problem_009.solve() == 31875000

def test_problem_016():
    assert problem_016.solve() == 1366

def test_problem_020():
    assert problem_020.solve() == 648

