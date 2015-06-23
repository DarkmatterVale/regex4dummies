# This is the setup file for pip

description_file = ""

setup(
    name = 'regex4dummies',

    version = '1.0.0',

    description = 'A NLP library that simplifies pattern finding',
    long_description = description_file,

    url = 'https://github.com/DarkmatterVale/regex4dummies',

    author = 'Vale Tolpegin',
    author_email = 'valetolpegin@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers & Programmers',

        'Topic :: NLP',

        'License :: MIT',

        'Programming Language :: Python :: 2.7',
    ],

    packages = find_packages(),

    install_requires = [ 'pattern', 'TextBlob' ],


)
