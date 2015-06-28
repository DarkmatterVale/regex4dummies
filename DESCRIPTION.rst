regex4dummies: A Simple Way To Find Patterns
============================================

A pattern finder for strings, implemented in Python.

regex4dummies was developed with lazy people in mind! It allows you to easily parse strings and find simple and complex patterns. Since it has such a small learning curve, after a couple of times using it you will become a pro!

In addition, this library is very useful to people who work with NLP ( natural language processing ) very often. This library is intended to work out-of-the-box however, so anyone can use it.


Features
----------

Some features include:

- Automatic pattern detection ( semantic and literal )
- Multiple parsers ( implementations of nltk and pattern )
- Keyword searching to find phrases ( and only phrases that contain said keyword )
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with

This list is very small compared to what will be implemented, so please check back in the future for additional features.

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
  print regex.compare_strings( '', True, strings )

  # Identifying semantic patterns in strings using the nltk parser
  print regex.compare_strings( 'nltk', False, strings )

  # Printing pattern information
  pattern_information = regex.get_sentence_information()
    for objects in pattern_information:
        print "[ Pattern ]          : " + objects.pattern
        print "[ Subject ]          : " + objects.subject
        print "[ Verb ]             : " + objects.verb
        print "[ Object ]           : " + objects.object[0]
        print "[ Reliability Score ]: " + str( objects.reliability_score )


Installation
------------

To install this library, run the following command.

::

  $ pip install regex4dummies


Patch Notes
-------------

( Latest ) 1.1.3 BUG FIX, VERY IMPORTANT IF YOU DOWNLOADED VERSION 1.1.2:

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

If you would like to contriubte, please fork the repository and create a PR with your feature update.


License
---------

Please see LICENSE.txt for information about the MIT license
