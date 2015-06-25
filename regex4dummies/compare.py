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
    global sentence_information

    # Empty constructor
    def __init__( self, *args, **kwargs ):
        pass

    # This method is called by the main regex4dummies class, and calls all further methods to find strings
    def compare_strings( self, strings, literal ):
        # Getting global variables
        global sentence_information

        # Reset variables
        patterns = []
        sentence_information = {}

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
                    compiled_patterns += [ 0, 0, pattern ]
            else:
                compiled_patterns += [ 0, 0, pattern ]

        return compiled_patterns

    # Recursive function that compares all strings and determins reliability score, applicability score, and pattern
    def find_patterns( self, strings, current_index, literal_find, patterns_arg ):
        patterns = patterns_arg

        if not literal_find:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, False, patterns_arg )

            for index in xrange( current_index, -1, -1 ):
                if strings[ index ] != strings[ current_index ]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.identify_patterns( strings[ current_index ], strings[ index ], patterns )
        else:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, True, patterns_arg )

            # for index in range( current_index, len( strings ) - 1 ):
            for index in xrange( current_index, -1, -1 ):
                if strings[ index ] != strings[ current_index ]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.find_literal_patterns( strings[ current_index ], strings[ index ], patterns )

        # return patterns
        return patterns

    # This function identifies patterns in 2 strings
    def identify_patterns( self, base_string, test_string, pattern_arg ):
        # Getting global variables
        global sentence_information

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
                # If there are two sentences/patterns to compare
                if base_sentence != [] and test_sentence != []:
                    # If the patterns' semantic "value" is the same
                    if base_sentence[0] == test_sentence[0] and base_sentence[1] == test_sentence[1] and base_sentence[2] == test_sentence[2]:
                        # If one sentence/pattern is longer than the other, use that pattern
                        if len( base_sentence[ len( base_sentence ) - 1 ].split( ' ' ) ) > len( test_sentence[ len( test_sentence ) - 1 ].split( ' ' ) ):
                            # If other patterns have been detected
                            if patterns != []:
                                # If the current test patterns are not in patterns
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]

                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ] = base_sentence[ 0 : len( base_sentence ) - 2 ]
                                elif base_sentence[ len( base_sentence ) - 1 ] in patterns:
                                    # Updating reliability score
                                    try:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 3 ] += 1
                                    except:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 1 )
                            # If there are no patterns currently found, add this pattern
                            elif patterns == []:
                                patterns += [ base_sentence[ len( base_sentence ) - 1 ] ]

                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ] = base_sentence[ 0 : len( base_sentence ) - 2 ]
                                # Updating reliability score
                                try:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 3 ] += 1
                                except:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 1 )
                        else:
                            # If there are patterns already found
                            if patterns != []:
                                # If the test patterns are not in the already found patterns
                                if test_sentence[ len( test_sentence ) - 1 ] not in patterns and base_sentence[ len( base_sentence ) - 1 ] not in patterns:
                                    patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]

                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 2 ]
                                elif test_sentence[ len( test_sentence ) - 1 ] in patterns:
                                    # Updating reliability score
                                    try:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 3 ] += 1
                                    except:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 1 )
                            # If there are no patterns currently found
                            elif patterns == []:
                                patterns += [ test_sentence[ len( test_sentence ) - 1 ] ]

                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 2 ]
                                # Updating reliability score
                                try:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 3 ] += 1
                                except:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 1 )

        # return patterns
        return patterns

    def find_literal_patterns( self, base_string, test_string, pattern_arg ):
        # Getting global variables
        global sentence_information

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

                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', 1 ]
                        else:
                            sentence_information[ str( ' '.join( pattern ) ) ][ 3 ] += 1

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
                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', 1 ]

                            test_sentence_info += [ str( ' '.join( pattern ) ) ]
                        else:
                            sentence_information[ str( ' '.join( pattern ) ) ][ 3 ] += 1

        patterns += test_sentence_info

        return patterns

    # If semantic pattern finding was implemented, the following will be returned
    # Every sentence contains different parts of speech. This method returns those parts of speech in the following order:
    #   1. Subject
    #   2. Verb
    #   3. [Direct] Object
    # An example, might look like this:
    #   { "The sentence here" : [ "my_subject", "my_verb", "my_object" ] }
    def get_sentence_information( self ):
        global sentence_information

        return sentence_information
