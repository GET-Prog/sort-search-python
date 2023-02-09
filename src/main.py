from random import shuffle
from typing import Callable

from src.helper_generate_data import generate
from src.sort import merge_sort, quick_sort


def compare_sort():
    data_size = 1_000_000
    turns = 1_000

    average_time_merge = time_sort(merge_sort.merge_sort_it, data_size, turns)
    print(
        "merge function took {:.3f} ms ({} turns)".format(
            average_time_merge * 1000.0, turns
        )
    )

    average_time_quick = time_sort(quick_sort.quick_sort_it, data_size, turns)
    print(
        "quick function took {:.3f} ms ({} turns)".format(
            average_time_quick * 1000.0, turns
        )
    )


def time_sort(function: Callable, size: int, turns: int) -> float:
    total_time = 0
    for _ in range(turns):
        data = generate(size)
        shuffle(data)
        data, time = function(data)
        total_time += time

    average_time = total_time / turns
    return average_time


if __name__ == "__main__":
    compare_sort()
