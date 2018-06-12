#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

version = '1.1.1'

install_requires = [
    'six',
    'pyDes>=2.0.1',
    'pyscard',
]

dev_extras = [
    'pep8',
    'tox',
    'pandoc',
    'pypandoc',
]


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", '')

except(IOError, ImportError):
    import io
    with io.open('README.md', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='llsmartcard-ph4',
    version=version,
    description='Module for easily interacting with smartcards.',
    long_description=long_description,
    url='https://github.com/ph4r05/llsmartcard',
    author='Chad Spensky',
    author_email='chad.spensky@ll.mit.eduasd',
    maintainer='Dusan Klinec',
    maintainer_email='dusan.klinec@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_extras,
    },
)
