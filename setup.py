from codecs import open
from os import path

from setuptools import find_packages, setup

# Package meta-data.
NAME = "TopoEmbedX"
DESCRIPTION = "TEX provides classes and methods for higher order representation learning on simplicial, cellular, CW and combinatorial complexes."
URL = "https://github.com/pyt-team/TopoEmbedX"
VERSION = 0.1

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "gudhi",
    "toponetx",
    "networkx",
    "hypernetx",
    "numpy",
    "pre-commit",
    "scipy",
    "karateclub"
]

full_requires = []

test_requires = [
    "pytest",
    "pytest-cov",
]

dev_requires = test_requires + [
    "pre-commit",
    "flake8",
    "yapf",
    "black==22.6.0",
    "black[jupyter]",
    # "flake8-docstrings",  # flake8-docstrings causes flake8 to change behaviour for tests; removed it
    "isort==5.10.1",
    "codecov",
    "coverage",
]

setup(
    name=NAME,
    version=VERSION,
    description="TEX provides classes and methods for higher order represenation learning on simplicial, cellular, CW and combinatorial complexes.",
    long_description="TEX provides classes and methods for higher order represenation learning on simplicial, cellular, CW and combinatorial complexes.",
    url=URL,
    download_url=URL,
    license="MIT",
    author="PyT-Team Authors",
    contact_email="mustafahajij@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "higher order networks",
        "Simplicial Complexes",
        "Simplicial Complex Neural Networks",
        "Cell Complex Neural Networks",
        "Cell Complex Networks",
        "Cubical Complexes",
        "Cellular complexes",
        "Cell Complex",
        "Topological Data Analysis",
        "Topological Machine Learning",
        "Topological Deep Learning",
        "Combinatorial complexes",
        "CW Complex",
        "Higher Order Representation Learning"
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require={
        "full": full_requires,
        "test": test_requires,
        "dev": dev_requires,
    },
    packages=find_packages(),
)

