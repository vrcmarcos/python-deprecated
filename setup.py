#!/usr/bin/env python
#  -*- coding: utf-8 -*-
u"""
Python-Deprecated
-----------------

Python ``@deprecated`` decorator to deprecate old python classes, functions or methods.

Deprecated is Easy to Use
`````````````````````````

If you need to mark a function or a method as deprecated,
you can use the ``@deprecated`` decorator:

Save in a hello.py:

.. code:: python

    from deprecated import deprecated


    @deprecated
    def some_old_function(x, y):
        return x + y


    class SomeClass(object):
        @deprecated
        def some_old_method(self, x, y):
            return x + y


    some_old_function(12, 34)
    obj = SomeClass()
    obj.some_old_method(5, 8)


And Easy to Setup
`````````````````

And run it:

.. code:: bash

    $ pip install Python-Deprecated
    $ python hello.py
    hello.py:15: DeprecationWarning: Call to deprecated function some_old_function.
      some_old_function(12, 34)
    hello.py:17: DeprecationWarning: Call to deprecated function some_old_method.
      obj.some_old_method(5, 8)


Links
`````

* `website <https://github.com/vrcmarcos/python-deprecated>`_
* `StackOverFlow Question <http://stackoverflow.com/questions/2536307>`_
* `development version
  <https://github.com/vrcmarcos/python-deprecated/zipball/master#egg=Python-Deprecated-dev>`_

"""
from setuptools import setup

setup(
    name='Python-Deprecated',
    version='1.1.0',
    url='https://github.com/vrcmarcos/python-deprecated',
    license='MIT',
    author='Marcos Cardoso',
    author_email='vrcmarcos@gmail.com',
    description='Python @deprecated decorator to deprecate old python classes, functions or methods.',
    long_description=__doc__,
    keywords='deprecate,deprecated,deprecation,warning,warn,decorator',
    packages=['deprecated'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'tox',
            'bumpversion',
            'sphinx',
        ],
    },
)
