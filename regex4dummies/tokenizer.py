__author__ = 'Vale Tolpegin'

"""

Class information:
- name: Tokenizer
- version: 1.4.3

Tokenizer provides regex4dummies an easy-to-use interface to the pattern, nltk, and nlpnet tokenizers

"""

from nltk_parser import NLTK
from pattern_parser import PATTERN
from nlpnet_parser import NLPNET

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
        elif parser.lower() == "":
            return self.average_tokenize( string_to_tokenize )
        else:
            print "A valid parser was not chosen to tokenize the string. Please choose one of the following:"
            print "- nltk"
            print "- pattern"
            print "- nlpnet"
            print '- ""'
            print ""

            exit( 0 )


    def average_tokenize( self, string_to_tokenize ):
        """
        Returns the averaged tokenization of the string
        """

        # Get tokenized strings
        tokenized_nltk = self.tokenize_nltk( string_to_tokenize )
        tokenized_pattern = self.tokenize_pattern( string_to_tokenize )
        tokenized_nlpnet = self.tokenize_nlpnet( string_to_tokenize )

        # Splitting the given string for easier processing
        split_input_string = string_to_tokenize.split( ' ' )

        # Bring those strings together to form a single string with all of the averaged tokens
        averaged_string = []
        for word_index in range( 0, len( split_input_string ) ):
            # Setting variables
            nltk_tag = tokenized_nltk[ word_index ][ 1 ]
            pattern_tag = tokenized_pattern.split( ' ' )[ word_index ].split( '/' )[ 1 ]
            nlpnet_tag = tokenized_nlpnet[ 0 ][ word_index ][ 1 ]
            tags = []

            if nltk_tag.lower() == pattern_tag.lower():
                if nltk_tag.lower() == nlpnet_tag.lower():
                    tags.append( [ nltk_tag, 3 ] )
                else:
                    tags.append( [ nltk_tag, 2 ] )
                    tags.append( [ nlpnet_tag, 1 ] )
            elif nltk_tag.lower() == nlpnet_tag.lower():
                tags.append( [ nltk_tag, 2 ] )
                tags.append( [ pattern_tag, 1 ] )
            elif pattern_tag.lower() == nlpnet_tag.lower():
                tags.append( [ nltk_tag, 1 ] )
                tags.append( [ pattern_tag, 2 ] )
            else:
                tags.append( [ nltk_tag, 1 ] )
                tags.append( [ pattern_tag, 1 ] )
                tags.append( [ nlpnet_tag, 1 ] )

            averaged_string.append( ( split_input_string[ word_index ], tags ) )

        # Return the averaged string
        return averaged_string


    def tokenize_nltk( self, string_to_tokenize ):
        """ Interface method to the nltk tokenizer """

        nltk_tokenizer = NLTK()

        return nltk_tokenizer.tokenize( string_to_tokenize )


    def tokenize_pattern( self, string_to_tokenize ):
        """ Interface method to the pattern tokenizer """

        pattern_tokenizer = PATTERN()

        return pattern_tokenizer.tokenize( string_to_tokenize )


    def tokenize_nlpnet( self, string_to_tokenize ):
        """ Interface method to the nlpnet tokenizer """

        nlpnet_tokenizer = NLPNET()

        return nlpnet_tokenizer.tokenize( string_to_tokenize )
