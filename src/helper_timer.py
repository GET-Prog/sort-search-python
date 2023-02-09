from time import perf_counter
from typing import Any, Callable, Tuple


def timing(function: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Tuple[Any, float]:
        start = perf_counter()
        return function(*args, **kwargs), perf_counter() - start

    return wrapper
