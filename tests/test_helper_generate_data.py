import pytest

from src.helper_generate_data import generate


@pytest.fixture
def generate_array():
    return generate(1000)


def test_generate(generate_array):
    assert generate_array == list(range(1000))
