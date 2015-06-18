Included in this library is the ability to complete literal parsing on a set of strings. This can be helpful for a number of reasons, including:

- Pattern count ( number of times the pattern appears )
- Identifying non-semantic patterns
- Find patterns in conjunction with semantic pattern finding

To use literal parsing, you need to call the following method:

```
compare_strings( strings, True )

# Strings: The strings to be parsed
# 2nd arg: Determines whether literal parsing is executed
```

By calling this method with this set of arguments, the parser will return a set of strings, also known as patterns, that are literally found.
