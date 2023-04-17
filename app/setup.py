#!/usr/bin/env python

from distutils.core import find_packages, setup

setup(
    name="app",
    version="1.0",
    description="Django Utility",
    author="TODO",
    author_email="TODO@TODO.com",
    url="https://www.python.org/sigs/distutils-sig/",
    packages=find_packages(),
    scripts=["manage.py"],
)
