# Creating Literal Parsers

Creating a literal parser is much simpler than creating a semantic parser. I am not able to give you any guidance to how to write this, because it can be done in many different ways.

Every parser must follow a couple of rules to be able to successfully integrate into the current system.

- First, each parser created must return the patterns identified as an array with the following attributes: [ reliability score, applicability score, pattern ]. If you are not going to use the reliability score and applicability score, please just set these to 0. The pattern is the string containing the identified pattern.
- In addition, the pattern must be added the parse() method located at the top of the literal_parsing file ( version 1.3.2 of the code is below ):

```
def parse( self, base_string, test_string, pattern_arg, parser ):
    if parser == "default":
        return self.default_parser( base_string, test_string, pattern_arg );
    else:
        print ""
        print "A valid parser was not chosen. Please choose any of the following parsers: "
        print "- 'default'"
        print ""

        exit( 0 )
```

You will need to add your parser to the if statement "chain", like below:

```
elif parser_name =='Add Your Parser's Name Here':
```

You will also need to call your method in the same format as the other parsers.
