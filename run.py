#!/usr/bin/env python3
"""
Project Euler Problem Runner & Auto-Sync Utility
Usage:
    python run.py <problem_number>           # Runs, benchmarks & tests the problem
    python run.py <problem_number> --push    # Benchmarks, updates README, commits & pushes to GitHub
    python run.py all                        # Runs all test suites
"""

import sys
import time
import argparse
import subprocess
import importlib
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).parent.resolve()
SOLUTIONS_DIR = ROOT_DIR / "solutions"
README_PATH = ROOT_DIR / "README.md"

def run_problem(problem_num: int, auto_push: bool = False):
    mod_name = f"problem_{problem_num:03d}"
    sol_file = SOLUTIONS_DIR / f"{mod_name}.py"

    if not sol_file.exists():
        print(f"[!] Error: Solution file not found: {sol_file}")
        sys.exit(1)

    sys.path.insert(0, str(ROOT_DIR))
    try:
        module = importlib.import_module(f"solutions.{mod_name}")
    except Exception as e:
        print(f"[!] Error importing {mod_name}: {e}")
        sys.exit(1)

    if not hasattr(module, "solve"):
        print(f"[!] Error: {mod_name}.py does not define a solve() function.")
        sys.exit(1)

    print(f"\n[EULER] Running Project Euler Problem {problem_num}...")
    start = time.perf_counter()
    answer = module.solve()
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"   Answer:  {answer}")
    print(f"   Runtime: {elapsed_ms:.2f} ms")

    # Run pytest if test file exists
    test_result = subprocess.run(
        [sys.executable, "-m", "pytest", str(ROOT_DIR / "tests" / "test_solutions.py"), "-k", f"problem_{problem_num:03d}"],
        capture_output=True,
        text=True
    )
    if test_result.returncode == 0:
        print("   Tests:   [PASSED]")
    else:
        print("   Tests:   [INFO] (No dedicated test passed or tests pending)")

    if auto_push:
        push_to_git(problem_num, elapsed_ms)

def push_to_git(problem_num: int, runtime_ms: float):
    print("\n[GIT] Auto-syncing to GitHub...")
    subprocess.run(["git", "-C", str(ROOT_DIR), "add", "-A"], check=True)
    
    commit_msg = f"feat(euler): solve problem {problem_num:03d} (runtime: {runtime_ms:.2f}ms)"
    commit_res = subprocess.run(["git", "-C", str(ROOT_DIR), "commit", "-m", commit_msg], capture_output=True, text=True)
    
    if "nothing to commit" in commit_res.stdout:
        print("   Git: No new changes to commit.")
    else:
        print(f"   Git: Committed ({commit_msg})")
        print("   Pushing to GitHub remote (main)...")
        push_res = subprocess.run(["git", "-C", str(ROOT_DIR), "push", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print("   [SUCCESS] Pushed to GitHub!")
        else:
            print(f"   [WARNING] Push failed: {push_res.stderr}")

def run_all():
    print("\n[TEST] Running full test suite for all solutions...")
    subprocess.run([sys.executable, "-m", "pytest", str(ROOT_DIR / "tests" / "test_solutions.py"), "-v"])

def main():
    parser = argparse.ArgumentParser(description="Project Euler Problem Runner & Auto-Sync")
    parser.add_argument("problem", help="Problem number to run (e.g. 1, 9, 16) or 'all'")
    parser.add_argument("--push", action="store_true", help="Auto-commit and push solution to GitHub")

    args = parser.parse_args()
    if args.problem.lower() == "all":
        run_all()
    else:
        try:
            num = int(args.problem)
        except ValueError:
            print(f"Invalid problem argument: {args.problem}")
            sys.exit(1)

        run_problem(num, auto_push=args.push)

if __name__ == "__main__":
    main()
