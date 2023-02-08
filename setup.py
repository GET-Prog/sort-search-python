from pathlib import Path
from typing import Union

from setuptools import find_packages, setup


def open_txt(filename: Union[str, Path]) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    return data


here = Path(__file__).parent.resolve()
requirements = open_txt(here / "requirements.txt")

setup(
    name="SortSearch",
    version=1.0,
    description="Sort and Search",
    author="Vinícius Romano",
    author_email="mdcdxcvi@gmail.com",
    include_package_data=True,
    python_requires=">=3.6.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
)
