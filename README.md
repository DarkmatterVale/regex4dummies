# regex4dummies

![Build Status](https://travis-ci.org/DarkmatterVale/regex4dummies.svg?branch=master)

A pattern finder for strings, implemented in Python.

regex4dummies was made for lazy people! It allows you to easily parse strings and find simple and complex patterns. In fact, one of the key features of regex4dummies is that the library will automatically find patterns if you give it a mandatory word or phrase to look for. This can be a keyword or something more complex.


###

Features:
- Automatic pattern detection
- Keyword searching to find phrases
- Very versatile library, can be used to find simple and complex patterns
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with


## Roadmap

As of 6/28/15, this is what is left to complete:

- High Priority ( short-term, completed within 3 months ):
  - Docs
    - A place that shows the docs in a nice, neat, user friendly way
  - Examples
    - All functions need to have specific examples on how to use them. These examples need to be specific and easy to understand
  - Parsers
    - nltk
      - Update custom-made grammatical parser to be more effective in determining whether two sentences are the same
      - Gather prepositional phrases
      - Gather indirect object as well as direct object
      - Be able to identify word case ( for verbs, present, past, future, etc ) & use that information to make sure some patterns are not removed due to case differences
      - Independent and dependent clause separator
    - pattern
      - Implement additional information gathering
      - Implement a more effective way to compare sentences to get better results. Currently, only if the subject, verb, and objects are the same will the two sentences be considered the same. This is good for many situations, but when comparing complex sentences, this will get a little tricky
    - nlpnet
      - Add support for this parser
      - Add citations that the author requires be added
- Medium/Long Priority ( mid-term and long-term, hopefully completed within a year ):
  - Machine Learning implemented-this will allow the parser to learn different "styles" of grammatical syntax, helping it be more accurate

## Usage

To see how to use this library, please see the Wiki part of this Github repository.


## Installation

To install this library, run the following command.

```
pip install regex4dummies
```

NOTE: THIS CURRENTLY DOES NOT WORK. We are in the process of having this package added to pip's list of libraries.


## Contributing

If you would like to contriubte, please fork the repository and create a PR with your feature update.


## License

Please see LICENSE.txt for information about the MIT license
