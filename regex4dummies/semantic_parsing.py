__author__ = 'Vale Tolpegin'

from pattern.en import parse
from textblob.parsers import PatternParser
from textblob import TextBlob
import re
import nltk

class semantic_parsing:
    def __init__( self, *args, **kwargs ):
        pass

    def parse( self, base_string, test_string, pattern_arg ):
        return self.use_pattern( base_string, test_string, pattern_arg )

    def use_nltk( self, base_string, test_string, pattern_arg ):
        sentence_information = {}
        patterns = pattern_arg

        base_blob = TextBlob( base_string )
        base_sentenc_info = []

        for base_sentence in base_blob.sentences:
            subject               = ""
            verb                  = ""
            object                = ""
            prepositional_phrases = ""
            raw_data              = nltk.ne_chunk( nltk.pos_tag( nltk.word_tokenize( str( base_sentence ) ) ), binary=True )

            print raw_data
            print nltk.pos_tag( nltk.word_tokenize( str( base_sentence ) ) )

        test_blob = TextBlob( test_string )
        test_sentence_info = []

        for test_sentence in test_blob.sentences:
            subject               = ""
            verb                  = ""
            object                = ""
            prepositional_phrases = ""
            raw_data              = nltk.pos_tag( nltk.word_tokenize( str( test_sentence ) ) )

            print raw_data

        print ""
        print ""

        return "YOLO", { "YOLONAME" : "YOLO", "YOLO2NAME" : "YOLO1" }

    def use_pattern( self, base_string, test_string, pattern_arg ):
        sentence_information = {}
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

        return patterns, sentence_information
