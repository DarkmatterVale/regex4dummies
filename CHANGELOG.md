# Changelog

## ( Current ) v1.4.5: More bugs, string compare function

- Fixed bug with NLTK verb phrase extractor
- Added a string compare function
- Example application code refactoring

## v1.4.4: Bug updates, Phrase Extractor

- More code refactoring. This time, I redid the structure of the main folder, making it simpler to understand
- Updating code. Previously, I used global variables to store file-wide variables. This has now been changed and done properly through the self variable
- User interface change. Instead of the confusing arguments that previously existed whenever calling a function, a new simpler interface has been created. Details are above
- Multiple bug fixes
- Added Phrase Extractor class. This allows the user to get noun, verb, and prepositional phrases within a text
- Updated pip information and comments

## v1.4.3: Topic analysis, bug fixes, some code refactoring

- Toolkit NLTK dependency bug. This could have caused the dependency function to not work, but it now does
- Topic analysis update. There is a new function which allows you to extract the important information from within a text
- Code refactoring. Tests have been redone, allowing for flexible updates in the future to be added with ease. In addition, a lot of other code has been changed
- Toolkit POS Tagger update. The update brings an interesting feature which allows you to get the POS tag from all 3 parsers, and regex4dummies will tally up the results, giving you the choice to pick which tag you think is correct

## v1.4.2: Miscellaneous Update & overall performance improvement

- Accuracy tester is a lot better ( except for semantic comparisons ). A new "corpus" will be added soon to get accurate semantic comparisons
- Literal parser improvements ( which are numerous ). Multiple bug fixes, sub-patterns are not gathered ( patterns within a larger pattern no longer count as individual patterns ), and some general improvements
- Behind-the-scenes work to update code and make it more flexible for future updates
- GUI update. It is now backwards compatible
- Toolkit update! It should now work, and I apologize for it not working in previous updates
- Topic analyzer update. It should find more topics, as well as returning the topics in order from most-likely to be the main topic to least likely. In the future, an update will allow the extraction of the most important information as a whole ( not just the topics )
- Source code is smaller. Removed some code that was not being used, helping reduce the size of the repository

## v1.4.1: Toolkit bug fix

- The toolkit functions should now work. There was an import typo in the code which caused it to break. I apologize for the late fix!

## v1.4.0: Feature additions and some minor updates

- Two new functions have been added! The tokenizer function will return the tokenized version of the string passed using the given parser ( pattern, nlpnet, or nltk ). The dependency function will return the string with the added dependency information using a specific parser( pattern, nltk, or nlpnet )
- FuzzyWuzzy is the new applicability score. In the past, it has been pretty hard to find a good way to implement the applicability score, and this has been reflected in the quality of the score. Hopefully, this update will greatly improve the accuracy of this score
- Small topic finder update

## v1.3.7: Bug fixes & minor updates

- First version of the accuracy tester released
- Another round of bug fixes. Some of the bugs found can cause aspects of regex4dummies to not be usable ( and crash your programs ), so if you encounter any bugs be sure to update to v1.3.7
- GUI update. The GUI should be compatible with the latest version of regex4dummies now ( it is not backwards compatible, however, so update to the latest version of the library to get full functionality ).

## v1.3.6: Fatal bug fix

If you downloaded version 1.3.5, you will need to update to 1.3.6 before you can use regex4dummies due to a fatal bug. All of the feature updates from 1.3.5 are still available in 1.3.6

## v1.3.5: Feature update

- Topic identifier has been added. This is currently in "beta" and only features NLTK's NE chunker. In the next releases, functionality will increase. Think of this as a preview of what is to come
- Substantial code refactoring. The semantic parser code structure has been changed. This is mostly intended for developers only who would like to develop their own modules for regex4dummies, but it also make the code easier to read
- Behind-the-scenes parser update. A Stemmer has been implemented in pattern comparison to help the parsers be more accurate ( only applies to individual parser calls, not the "all parser" call )

## v1.3.4: Minor update

This is not a parser or core functionality update ( sadly :( ). An accuracy tester is half-completed, but due to the need to create a "gold-standard" test set, I need additional time.

- Artwork added to main website page
- Current Status page updated to include next milestone information display
- Minor in-repo doc update

## v1.3.3: Semantic parser updates!

- All parsers can now be called using the same compare_strings() function, but without having to separate data yourself. See above for the usage of this command ( in the example code )
- Applicability Score has been added and can now be found in any semantic pattern
- A bug fix

## v1.3.2: Developer feature update, semantic parser update, and a literal parser update

- Custom literal parsers can now be created! Documentation will be on the website shortly for those eager to develop their own literal parsers
- Prepositional phrases are now gathered by all parsers. As seen above, they can be seen by calling "objects.prepositional_phrases"
- The scope of the literal parser has increased. Previously, only single sentences were compared to other single sentences before. Now, in addition to single sentence comparisons, multi-sentence comparisons are completed.

## Version 1.3.1: Bug fix and minor background code

- nlpnet parser bug fix. This might have caused a fatal error. To be sure the bug will never affect you, or to fix the bug, update to the most recent version
- Tests have been updated. The code is better tested and will contain fewer bugs at future release times

## Version 1.3.0

This release does not pertain to the actual Python library. Throughout the past week, I have been hard at work creating a nice and simple website for regex4dummies. And I finally got the first version done! Feel free to check out the new homepage of the project, https://darkmattervale.github.io/regex4dummies

## 1.2.1 MAJOR all around update!

- MAJOR: ANOTHER PARSER! nlpnet has been integrated into the library & can be called exactly like nltk or pattern
- MAJOR: Dependency downloader GUI! This will allow you to only download the libraries required for your needs. I am aware these dependencies are currently VERY large, and I am working on reducing the size. Please check back for updates and a newer version to address this
- A bug in the client GUI should be fixed
- travis-ci monitoring and testing. This is another way to test out code to make sure it is release-ready before published
- Minor code refactoring

## 1.1.3 BUG FIX, VERY IMPORTANT IF YOU DOWNLOADED VERSION 1.1.2:

- There is a bug that causes the library to not be usable. To fix this, upgrade to 1.1.3

## 1.1.2 includes a minor addition and an update to the nltk parser.

- __version__ variable added to the regex4dummies class, which allows you to see what version of regex4dummies you are using.
- Compound verbs can now be used in sentences being parsed by the nltk parser

## 1.1.0! The first MAJOR update to regex4dummies has been released! A number of things have been updated in this release, including:

- A BRAND-NEW parser! You can now use an implementation of nltk ( which works in conjunction with a custom-made recursive parser )
- MAJOR code refactoring. Even though end-users will not see this update, it is an important and much-needed cleanup of code
- reliability score update. It now is returned and properly calculated. It should be bug free now
- A couple of bug fixes

To use the new parser, a new option has been created and is the first parameter in the compare_strings() method. It can be seen in action above and in the documentation


## In 1.0.4, a set of functions have been updated. Below is more information on the specific changes:

- get_sentence_information() function updated. Instead of returning a dictionary/list, it now returns an object with the properties shown in the above example code ( last part of the program ). If you were previously using this function, please make sure you update to use the latest version
- GUI has been updated to reflect the function change
- Docs update. The documentation contained within the repository has been updated and is more developed


## In this release ( 1.0.3 ), a number of updates have been added:

- Another GUI update. It is now more advanced and supports additional features.
- Parser update. Reliability score is now available when you grab sentence information ( which is a new command! )


## In release 1.0.2, the following has been added/updated:

- GUI update. Bug fix which caused a malfunction in reading in sentences.


#### In release 1.0.1, the following has been added/updated:

- Parser update. The parser was not properly implementing recursive string parsing, causing some strings to not be compared to other strings. This has now been fixed.
- GUI update ( Alpha version ). This is only Alpha, but it is making a lot of progress and should be smoother & better soon.
