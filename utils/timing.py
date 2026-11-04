import time
from functools import wraps
from typing import Any, Callable, Tuple

def benchmark(func: Callable) -> Callable:
    """Decorator to measure the execution time of a function in milliseconds."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        return result, elapsed_ms
    return wrapper
