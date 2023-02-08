from random import shuffle
from typing import Any, List

from src.helper_generate_data import generate


def set_merge_sort(data: List[Any]):
    zero_array = [0] * len(data)
    merge_sort(data, zero_array, 0, len(data) - 1)


def merge_sort(data: List[Any], temp_data: List[int], start: int, end: int):
    if start < end:
        half = (start + end) // 2
        merge_sort(data, temp_data, start, half)
        merge_sort(data, temp_data, half + 1, end)
        merge(data, temp_data, start, half + 1, end)


def merge(data: List[Any], temp_data: List[int], start: int, half: int, end: int):
    size_of_data = end - start + 1
    end_first_section = half - 1
    idx = start

    while start <= end_first_section and half <= end:
        if data[start] <= data[half]:
            temp_data[idx] = data[start]
            start += 1
        else:
            temp_data[idx] = data[half]
            half += 1
        idx += 1

    while start <= end_first_section:
        temp_data[idx] = data[start]
        start += 1
        idx += 1

    while half <= end:
        temp_data[idx] = data[half]
        half += 1
        idx += 1

    for _ in range(0, size_of_data):
        data[end] = temp_data[end]
        end -= 1


if __name__ == "__main__":
    data = generate(50)
    shuffle(data)
    print(data, "\n")
    set_merge_sort(data)
    print(data)
