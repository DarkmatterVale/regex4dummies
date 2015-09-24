regex4dummies: A Simple Way To Find Patterns
============================================

.. image:: https://travis-ci.org/DarkmatterVale/regex4dummies.svg?branch=master
    :target: https://travis-ci.org/DarkmatterVale/regex4dummies

Simple pattern finding in strings and natural language processing. Checkout regex4dummies' website at https://darkmattervale.github.io/regex4dummies/


Features
----------

- Automatic pattern detection ( semantic and literal )
- Multiple parsers ( implementations of nltk, pattern, and nlpnet )
- Keyword searching to find specific phrases within text
- Topic analysis & Important information extraction
- Tokenizer and sentence dependency identifier


Roadmap
----------

Some features I plan to implement in the future:

- Machine Learning. This will allow the parsers to learn multiple grammatical “styles” and be able to successfully parse a much wider selection of strings
- Additional parsers
- Phrase extractor. This can include verb phrases, noun phrases, prepositional phrases, etc
- String comparison function. This will return a value that will determine how similar two strings are

If you have feature requests, feel free to add an issue to the Github issue tracker. All contributions and requests are appreciated!


Usage
-------

regex4dummies is very easy to use. Simply import the library, get some strings, and compare them!

.. code-block:: Python

  from regex4dummies import regex4dummies
  from regex4dummies import Toolkit

  # Creating strings
  strings = [ "This is the first test string.", "This is the second test string." ]

  regex = regex4dummies()

  # Identifying literal patterns in strings
  print regex.compare_strings( 'default', True, strings )

  # Identifying semantic patterns in strings using the nltk parser
  print regex.compare_strings( 'nltk', False, strings )

Above is regex4dummies in its simplest form. It allows for additional features as well, including:

.. code-block:: Python

  # Display the version of regex4dummies you are using
  print regex.__version__

  # To use the other parsers, replace the above line of code with either of the following:
  # print regex.compare_strings( 'pattern', False, strings )
  # print regex.compare_strings( 'nlpnet', False, strings )

  # To call all of the parsers, replace the above line of code with the following:
  # print regex.compare_strings( '', False, strings )

  # To get the topics of the strings, call the get_pattern_topics function
  print regex.get_pattern_topics()

  # Printing pattern information
  pattern_information = regex.get_sentence_information()
    for objects in pattern_information:
        print "[ Pattern ]             : " + objects.pattern
        print "[ Subject ]             : " + objects.subject
        print "[ Verb ]                : " + objects.verb
        print "[ Object ]              : " + objects.object[0]
        print "[ Prep Phrases ]        : " + str( objects.prepositional_phrases )
        print "[ Reliability Score ]   : " + str( objects.reliability_score )
        print "[ Applicability Score ] : " + str( objects.applicability_score )
        print ""

A newly released set of features include a tokenizer and dependency finder function. To use them, simply give a string as the first parameter, and the name of the parser you would like to use as the second for both functions.

.. code-block:: Python

  # Testing the toolkit functions
  tool_tester = Toolkit()

  # Testing the tokenizer functions
  print tool_tester.tokenize( "This is a test string.", "" )

  # Testing the dependency functions
  print tool_tester.find_dependencies( "This is a test string.", "pattern" )

Other features included are demonstrated below.

.. code-block:: Python

  # Testing the information extraction functions
  regex.extract_important_information( [ "This is a test string." ] )


Installation
------------

To install this library, use pip.

::

  $ pip install regex4dummies

In addition to the library, wget is a required command-line command to use the nlpnet parser. If you do not have wget or cannot get it, follow the below directions to still get the functionality of the nlpnet parser.

Instructions to install the required dependency for nlpnet:

1. Download the nlpnet_dependency file on the most recent release found in Github ( please not, when uncompressed, this file is over 350 MB large ).
2. Place this directory into the same directory that nltk-data is located ( if you don't have that installed, just run the library and go through the GUI downloader )

That's it! The nlpnet parser should now be able to be used.


Patch Notes
-------------

v1.4.3: Topic analysis, bug fixes, and code refactoring

- Toolkit NLTK dependency bug. This could have caused the dependency function to not work, but it now does
- Topic analysis update. There is a new function which allows you to extract the important information from within a text
- Code refactoring. Tests have been redone, allowing for flexible updates in the future to be added with ease. In addition, a lot of other code has been changed
- Toolkit POS Tagger update. The update brings an interesting feature which allows you to get the POS tag from all 3 parsers, and regex4dummies will tally up the results, giving you the choice to pick which tag you think is correct


Contributing
--------------

Contributors are welcome and much needed! regex4dummies is still under heavy development, and needs all of the help it can get. If you have any feature ideas, feel free to create an issue on the github repository ( https://github.com/darkmattervale/regex4dummies/issues ) or fork the repository and create your addition.

Any help you can give is much appreciated. The more help we get, the better regex4dummies will perform. Thanks for contributing!


License
---------

Please see LICENSE.txt for information about the MIT license


Citations
-----------

nlpnet:

- Fonseca, E. R. and Rosa, J.L.G. Mac-Morpho Revisited: Towards Robust Part-of-Speech Tagging. Proceedings of the 9th Brazilian Symposium in Information and Human Language Technology, 2013. p. 98-107 [PDF]
