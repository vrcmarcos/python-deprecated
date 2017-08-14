# Python Deprecated Decorator

Python ``@deprecated`` decorator to deprecate old python classes, functions or methods.

[![Build Status](https://travis-ci.org/vrcmarcos/python-deprecated.svg?branch=master)](https://travis-ci.org/vrcmarcos/python-deprecated)
[![Build status](https://ci.appveyor.com/api/projects/status/ctgktcdg2pf8lsxe?svg=true)](https://ci.appveyor.com/project/tantale/python-deprecated)
[![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/python-deprecated/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/python-deprecated?branch=master)
[![GitHub version](https://badge.fury.io/gh/vrcmarcos%2Fpython-deprecated.svg)](https://badge.fury.io/gh/vrcmarcos%2Fpython-deprecated)
[![Code Health](https://landscape.io/github/vrcmarcos/python-deprecated/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/python-deprecated/master)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/python-deprecated/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/python-deprecated/badge/?version=latest)](http://python-deprecated.readthedocs.io/en/latest/?badge=latest)

## Installation

```shell
pip install Python-Deprecated
```

## Usage

To use this, decorate your deprecated function with **@deprecated** decorator:

```python
from deprecated import deprecated


@deprecated
def some_old_function(x, y):
    return x + y
```

You can also decorate a class or a method:

```python
from deprecated import deprecated


class SomeClass(object):
    @deprecated
    def some_old_method(self, x, y):
        return x + y


@deprecated
class SomeOldClass(object):
    pass
```

You can give a "reason" message to help the developer to choose another function/class:

```python
from deprecated import deprecated


@deprecated(reason="use another function")
def some_old_function(x, y):
    return x + y
```

## Authors

The authors of this library are:
[Marcos CARDOSO](https://github.com/vrcmarcos), and
[Laurent LAPORTE](https://github.com/tantale).

The original code was made in [this StackOverflow post](https://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically) by
[Leandro REGUEIRO](https://stackoverflow.com/users/1336250/leandro-regueiro),
[Patrizio BERTONI](https://stackoverflow.com/users/1315480/patrizio-bertoni), and
[Eric WIESER](https://stackoverflow.com/users/102441/eric).
