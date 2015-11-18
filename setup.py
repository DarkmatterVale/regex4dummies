# This is the setup file for pip
from setuptools import setup, find_packages
import os, sys
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst')) as f:
    description_file = f.read()


setup(
    name = 'regex4dummies',

    version = '1.4.5',

    description = 'A NLP library that simplifies pattern finding in strings',
    long_description = description_file,

    url = 'https://darkmattervale.github.io/regex4dummies',

    author = 'Vale Tolpegin',
    author_email = 'regex4dummies@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    packages = find_packages(),

    install_requires = [ 'pattern', 'TextBlob', 'nltk', 'nlpnet', 'numpy', 'fuzzywuzzy', 'python-Levenshtein' ],

    keywords = [ 'TextBlob', 'NLTK', 'Pattern', 'NLP' ],
)
