__author__ = 'Vale Tolpegin'

"""

Class information:
- name: Tokenizer
- version: 1.4.0

Tokenizer provides regex4dummies an easy-to-use interface to the pattern, nltk, and nlpnet tokenizers

"""

from nltk_parser import NLTK
from pattern_parser import PATTERN

class Tokenizer:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def tokenize( self, string_to_tokenize, parser ):
        if parser.lower() == "nltk":
            return self.tokenize_nltk( string_to_tokenize )
        elif parser.lower() == "pattern":
            return self.tokenize_pattern( string_to_tokenize )
        elif parser.lower() == "nlpnet":
            return self.tokenize_nlpnet( string_to_tokenize )
        else:
            print "A valid parser was not chosen to tokenize the string. Please choose one of the following:"
            print "- nltk"
            print "- pattern"
            print "- nlpnet"
            print ""

            exit( 0 )


    def tokenize_nltk( self, string_to_tokenize ):
        """ Interface method to the nltk tokenizer """

        pass


    def tokenize_pattern( self, string_to_tokenize ):
        """ Interface method to the pattern tokenizer """

        pass


    def tokenize_nlpnet( self, string_to_tokenize ):
        """ Interface method to the nlpnet tokenizer """

        pass
