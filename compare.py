__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Parsing related libraries
import re
from textblob import TextBlob
from textblob.parsers import PatternParser
from pattern.en import parse

"""

    This class accomplishes the bulk of regex4dummies' work. Below is a short list of how this class works and what it does.

    1. Find patterns in a set of strings ( including or excluding a keyword search )
    2. Determine patterns' applicability and reliability
        a. Is the string's meaning different than another string? ( applicability )
        b. How many sources contain this pattern? ( reliability )
    3. Returns an array of patterns with the following values per array item
        a. Pattern: this is the string that was identified
        b. Reliability Score: 0 - 100 based off of how many times this pattern/string is seen on websites
        c. Applicability Score: 0 - 100 based off of how applicable/relevant this pattern/string is to the original query

"""

class compare:

    # Empty constructor
    def __init__( self, *args, **kwargs ):
        pass

    # This method is called by the main regex4dummies class, and calls all further methods to find strings
    def compare_strings( self, strings, literal ):
        # Reset patterns variable
        patterns = []

        # Find the keyword
        keyword = ""
        for string in strings:
            if 'keyword=' in string:
                keyword = re.sub( 'keyword=', '', string )

        # Call find_patterns( strings )
        patterns = self.find_patterns( strings, 0, literal, [] )

        # After patterns are identified in strings, complete final processing
        #   1. Find reliability score
        #   2. Find applicability score
        #   3. If there is a keyword
        #       a. pare down pattern list to only those that have the keyword in them

        compiled_patterns = []
        for pattern in patterns:
            if keyword != '':
                if keyword in pattern:
                    compiled_patterns += [ self.find_reliability_score( pattern ), self.find_applicability_score( pattern ), pattern ]
            else:
                compiled_patterns += [ self.find_reliability_score( pattern ), self.find_applicability_score( pattern ), pattern ]

        return compiled_patterns

    # Recursive function that compares all strings and determins reliability score, applicability score, and pattern
    def find_patterns( self, strings, current_index, literal_find, patterns_arg ):
        patterns = patterns_arg

        if not literal_find:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, False, patterns_arg )

            # for index in range( current_index, len( strings ) - 1 ):
            for index in range( current_index, len( strings ) - 1 ):
                # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                patterns = self.identify_patterns( strings[ index ], strings[ index + 1 ], patterns )
        else:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, True, patterns_arg )

            # for index in range( current_index, len( strings ) - 1 ):
            for index in range( current_index, len( strings ) - 1 ):
                # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                patterns = self.find_literal_patterns( strings[ index ], strings[ index + 1 ], patterns )

        # return patterns
        return patterns

    # This function identifies patterns in 2 strings
    def identify_patterns( self, base_string, test_string, pattern_arg ):
        # patterns = {}
        patterns = pattern_arg

        # Creating string textblob for analysis & analyzing the base_string's sentences
        base_blob = TextBlob( base_string, parser=PatternParser() )
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
                    if sentence[ len( sentence ) ] == str( base_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                base_sentence_info.append( [ subject, verb, object, prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ], str( base_sentence ) ] )

        #print base_sentence_info
        #print "[ Finished Displaying Base Sentence Info ]"

        # Creating string textblob for analysis & analyzing the base_string's sentences
        test_blob = TextBlob( test_string, parser=PatternParser() )
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
                    if sentence[ len( sentence ) ] == str( test_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                test_sentence_info.append( [ subject, verb, object, prepositional_phrases.split( '...' )[ 1:len(prepositional_phrases.split( '...' )) ], str( test_sentence ) ] )

        #print test_sentence_info
        #print "[ Finished Displaying Test Sentence Info ]"

        # Comparing the two sets of strings together & finding patterns
        for base_sentence in base_sentence_info:
            for test_sentence in test_sentence_info:
                if base_sentence != [] and test_sentence != []:
                    if base_sentence[0] == test_sentence[0] and base_sentence[1] == test_sentence[1] and base_sentence[2] == test_sentence[2]:
                        if len( base_sentence[ len( base_sentence ) - 1 ].split( ' ' ) ) > len( test_sentence[ len( test_sentence ) - 1 ].split( ' ' ) ):
                            if patterns != []:
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]
                            elif patterns == []:
                                patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]
                        else:
                            if patterns != []:
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]
                            elif patterns == []:
                                patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]

        # return patterns
        return patterns

    def find_literal_patterns( self, base_string, test_string, pattern_arg ):
        # Getting the current patterns already found
        patterns = pattern_arg

        # Literal translation from base_string -> test_string
        base_blob = TextBlob( base_string )
        base_sentence_info = []

        # Find patterns
        for sentence in base_blob.sentences:
            words = sentence.split( ' ' )

            for length in xrange( len( words ), 1, -1 ):
                for end in xrange( len( words ), 0, -1 ):
                    if end - length < 0:
                        break

                    pattern = words[ end - length: end ]

                    if ' '.join( pattern ) in str( test_string ):
                        if ' '.join( pattern ) not in patterns:
                            base_sentence_info += [ str( ' '.join( pattern ) ) ]

        patterns += base_sentence_info

        # Literal translation from base_string -> test_string
        test_blob = TextBlob( test_string )
        test_sentence_info = []

        # Find patterns
        for sentence in test_blob.sentences:
            words = sentence.split( ' ' )

            for length in xrange( len( words ), 1, -1 ):
                for end in xrange( len( words ), 0, -1 ):
                    if end - length < 0:
                        break

                    pattern = words[ end - length: end ]

                    if ' '.join( pattern ) in str( base_string ):
                        if ' '.join( pattern ) not in patterns:
                            test_sentence_info += [ str( ' '.join( pattern ) ) ]

        patterns += test_sentence_info

        return patterns

    def find_reliability_score( self, pattern ):
        return 0

    def find_applicability_score( self, pattern ):
        return 0
