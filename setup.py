#!/usr/bin/env python

from setuptools import setup

setup(
    name="PyShirtsIO",
    version="0.0.1",
    description="A Python API wrapper for Shirts.io",
    author="Thomas Lovett",
    author_email="tklovett@gmail.com",
    url="https://github.com/tklovett/PyShirtsIO",
    packages=['ShirtsIO'],
    license="LICENSE",
    test_suite='nose.collector',
    install_requires=[
        'requests',
    ],
    setup_requires=[
        'httpretty',
        'sure',
        'nose',
        'nose-cov',
        'mock'
    ]
)
