#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pathlib import Path

THIS_DIR = Path(__file__).parent
README_FILE = THIS_DIR / 'README.rst'
HISTORY_FILE = THIS_DIR / 'HISTORY.rst'

README = README_FILE.read_text()
HISTORY = HISTORY_FILE.read_text()

requirements = ['polysign', 'Tornado', 'concurrent-log-handler', 'requests', 'aioprocessing']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="EggdraSyl Bismuth Foundation",
    author_email='dev@eggpool.net',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Core Bismuth libraries for stable nodes versions.",
    install_requires=requirements,
    license="MIT license",
    long_description=README + '\n\n' + HISTORY,
    include_package_data=True,
    keywords='bismuthcore',
    name='bismuthcore',
    packages=find_packages(include=['bismuthcore']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bismuthfoundation/bismuthcore',
    version='0.0.19',
    zip_safe=False,
)
