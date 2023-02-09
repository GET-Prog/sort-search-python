from typing import Callable, List
import pytest  # type: ignore

from src.helper_generate_data import generate


@pytest.fixture
def generate_array() -> List[int]:
    return generate(1000)


def test_generate(generate_array: Callable):
    assert generate_array == list(range(1000))
