#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='govorun',
    version='0.1',
    description='',
    author='Denis Gubanov',
    author_email='v12aml@gmail.com',
    install_requires=[
        "pecan",
    ],
    test_suite='govorun',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
