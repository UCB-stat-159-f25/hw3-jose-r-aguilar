# Ligotools: a Python package to read LIGO data


This repository contains a minimal, toy Python package with a few files as illustration for students of how to lay out their code to meet minimal Python packaging requirements.

It has a single source directory (`ligotools`) with an `__init__.py` file and one "implementation" file (`readligo.py`) as well as a few tests in `ligotools/tests`.

In addition to this `README.md` it includes some basic infrastructure: `LICENSE`, `pyproject.toml` and `.gitignore` files.

## Installation

This project can currently only be installed from source, via

```
pip install .
```

or for a development installation via


```
pip install -e .
```

## Tests

You can run the project test suite via

```
pytest readligo
```


## License

This project is released under the terms of the BSD 3-clause License.