__author__ = 'Vale Tolpegin'

import re
import os
import sys
from subprocess import *

from pattern.en import parse
from textblob import TextBlob
import nltk
import nlpnet

from nlpnet_parser import NLPNET
from nltk_parser import NLTK
from pattern_parser import PATTERN


"""

Class information:

- name: semantic_parsing
- version: 1.3.6

"""

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


    def use_nlpnet( self, base_string, test_string, pattern_arg ):
        """ Interface method to the nlpnet parser """

        # Instantiating NLPNET parser object
        nlpnet_parser = NLPNET()

        return nlpnet_parser.use_nlpnet( base_string, test_string, pattern_arg )


    def use_nltk( self, base_string, test_string, pattern_arg ):
        """ Interface method to the nltk parser """

        # Instantiating NLTK parser object
        nltk_parser = NLTK()

        return nltk_parser.use_nltk( base_string, test_string, pattern_arg )

    def use_pattern( self, base_string, test_string, pattern_arg ):
        """ Interface method to the pattern parser """

        # Instantiating PATTERN parser object
        pattern_parser = PATTERN()

        return pattern_parser.use_pattern( base_string, test_string, pattern_arg )


    # This function determines:
    #   1. Removes duplicate patterns
    #   2. Applicability score for a given pattern
    #
    # This function is used when all 3 parsers are used to identify patterns in one single call
    def full_pattern_comparison( self, parsed_data, patterns ):
        # Creating variable containing pattern information that will be returned
        pattern_information = {}

        # Comparing the output of one parser to the output of each other parser
        # This is the base data index which will be compared to all other outputs. For example, if there are 4 parsers, the total comparison will look something like:
        # Parsers: 1 2 3 4
        # 1 : 2 3 4
        # 2 : 3 4
        # 3 : 4
        # Where ':' means compared to.
        for data_index in range( 0, len( parsed_data ) ):
            # Getting the actual information about every pattern in a parser
            base_data = parsed_data[ data_index ][ 1 ]

            # For every pattern identified by that parser
            for base_pattern in base_data:
                # Get the pattern's information
                base_pattern_subject               = base_data[ base_pattern ][ 0 ]
                base_pattern_verb                  = base_data[ base_pattern ][ 1 ]
                base_pattern_object                = base_data[ base_pattern ][ 2 ]
                base_pattern_prepositional_phrases = base_data[ base_pattern ][ 3 ]

                # Comparing the base parser to the remainder of parsers
                for compare_index in range( data_index, len( parsed_data ) ):
                    # Getting the information about every pattern identified by the parser
                    test_data = parsed_data[ compare_index ][ 1 ]

                    # For each pattern identified
                    for test_pattern in test_data:
                        # Getting pattern information
                        test_pattern_subject               = test_data[ test_pattern ][ 0 ]
                        test_pattern_verb                  = test_data[ test_pattern ][ 1 ]
                        test_pattern_object                = test_data[ test_pattern ][ 2 ]
                        test_pattern_prepositional_phrases = test_data[ test_pattern ][ 3 ]

                        # Comparing pattern information
                        if base_pattern_subject == test_pattern_subject and base_pattern_verb == test_pattern_verb and base_pattern_object == test_pattern_object:
                            # If the patterns are the same, add the patterns to the identified patterns
                            # If the base_pattern is more descriptive, add that to the pattern information
                            if len( base_pattern.split( ' ' ) ) > len( test_pattern.split( ' ' ) ):
                                pattern_information[ base_pattern.lower() ] = [ base_pattern_subject, base_pattern_verb, base_pattern_object, base_pattern_prepositional_phrases, 2, 0 ]

                                # As long as the pattern is not already found
                                if base_pattern.lower() not in patterns and test_pattern.lower() not in patterns:
                                    # Add the pattern to the list of identified patterns
                                    patterns.append( str( base_pattern.lower() ) )
                                else:
                                    pattern_information[ base_pattern.lower() ][ 4 ] += 1

                                pattern_information[ base_pattern.lower() ][ 5 ] += 1
                            # Otherwise, add test_pattern
                            else:
                                pattern_information[ test_pattern.lower() ] = [ test_pattern_subject, test_pattern_verb, test_pattern_object, test_pattern_prepositional_phrases, 2, 0 ]

                                # As long as the pattern is not already found
                                if test_pattern.lower() not in patterns and base_pattern.lower() not in patterns:
                                    # Add the pattern to the list of identified patterns
                                    patterns.append( str( test_pattern.lower() ) )
                                else:
                                    pattern_information[ test_pattern.lower() ][ 4 ] += 1

                                pattern_information[ test_pattern.lower() ][ 5 ] += 1

        return patterns, pattern_information
