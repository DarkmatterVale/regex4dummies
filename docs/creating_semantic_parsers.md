# Creating Semantic Parsers

Creating your own parser is a fairly complex process. Because of this, not everyone should attempt it and expect good results immediately as it takes a lot of patience and work. If you would like to create your own parser, however, with enough work, it can be done.

But before you can add your parser to the semantic_parsing file, you need to write the parser! I cannot give any guidance to this since the possibilities of what could be done are endless. I can, however, explain how to integrate your parser into the library.

Each new parser has 2 requirements that it must fulfill ( if you would like to publish it to the community ).

- First, each parser must return the patterns identified as an array with the following attributes: [ reliability score, applicability score, pattern ]. If you are not going to use the reliability score and applicability score, please just set these to 0. The pattern is the string containing the identified pattern.
- Also, the pattern must be added the parse() method located at the top of the semantic_parsing file ( version 1.3.1 of the code is below ):

```
class semantic_parsing:
    def __init__( self, *args, **kwargs ):
        pass

    def parse( self, base_string, test_string, pattern_arg, parser_name ):
        if parser_name == 'nltk':
            return self.use_nltk( base_string, test_string, pattern_arg )
        elif parser_name == 'pattern':
            return self.use_pattern( base_string, test_string, pattern_arg )
        elif parser_name == 'nlpnet':
            return self.use_nlpnet( base_string, test_string, pattern_arg )
        elif parser_name == '':
            parsed_data = []
            parsed_data.append( self.use_nltk( base_string, test_string, [] ) )
            parsed_data.append( self.use_pattern( base_string, test_string, [] ) )
            parsed_data.append( self.use_nlpnet( base_string, test_string, [] ) )

            return self.full_pattern_comparison( parsed_data, pattern_arg )
        else:
            print ""
            print "A valid parser was not chosen. Please choose any of the following parsers: "
            print "- 'nlpnet'"
            print "- 'pattern'"
            print "- 'nltk'"
            print "- ''"
            print ""

            exit( 0 )
```

You will need to add your parser to the if statement "chain", like below:

```
elif parser_name =='Add Your Parser's Name Here':
```

You will also need to call your method in the same format as the other parsers.
