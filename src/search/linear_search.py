from random import sample
from typing import Any, List

from src.helper_generate_data import generate


def busca_linear(data: List[Any], target: Any) -> int:
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    else:
        return -1


if __name__ == "__main__":
    data = generate(1000)
    target = sample(data, 1)[0]

    print(f"Buscando por {target} em uma lista de tamanho {len(data)}")
    idx = busca_linear(data, target)
    print(f"Item {data[idx]} foi localizado na posição {idx}")
