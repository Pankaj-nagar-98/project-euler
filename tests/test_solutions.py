import sys
from pathlib import Path
import pytest

# Ensure solutions can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from solutions import problem_009, problem_016, problem_020

def test_problem_009():
    assert problem_009.solve() == 31875000

def test_problem_016():
    assert problem_016.solve() == 1366

def test_problem_020():
    assert problem_020.solve() == 648
