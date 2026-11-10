# 🧩 Project Euler Solutions

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Project Euler](https://img.shields.io/badge/Project%20Euler-Solved-orange.svg)](https://projecteuler.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured, mathematically optimized repository of **[Project Euler](https://projecteuler.net/)** problem solutions implemented in Python. Each problem adheres to clean architecture, algorithmic efficiency, and the official Project Euler **"one-minute rule"** (solutions execute in under one second).

---

## 📊 Progress Dashboard

- **Total Solved:** 9 Problems
- **Languages:** Python 3
- **Test Coverage:** 100% automated pytest suite

| # | Problem Title | Solution | Runtime | Status |
| :---: | :--- | :---: | :---: | :---: |
| **001** | [Multiples of 3 or 5](https://projecteuler.net/problem=1) | [`problem_001.py`](solutions/problem_001.py) | < 0.01 ms | ✅ Solved |
| **002** | [Even Fibonacci Numbers](https://projecteuler.net/problem=2) | [`problem_002.py`](solutions/problem_002.py) | < 0.01 ms | ✅ Solved |
| **003** | [Largest Prime Factor](https://projecteuler.net/problem=3) | [`problem_003.py`](solutions/problem_003.py) | ~0.15 ms | ✅ Solved |
| **008** | [Largest Product in a Series](https://projecteuler.net/problem=8) | [`problem_008.py`](solutions/problem_008.py) | ~0.40 ms | ✅ Solved |
| **009** | [Special Pythagorean Triplet](https://projecteuler.net/problem=9) | [`problem_009.py`](solutions/problem_009.py) | ~3.8 ms | ✅ Solved |
| **010** | [Summation of Primes](https://projecteuler.net/problem=10) | [`problem_010.py`](solutions/problem_010.py) | ~116 ms | ✅ Solved |
| **011** | [Largest Product in a Grid](https://projecteuler.net/problem=11) | [`problem_011.py`](solutions/problem_011.py) | ~0.99 ms | ✅ Solved |
| **016** | [Power Digit Sum](https://projecteuler.net/problem=16) | [`problem_016.py`](solutions/problem_016.py) | ~0.1 ms | ✅ Solved |
| **020** | [Factorial Digit Sum](https://projecteuler.net/problem=20) | [`problem_020.py`](solutions/problem_020.py) | ~0.1 ms | ✅ Solved |

---

## 🛠️ Repository Layout

```
project-euler/
├── solutions/               # Individual problem implementations
│   ├── problem_001.py
│   ├── problem_002.py
│   ├── problem_003.py
│   ├── problem_008.py
│   ├── problem_009.py
│   ├── problem_010.py
│   ├── problem_011.py
│   ├── problem_016.py
│   └── problem_020.py
├── utils/                   # Shared mathematical helpers & decorators
│   ├── __init__.py
│   └── timing.py            # Precision execution timer
├── tests/                   # Automated pytest validation suite
│   └── test_solutions.py
├── notebooks/               # Mathematical scratchpad & explorations
│   └── project_euler.ipynb
├── run.py                   # Automated solve, benchmark & git sync CLI
├── requirements.txt         # Dependencies
└── README.md
```

---

## 🚀 How to Run & Auto-Sync

### 1. Run & Benchmark Any Problem
Run a specific problem from the project root:
```bash
python run.py 9
python run.py 16
python run.py 20
```

### 2. Solve & Auto-Push to GitHub in One Go
When you finish a problem and want to benchmark, test, commit, and push automatically:
```bash
python run.py <problem_number> --push
```

### 3. Run All Tests
Verify that all historical solutions still pass their test assertions:
```bash
python run.py all
# or
pytest
```

---

## 📜 Principles & Standards
1. **The 1-Minute Rule**: Every algorithm is designed to execute within 1000 ms.
2. **Deterministic & Test-Driven**: Solutions are verified using automated unit tests.
3. **Clean Code**: Meaningful variable names, docstrings explaining mathematical reasoning, and PEP 8 formatting.

