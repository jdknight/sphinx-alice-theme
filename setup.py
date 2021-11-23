#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2021 James Knight

from setuptools import find_packages
from setuptools import setup
import os


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Theme',
        'Framework :: Sphinx',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
    ],
    description='Provides the Alice theme for Sphinx projects.',
    entry_points={
        'sphinx.html_themes': [
            'sphinx_alice_theme = sphinx_alice_theme',
        ],
    },
    include_package_data=True,
    install_requires=[
        'sphinx',
    ],
    license='BSD-2-Clause',
    long_description=read('README.md'),
    name='sphinx-alice-theme',
    packages=find_packages(exclude=['tests*']),
    platforms='any',
    test_suite='tests',
    url='https://github.com/jdknight/sphinx-alice-theme',
    version='0.1.0-dev0',
    zip_safe=False,
)
