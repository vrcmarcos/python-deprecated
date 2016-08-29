# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Python-Deprecated',
    version='1.0.0',
    url='https://github.com/vrcmarcos/python-deprecated',
    license='MIT',
    author='Marcos Cardoso',
    author_email='vrcmarcos@gmail.com',
    description='Python Deprecated Decorator',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
