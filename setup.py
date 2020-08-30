#!/usr/bin/env python

from setuptools import setup

setup(
    name='p3',
    version='0.1',
    description='Python Distribution Utilities',
    author='Adam Ta',
    author_email='notrelevant@gmail.net',
    url='https://github.com/sababa11/p1.git',
    install_requires=['p2==0.1'],
    packages=['p3'],
    )

print("OK")
