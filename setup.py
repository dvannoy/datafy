#!/usr/bin/env python
"""A setuptools based setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', 'r') as f:
    for line in f.read().split('\n'):
        requirements.append(line)
print(requirements)

# Read the version number
with open("datafy/_version.py") as f:
    exec(f.read())

setup(name='datafy',
    version=__version__, # use the same version that's in _version.py
    url='https://github.com/dvannoy/datafy',
    author='Dustin Vannoy',
    author_email = 'dustin@dustinvannoy.com',
    packages=['datafy'],
    license='LICENSE.txt',
    description='Library for data processing with files, postgres, and kafka',
    long_description=open('README.rst').read(),
    install_requires=requirements
)
