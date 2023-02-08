from typing import Any, List, Optional
from generate_data import generate
from random import sample

def busca_linear(data: Optional[List[Any]], target: Any) -> int:
    for idx in range(len(data)):
        if data[idx]==target:
            return idx
    else:
        return -1
    
if __name__=="__main__":
    data = generate(1000)
    target = sample(data, 1)[0]

    idx = busca_linear(data, target)
    print(f"{target} localizado.\nItem {data[idx]} foi localizado na posição {idx}")
