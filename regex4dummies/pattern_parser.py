__author__ = 'Vale Tolpegin'

"""

Class information:

- Name: PATTERN
- Version: 1.4.3

PATTERN is used to manage the Pattern parser

"""

import re
from subprocess import *

from pattern.en import parse
from textblob import TextBlob
from nltk.stem.porter import *
from fuzzywuzzy import fuzz

from normalizer import Normalizer


class PATTERN:
    global pattern_normalizer

    def __init__( self, *args, **kwargs ):
        """
        Constructor method, initializes variables.
        """

        global pattern_normalizer

        # Initializing variables
        pattern_normalizer = Normalizer()


    def tokenize( self, tokenize_string ):
        """ Returns the tokenized version of tokenize_string, which is just a normal English sentence """

        return parse( tokenize_string,
            tokenize = True,         # Split punctuation marks from words?
            tags = True,         # Parse part-of-speech tags? (NN, JJ, ...)
            chunks = False,         # Parse chunks? (NP, VP, PNP, ...)
            relations = False,        # Parse chunk relations? (-SBJ, -OBJ, ...)
            lemmata = False,        # Parse lemmata? (ate => eat)
            encoding = 'utf-8',       # Input string encoding.
            tagset = None )


    def find_dependencies( self, dependency_string ):
        """ Returns dependency_string with sentence dependencies included """

        return parse( dependency_string, relations=True )


    def use_pattern( self, base_string, test_string, pattern_arg ):
        patterns = pattern_arg

        # Creating string textblob for analysis & analyzing the base_string's sentences
        base_blob = TextBlob( base_string )
        base_sentence_info = []

        for base_sentence in base_blob.sentences:
            subject               = ""
            verb                  = ""
            object                = ""
            prepositional_phrases = ""
            raw_data              = parse( str( base_sentence ), relations=True )

            for word in parse( str( base_sentence ), relations=True ).split( ' ' ):
                if "SBJ-" in word:
                    subject += re.sub( r'/.*', '', word ) + " "
                elif "OBJ-" in word:
                    object += re.sub( r'/.*', '', word ) + " "
                elif "VP-" in word:
                    verb += re.sub( r'/.*', '', word ) + " "
                elif "PNP" in word:
                    prepositional_phrases += re.sub( r'/.*', '', word ) + " "
                elif "PNP" not in word and prepositional_phrases[len( prepositional_phrases ) - 3:] != "...":
                    prepositional_phrases += "..."

            #print "[ Subject ]: " + subject
            #print "[ Object ]: " + object
            #print "[ Verb ]: " + verb
            #print "[ Prepositional Phrases ]: " + str( prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ] )
            #print "[ Raw Data ]: " + raw_data

            add_sentence = True
            for sentence in base_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) - 1 ] == str( base_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                base_sentence_info.append( [ subject, verb, object, prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ], str( base_sentence ) ] )

        #print base_sentence_info
        #print "[ Finished Displaying Base Sentence Info ]"

        # Creating string textblob for analysis & analyzing the base_string's sentences
        test_blob = TextBlob( test_string )
        test_sentence_info = []

        for test_sentence in test_blob.sentences:
            subject               = ""
            verb                  = ""
            object                = ""
            prepositional_phrases = ""
            raw_data              = parse( str( test_sentence ), relations=True )

            for word in parse( str( test_sentence ), relations=True ).split( ' ' ):
                if "SBJ-" in word:
                    subject += re.sub( r'/.*', '', word ) + " "
                elif "OBJ-" in word:
                    object += re.sub( r'/.*', '', word ) + " "
                elif "VP-" in word:
                    verb += re.sub( r'/.*', '', word ) + " "
                elif "PNP" in word:
                    prepositional_phrases += re.sub( r'/.*', '', word ) + " "
                elif "PNP" not in word and prepositional_phrases[len( prepositional_phrases ) - 3:] != "...":
                    prepositional_phrases += "..."

            #print "[ Subject ]: " + subject
            #print "[ Object ]: " + object
            #print "[ Verb ]: " + verb
            #print "[ Prepositional Phrases ]: " + str( prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ] )
            #print "[ Raw Data ]: " + raw_data

            add_sentence = True
            for sentence in test_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) - 1 ] == str( test_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                test_sentence_info.append( [ subject, verb, object, prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ], str( test_sentence ) ] )

        #print test_sentence_info
        #print "[ Finished Displaying Test Sentence Info ]"

        return self.identify_common_patterns( base_sentence_info, test_sentence_info, patterns )

    def normalize_sentence_info( self, sentence_info ):
        """ Normalizes all of the incoming text to a standard """

        global pattern_normalizer

        # Normalizing text
        sentence_info = pattern_normalizer.normalize_sentence_info( sentence_info )

        # Return normalized information
        return sentence_info

    def identify_common_patterns( self, base_sentence_info, test_sentence_info, patterns ):
        # Creating variables
        sentence_information = {}

        # Comparing the two sets of strings together & finding patterns
        for base_sentence in base_sentence_info:
            for test_sentence in test_sentence_info:
                # If there are two sentences/patterns to compare
                if base_sentence != [] and test_sentence != []:
                    # Normalize the pattern
                    normalized_base_sentence = self.normalize_sentence_info( base_sentence )
                    normalized_test_sentence = self.normalize_sentence_info( test_sentence )

                    # If the patterns' semantic "value" is the same
                    if normalized_base_sentence[0] == normalized_test_sentence[0] and normalized_base_sentence[1] == normalized_test_sentence[1] and normalized_base_sentence[2] == normalized_test_sentence[2]:
                        # If one sentence/pattern is longer than the other, use that pattern
                        if len( base_sentence[ len( base_sentence ) - 1 ].split( ' ' ) ) > len( test_sentence[ len( test_sentence ) - 1 ].split( ' ' ) ):
                            # If other patterns have been detected
                            if patterns != []:
                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ] = base_sentence[ 0 : len( base_sentence ) - 1 ]
                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 2 )
                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] ) )

                                # If the current test patterns are not in patterns
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]

                                    #sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ] = base_sentence[ 0 : len( base_sentence ) - 1 ]
                                elif base_sentence[ len( base_sentence ) - 1 ] in patterns:
                                    # Updating reliability score
                                    try:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 4 ] += 1
                                    except:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 2 )
                            # If there are no patterns currently found, add this pattern
                            elif patterns == []:
                                patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]

                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ] = base_sentence[ 0 : len( base_sentence ) - 1 ]
                                # Updating reliability score
                                try:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 4 ] += 1
                                except:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 2 )

                                # Adding applicability score
                                try:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 5 ] = fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] )
                                except:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] ) )
                        else:
                            # If there are patterns already found
                            if patterns != []:
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 1 ]
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 2 )
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] ) )

                                # If the test patterns are not in the already found patterns
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]

                                    #sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 1 ]
                                elif test_sentence[ len( test_sentence ) - 1 ] in patterns:
                                    # Updating reliability score
                                    try:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 4 ] += 1
                                    except:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 2 )
                            # If there are no patterns currently found
                            elif patterns == []:
                                patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]

                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 1 ]
                                # Updating reliability score
                                try:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 4 ] += 1
                                except:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 2 )

                                # Adding applicability score
                                try:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 5 ] = fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] )
                                except:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( fuzz.ratio( base_sentence[ len( base_sentence ) - 1 ], test_sentence[ len( test_sentence ) - 1 ] ) )

        return patterns, sentence_information
