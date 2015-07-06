Included in this library is the ability to parse a set of strings to identify semantic patterns. This is an integral part to Natural Linguistics Processing, assisting the programmer in identifying the meaning of sentences.

Semantic pattern finding can assist the programmer in a number of ways, including:
- Identifying subject-verb-object relations
- Identifying similar sentences ( even though they may have completely separate vocabulary )

To implement semantic pattern finding, simply call the following command in your Python script

```
compare_strings( False, strings )

# Strings: The set of strings you would like to identify patterns in
# 2nd arg: Whether the parser should parse literally or semantically ( True = literal, False = semantic )
```
