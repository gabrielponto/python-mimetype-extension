# -*- coding: utf-8 -*-
import os
import re
import sys

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version(package):
    """Return package version as listed in `__version__` in `__init__.py`."""
    init_py = open(os.path.join(os.path.dirname(__file__),
                                package, '__init__.py'),
                   'r').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE
                     ).group(1)




setup(
    name='pymimeext',
    version=get_version('pymimeext'),
    author='Gabriel Oliveira',
    author_email='gabriel@gabrieloliveira.net',
    url='https://github.com/gabrielponto/python-mimetype-extension',
    packages=find_packages(),
    package_data={
        
    },
    zip_safe=False,
    provides=[
        'pymimeext'
    ],
    license='BSD',
    description='Python library to get content-type based on extension',
    long_description=read('README.md'),
    download_url='https://github.com/gabrielponto/python-mimetype-extension',
    scripts=[
        
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    install_requires=[
        
    ],
    tests_require=[
        
    ]
)