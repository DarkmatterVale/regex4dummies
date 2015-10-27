# Rules for comparing strings

To compare strings, they must be formatted in a specific way. If they are not formatted correctly, the parser will return skewed results. To successfully format your string array, please abide by the following format.

## Formatting Rules

As is stated in the name of this library, it is designed for dumb and lazy people to be able to use without getting stuck. That being said, it does not mean that this library is not versatile or useful. When you compare a set of strings ( see below for examples ), you must use the following format to get proper results from the parser:

```
[ "String 1", "String 2", "String 3", "keyword=Your keyword" ]
```

If you do not have a keyword, simply ignore the your keyword part.

```
[ "String 1", "String 2", "String 3", "keyword=" ]
```

You can use as many strings as you would like. The keyword, however, must be included in the array, although it can be located at any position within that array. The keyword can be either a single word, or a phrase.

The output of the program is an array of strings and integers, contained like the following:

```
[ [ 0, 0, "" ], [ 0, 0, "" ] ]
```

Each element of the above array contains a reliability score, an applicability score, and a pattern ( which is a string ). They are placed in the order reliabili9ty score, applicability score, pattern. The reliability score attempts to judge how reliable/correct this pattern is. For example, if the pattern was found in two strings ouf of a thousand, then it would have a reliability score of 0. The applicability score attempts to judge how applicable the pattern is to the keyword/phrase. If there is no phrase, this will always be 0. The pattern was the pattern was found when comparing all of the strings. An example of a pattern, with a reliability score of 50 and an applicability score of 80, is shown below.

```
[ [ 50, 80, "pattern" ] ]
```

A simple example of how to use this library is to compare two strings, each containing a name. The objective is to find the name, which is in both strings.

```
from regex4dummies import regex4dummies

string_1 = """ My name is John and I like to program artificial intelligence. """
string_2 = """ John watches his computer learn. """

if __name__ == '__main__':
combined_list = {}
combined_list.append( string_1 )
combined_list.append( string_2 )

name_comparer = regex4dummies()
```

There are three arguments that are required to be passed to the compare_strings() function, in this format:

```
compare_strings( parser=parser, pattern_detection=literal_parsing, text=string_list )
```

- parser : This is which parser you would like to use. There are currently two options:
- 'nltk' : This is a parser using nltk's POS tagger and a custom-made recursive grammar parser ( which is still under development, but should be usable and give good results )
- 'pattern' : This is a parser using pattern's built-in POS tagger and parser. None of this is custom made and this is very well developed. However, it still have a high rate of "failure", or incorrect results
- 'nlpnet' : This is a parser that has about a 90% correct rate. It is all built-in and is a little slow, but is very effective for short strings
- NOTE : This does not have to be specified if completing a literal parse of the strings passed
- literal_parsing : If this is true, a literal parse will be applied to the set of strings. If false, a semantic parse will be applied using the specified parser
- string_list : This is covered in detail in the above section, so please look there for in-depth information about this argument

When the program is run, only one pattern will be printed. Below is the output. As seen, there is a 100% reliability score, and a 100% applicability score, followed by the pattern which is John

```
[[100, 100, "John"]]
```
