#!/usr/bin/python
from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='rfc3161ng_async',
    version='3.0-dev',
    license='MIT',
    url='https://github.com/nicholasamorim/rfc3161ng_async',
    description='Python 3.7+ implementation of the RFC3161 specification, using pyasn1, tornado or aiohttp',
    long_description=long_description,
    author='Benjamin Dauvergne',
    author_email='bdauvergne@entrouvert.com',
    maintainer='Nicholas Amorim',
    maintainer_email='nicholas@alienretro.com',
    platforms=['any'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['rfc3161ng_async'],
    python_requires='>=3.7',
    install_requires=[
        'pyasn1',
        'python-dateutil',
        'pyasn1_modules',
        'cryptography',
    ]
)
