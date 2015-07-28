regex4dummies: A Simple Way To Find Patterns
============================================

.. image:: https://travis-ci.org/DarkmatterVale/regex4dummies.svg?branch=master
    :target: https://travis-ci.org/DarkmatterVale/regex4dummies

regex4dummies was developed with lazy people in mind! It allows you to easily parse strings and find simple and complex patterns. Since it has such a small learning curve, after a couple of times using it you will become a pro!

In addition, this library is very useful to people who work with NLP ( natural language processing ) very often. This library is intended to work out-of-the-box however, so anyone can use it.

Remember to check out the new homepage! You can see it at https://darkmattervale.github.io/regex4dummies


Features
----------

Some features include:

- Automatic pattern detection ( semantic and literal )
- Multiple parsers ( implementations of nltk and pattern )
- Keyword searching to find phrases ( and only phrases that contain said keyword )
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with


Roadmap
----------

Some features I plan to implement in the future:

- Machine Learning. This will allow the parsers to learn multiple grammatical “styles” and be able to successfully parse a much wider selection of strings
- Additional parsers
- Continued improvements on the current parsers. This will be a long-term project, and additional details can be found on the main Github page

If you have feature requests, feel free to email me or add an issue to the Github issue tracker. All contributions and requests are appreciated!

Usage
-------

To see how to use this library, please see the Wiki part of this Github repository.

Here is an example of how to use the library.

.. code-block:: Python

  # Importing the regex4dummies library
  from regex4dummies import regex4dummies

  # Identifying test strings
  strings = [ "This is the first string.", "This is the second test string." ]

  # Creating regex object & test strings
  regex = regex4dummies()

  # Display the version of regex4dummies you are using
  print regex.__version__

  # Identifying literal patterns in strings
  print regex.compare_strings( 'default', True, strings )

  # Identifying semantic patterns in strings using the nltk parser
  print regex.compare_strings( 'nltk', False, strings )

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

To install this library, run the following command.

::

  $ pip install regex4dummies

In addition to the library, wget is a required command-line command to use the nlpnet parser. If you do not have wget or cannot get it, follow the below directions to still get the functionality of the nlpnet parser.

Instructions to install the required dependency for nlpnet:

1. Download the nlpnet_dependency file on the most recent release found in Github ( please not, when uncompressed, this file is over 350 MB large ).
2. Place this directory into the same directory that nltk-data is located ( if you don't have that installed, just run the library and go through the GUI downloader )

That's it! The nlpnet parser should now be able to use its POSTagger.

Patch Notes
-------------

( Latest ) v1.3.7: Bug fixes & minor updates

- First version of the accuracy tester released
- Another round of bug fixes. Some of the bugs found can cause aspects of regex4dummies to not be usable ( and crash your programs ), so if you encounter any bugs be sure to update to v1.3.7
- GUI update. The GUI should be compatible with the latest version of regex4dummies now ( it is not backwards compatible, however, so update to the latest version of the library to get full functionality ).

Released on 7/28/2015

v1.3.6: Fatal bug fix

If you downloaded version 1.3.5, you will need to update to 1.3.6 before you can use regex4dummies due to a fatal bug. All of the feature updates from 1.3.5 are still available in 1.3.6

v1.3.5: Feature update

- Topic identifier has been added. This is currently in "beta" and only features NLTK's NE chunker. In the next releases, functionality will increase. Think of this as a preview of what is to come
- Substantial code refactoring. The semantic parser code structure has been changed. This is mostly intended for developers only who would like to develop their own modules for regex4dummies, but it also make the code easier to read
- Behind-the-scenes parser update. A Stemmer has been implemented in pattern comparison to help the parsers be more accurate ( only applies to individual parser calls, not the "all parser" call )

v1.3.4: Minor update

This is not a parser or core functionality update ( sadly :( ). An accuracy tester is half-completed, but due to the need to create a "gold-standard" test set, I need additional time.

- Artwork added to main website page
- Current Status page updated to include next milestone information display
- Minor in-repo doc update

v1.3.3: Semantic parser updates!

- All parsers can now be called using the same compare_strings() function, but without having to separate data yourself. See above for the usage of this command ( in the example code )
- Applicability Score has been added and can now be found in any semantic pattern
- A bug fix

v1.3.2: Developer feature update, semantic parser update, and a literal parser update

- Custom literal parsers can now be created! Documentation will be on the website shortly for those eager to develop their own literal parsers
- Prepositional phrases are now gathered by all parsers. As seen above, they can be seen by calling "objects.prepositional_phrases"
- The scope of the literal parser has increased. Previously, only single sentences were compared to other single sentences before. Now, in addition to single sentence comparisons, multi-sentence comparisons are completed.

Released on 7/8/15 ( July 8, 2015 )

Version 1.3.1: Bug fix and minor background code

- nlpnet parser bug fix. This might have caused a fatal error. To be sure the bug will never affect you, or to fix the bug, update to the most recent version
- Tests have been updated. The code is better tested and will contain fewer bugs at future release times

Version 1.3.0

This release does not pertain to the actual Python library. Throughout the past week, I have been hard at work creating a nice and simple website for regex4dummies. And I finally got the first version done! Feel free to check out the new homepage of the project, https://darkmattervale.github.io/regex4dummies

1.2.1 MAJOR all around update!

- MAJOR: ANOTHER PARSER! nlpnet has been integrated into the library & can be called exactly like nltk or pattern
- MAJOR: Dependency downloader GUI! This will allow you to only download the libraries required for your needs. I am aware these dependencies are currently VERY large, and I am working on reducing the size. Please check back for updates and a newer version to address this
- A bug in the client GUI should be fixed
- travis-ci monitoring and testing. This is another way to test out code to make sure it is release-ready before published
- Minor code refactoring

1.1.3 BUG FIX, VERY IMPORTANT IF YOU DOWNLOADED VERSION 1.1.2:

- There is a bug that causes the library to not be usable. To fix this, upgrade to 1.1.3

1.1.2 includes a minor addition and an update to the nltk parser.

- __version__ variable added to the regex4dummies class, which allows you to see what version of regex4dummies you are using.
- Compound verbs can now be used in sentences being parsed by the nltk parser

1.1.0! The first MAJOR update to regex4dummies has been released! A number of things have been updated in this release, including:

- A BRAND-NEW parser! You can now use an implementation of nltk ( which works in conjunction with a custom-made recursive parser )
- MAJOR code refactoring. Even though end-users will not see this update, it is an important and much-needed cleanup of code
- reliability score update. It now is returned and properly calculated. It should be bug free now
- A couple of bug fixes

To use the new parser, a new option has been created and is the first parameter in the compare_strings() method. It can be seen in action above and in the documentation


In 1.0.4, a set of functions have been updated. Below is more information on the specific changes:

- get_sentence_information() function updated. Instead of returning a dictionary/list, it now returns an object with the properties shown in the above example code ( last part of the program ). If you were previously using this function, please make sure you update to use the latest version
- GUI has been updated to reflect the function change
- Docs update. The documentation contained within the repository has been updated and is more developed


In this release ( 1.0.3 ), a number of updates have been added:

- Another GUI update. It is now more advanced and supports additional features.
- Parser update. Reliability score is now available when you grab sentence information ( which is a new command! )


In release 1.0.2, the following has been added/updated:

- GUI update. Bug fix which caused a malfunction in reading in sentences.


In release 1.0.1, the following has been added/updated:

- Parser update. The parser was not properly implementing recursive string parsing, causing some strings to not be compared to other strings. This has now been fixed.
- GUI update ( Alpha version ). This is only Alpha, but it is making a lot of progress and should be smoother & better soon.


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
