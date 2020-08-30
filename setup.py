#!/usr/bin/env python

from setuptools import setup

setup(
    name='p3',
    version='0.1',
    description='Python Package 3',
    author='Adam Ta',
    author_email='notrelevant@mail.net',
    url='https://github.com/sababa11/p3.git',
    install_requires=['p2==0.1'],
    packages=['p3'],
    )

print("OK")
