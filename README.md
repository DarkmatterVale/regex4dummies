# regex4dummies
A pattern finder for strings, implemented in Python.

regex4dummies was made for lazy people! It allows you to easily parse strings and find simple and complex patterns. In fact, one of the key features of regex4dummies is that the library will automatically find patterns if you give it a mandatory word or phrase to look for. This can be a keyword or something more complex.

###

Features:
- Automatic pattern detection
- Keyword searching to find phrases
- Very versatile library, can be used to find simple and complex patterns
- Simple to use. Just install this library, and import it into whatever scripts you would like to use it with

## Usage

As is stated in the name of this library, it is designed for dumb and lazy people to be able to use without getting stuck. That being said, it does not mean that this library is not versatile or useful. When you compare a set of strings ( see below for examples ), you must use the following format:

```
{ "String 1", "String 2", "String 3", "keyword=Your keyword" }
```

If you do not have a keyword, simply ignore the your keyword part.

```
{ "String 1", "String 2", "String 3", "keyword=" }
```

You can use as many strings as you would like. The keyword, however, must be included in the array, although it can be located at any position within that array. The keyword can be either a single word, or a phrase.

The output of the program is an array of tuples, contained like the following:

```
[ [ 0, 0, "" ], [ 0, 0, "" ] ]
```

Each element of the above array contains a reliability score, an applicability score, and a pattern ( which is a string ). They are placed in the order reliability score, applicability score, pattern. The reliability score attempts to judge how reliable/correct this pattern is. For example, if the pattern was found in two strings ouf of a thousand, then it would have a reliability score of 0. The applicability score attempts to judge how applicable the pattern is to the keyword/phrase. If there is no phrase, this will always be 0. The pattern was the pattern was found when comparing all of the strings. An example of a pattern, with a reliability score of 50 and an applicability score of 80, is shown below.

```
[ [ 50, 80, "pattern" ] ]
```

A simple example of how to use this library is to compare two strings, each containing a name. The objective is to find the name, which is in both strings.

```
import os
import sys
import regex4dummies as re4dummies

string_1 = """ My name is John and I like to program artificial intelligence. """
string_2 = """ John watches his computer learn. """

if __name__ == '__main__':
    combined_list = {}
    combined_list.append( string_1 )
    combined_list.append( string_2 )

    name_comparer = re4dummies()

    print name_comparer.compare_strings( combined_list )
```

When the program is run, only one pattern will be printed. Below is the output. As seen, there is a 100% reliability score, and a 100% applicability score, followed by the pattern which is John

```
[[100, 100, "John"]]
```


## Contributing

If you would like to contriubte, please fork the repository and create a PR with your feature update.

## License

Please see LICENSE.txt for information about the MIT license