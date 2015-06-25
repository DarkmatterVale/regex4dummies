regex4dummies: A Simple Way To Find Patterns
============================================

A pattern finder for strings, implemented in Python.

regex4dummies was developed with lazy people in mind! It allows you to easily parse strings and find simple and complex patterns. Since it has such a small learning curve, after a couple of times using it you will become a pro!

In addition, this library is very useful to people who work with NLP ( natural language processing ) very often. This library is intended to work out-of-the-box however, so anyone can use it.

Features
----------

Some features include:

- Automatic pattern detection ( semantic and literal )
- Keyword searching to find phrases ( and only phrases that contain that keyword )
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with

This list is very small compared to what will be implemented, so please check back in the future.


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

( Latest ) In this release ( 1.0.3 ), a number of updates have been added:

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
