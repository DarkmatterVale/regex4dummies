regex4dummies: A Simple Way To Find Patterns
============================================

A pattern finder for strings, implemented in Python.

regex4dummies was made for lazy people! It allows you to easily parse strings and find simple and complex patterns. In fact, one of the key features of regex4dummies is that the library will automatically find patterns if you give it a mandatory word or phrase to look for. This can be a keyword or something more complex such as a sentence.


Features
----------

- Automatic pattern detection
- Keyword searching to find phrases
- Very versatile library, can be used to find simple and complex patterns ( semantic and literal )
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with


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

  # Identifying literal patterns in strings
  print regex.compare_strings( True, strings )

  # Identifying semantic patterns in strings
  print regex.compare_strings( False, strings )


Installation
------------

To install this library, run the following command.

::

  $ pip install regex4dummies


Patch Notes
-------------

( Latest ) In release 1.0.2, the following has been added/updated:

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
