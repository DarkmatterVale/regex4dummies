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

As of 7/1/15, this is what is left to complete:

- High Priority ( short-term, completed within 3 months from 6/28/15 ):
  - Docs
    - A place that shows the docs in a nice, neat, user friendly way
  - Examples
    - All functions need to have specific examples on how to use them. These examples need to be specific and easy to understand
  - Parsers
    - Update comparison to be more effective in determining whether two sentences/patterns are the same
    - nltk
      - Gather prepositional phrases
      - Gather indirect object as well as direct object
      - Be able to identify word case ( for verbs, present, past, future, etc ) & use that information to make sure some patterns are not removed due to case differences
      - Independent and dependent clause separator
    - pattern
      - Implement additional information gathering ( such as prepositional phrases, etc )
      - Be able to identify word case ( for verbs, present, past, future, etc ) & use that information to make sure some patterns are not removed due to case differences
    - nlpnet
      - Implement additional information gathering ( such as prepositional phrases, etc )
- Medium/Long Priority ( mid-term and long-term, hopefully completed within a year ):
  - Machine Learning implemented-this will allow the parser to learn different "styles" of grammatical syntax, helping it be more accurate ( hopefully )
  - Remove need to specify parser. All 3 parsers will be called, and the correct pattern is deduced automatically

## Usage

To see how to use this library, please see the Wiki part of this Github repository or the docs folder.


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

## Citations

Citations for nlpnet:

- Fonseca, E. R. and Rosa, J.L.G. Mac-Morpho Revisited: Towards Robust Part-of-Speech Tagging. Proceedings of the 9th Brazilian Symposium in Information and Human Language Technology, 2013. p. 98-107 [PDF]
