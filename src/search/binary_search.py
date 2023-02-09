from random import sample
from typing import Any, List

from src.helper_generate_data import generate


def binary_search(data: List[Any], target: Any) -> int:
    start_interval, end_interval = 0, len(data) - 1

    while start_interval <= end_interval:
        half = (start_interval + end_interval) // 2
        if data[half] == target:
            return half

        if data[half] < target:
            start_interval = half + 1
        else:
            end_interval = half - 1

    return -1


if __name__ == "__main__":
    data = generate(1000)
    target = sample(data, 1)[0]

    print(f"Buscando por {target} em uma lista de tamanho {len(data)}")
    idx = binary_search(data, target)
    print(f"Item {data[idx]} foi localizado na posição {idx}")
