regex4dummies: A Simple Way To Find Patterns
============================================

.. image:: https://travis-ci.org/DarkmatterVale/regex4dummies.svg?branch=master
    :target: https://travis-ci.org/DarkmatterVale/regex4dummies

Simple pattern finding in strings.


Features
----------

- Automatic pattern detection ( semantic and literal )
- Multiple parsers ( implementations of nltk, pattern, and nlpnet )
- Keyword searching to find specific phrases


Roadmap
----------

Some features I plan to implement in the future:

- Machine Learning. This will allow the parsers to learn multiple grammatical “styles” and be able to successfully parse a much wider selection of strings
- Additional parsers
- Continued improvements on the current parsers. This will be a long-term project, and additional details can be found on the main Github page

If you have feature requests, feel free to add an issue to the Github issue tracker. All contributions and requests are appreciated!

Usage
-------

regex4dummies is very easy to use. Simply import the library, get some strings, and compare them!

.. code-block:: Python

  from regex4dummies import regex4dummies

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

( Latest ) v1.3.7: Bug fixes & minor updates

- First version of the accuracy tester released
- Another round of bug fixes. Some of the bugs found can cause aspects of regex4dummies to not be usable ( and crash your programs ), so if you encounter any bugs be sure to update to v1.3.7
- GUI update. The GUI should be compatible with the latest version of regex4dummies now ( it is not backwards compatible, however, so update to the latest version of the library to get full functionality ).


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
