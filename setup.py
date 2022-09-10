#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open('requirements.txt') as fid:
    requires = [line.strip() for line in fid]

setup(
    name='treeFunc',
    version='0.0.3',
    description='Tree feature functions',
    author='tree4101',
    author_email='treegi4101@gmail.com',
    packages=list(setuptools.find_packages()),
    install_requires=requires
)
