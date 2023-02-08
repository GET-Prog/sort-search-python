from random import shuffle
from typing import List

def generate(size: int) -> List[int]:
    data = list(range(size))
    shuffle(data)
    return data

if __name__=="__main__":
    generate(1000)