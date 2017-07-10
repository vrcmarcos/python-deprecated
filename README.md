# Python Deprecated Decorator

Python @deprecated decorator to deprecate old python functions

[![Build Status](https://travis-ci.org/vrcmarcos/python-deprecated.svg?branch=master)](https://travis-ci.org/vrcmarcos/python-deprecated) [![Coverage Status](https://coveralls.io/repos/github/vrcmarcos/python-deprecated/badge.svg?branch=master)](https://coveralls.io/github/vrcmarcos/python-deprecated?branch=master) [![GitHub version](https://badge.fury.io/gh/vrcmarcos%2Fpython-deprecated.svg)](https://badge.fury.io/gh/vrcmarcos%2Fpython-deprecated) [![Code Health](https://landscape.io/github/vrcmarcos/python-deprecated/master/landscape.svg?style=flat)](https://landscape.io/github/vrcmarcos/python-deprecated/master) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vrcmarcos/python-deprecated/master/LICENSE)

## Installation

```shell
pip install Python-Deprecated
```

## Usage

To use this, decorate your deprecated method with **@deprecated** decorator:

```python
from deprecated import deprecated

@deprecated
def deprecated_function():
    ...
```

## Author:

The author/code was made in [this StackOverflow post](http://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically) by [Leandro Regueiro](http://stackoverflow.com/users/1336250/leandro-regueiro), [Patrizio Bertoni](http://stackoverflow.com/users/1315480/patrizio-bertoni) and [Eric](http://stackoverflow.com/users/102441/eric)

## Changelog

#### 1.0.0:
- **deprecated**: Created **@deprecated** decorator