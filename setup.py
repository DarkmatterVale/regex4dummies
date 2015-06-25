# This is the setup file for pip
from setuptools import setup, find_packages
import os, sys
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst')) as f:
    description_file = f.read()


setup(
    name = 'regex4dummies',

    version = '1.0.3',

    description = 'A NLP library that simplifies pattern finding in strings',
    long_description = description_file,

    url = 'https://github.com/DarkmatterVale/regex4dummies',

    author = 'Vale Tolpegin',
    author_email = 'valetolpegin@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Topic :: Text Processing :: Linguistic',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    packages = find_packages(),

    install_requires = [ 'pattern', 'TextBlob' ],

    keywords = [ 'TextBlob', 'NLTK', 'Pattern', 'NLP' ],
)
