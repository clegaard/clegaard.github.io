+++
title = "Python packages in 2023"
date = 2022-02-22
draft = true
+++

Software should be easy to install. 

# New configuration format
The `pyproject.toml` is a configuration file introduced in [PEP 518](https://peps.python.org/pep-0518/), and have since been extended by [PEP 517](https://peps.python.org/pep-0517/), [PEP 621](https://peps.python.org/pep-0621/) and [PEP 660](https://peps.python.org/pep-0660/).
In short, it is an attempt to standardize the information present in the configuration files of various build system like [Setuptools](https://setuptools.pypa.io/en/latest/index.html), [Poetry](https://python-poetry.org/) or [Flit](https://pypi.org/project/flit/).


# Setuptools and pyproject.toml
In addition to the standard attributes of the `pyproject.toml` format it is also possible to specify build system specific information such as how extract metadata like the module's version and extra dependencies for developers, typically installed like `python3 -m pip install my_module[test]`.

``` toml
[build-system]
requires = ["setuptools", "setuptools-scm"] # <- requires setup tools
build-backend = "setuptools.build_meta"

[project]
name = "psl"
authors = [ # <- authors as key value pairs
    {name = "Aaron Tuor", email = "todo@pnnl.gov"},
    {name = "Jan Drgona", email = "todo@pnnl.gov"},
    {name = "Elliot Skomski", email = "todo@pnnl.gov"},
    {name = "Soumya Vasisht", email = "todo@pnnl.gov"},
]

description = "Dynamic Systems Library in Python"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3.10",
]
dependencies = [
    "numpy", "scipy", "matplotlib", "pyts", "tqdm" # <- dependencies
]

dynamic = ["version"] # declares that "version" will be provided by the build backend, in this case Setuptools

# Setuptools specific

[tool.setuptools]
packages = ["psl"] # <- look for modules in the "psl" directory

[tool.setuptools.dynamic]
version = {attr = "psl.__version__"} # <- grab the version from the modules.__version__ attribute

[tool.setuptools.package-data]
psl = ["psl/parameters/buildings/*"] # <- include static data matching the GLOB

[project.scripts]
psl = "psl.cli:cli" # <- defines entry points, making it possible to invoke the module from the shell like `psl --arguments`
```


For a list of Setuptools specific configurations their [docs](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#setuptools-specific-configuration).


# Challenges
Some 

https://github.com/conda/conda/issues/10633