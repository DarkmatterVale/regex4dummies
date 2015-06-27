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
        return self.use_nltk( base_string, test_string, pattern_arg )

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
            raw_data              = str( base_sentence )
            pos_sentence          = nltk.pos_tag( nltk.word_tokenize( str( base_sentence ) ) )

            #print raw_data
            #print nltk.pos_tag( nltk.word_tokenize( str( base_sentence ) ) )
            #print "[ Subject ]: " + self.find_subject( str( base_sentence ), raw_data )

            print "***BASE SENTENCE***"
            print "Raw Sentence: " + raw_data
            print "POS Sentence: " + str( pos_sentence )
            print "[ Subject ] : " + self.find_subject( raw_data, pos_sentence )
            print "[ Verb ]    : " + self.find_verb( raw_data, pos_sentence )
            print "[ Object ]  : " + str( self.find_object( raw_data, pos_sentence, pos_sentence ) )

        test_blob = TextBlob( test_string )
        test_sentence_info = []

        for test_sentence in test_blob.sentences:
            subject               = ""
            verb                  = ""
            object                = ""
            prepositional_phrases = ""
            raw_data              = str( test_sentence )
            pos_sentence          = nltk.pos_tag( nltk.word_tokenize( str( test_sentence ) ) )

            print "***TEST SENTENCE***"
            print "Raw Sentence: " + raw_data
            print "POS Sentence: " + str( pos_sentence )
            print "[ Subject ] : " + self.find_subject( raw_data, pos_sentence )
            print "[ Verb ]    : " + self.find_verb( raw_data, pos_sentence )
            print "[ Object ]  : " + str( self.find_object( raw_data, pos_sentence, pos_sentence ) )

        print ""
        print ""

        return "", {}

    def find_subject( self, sentence_raw, sentence_tagged ):
        # Getting full subject
        for index in range( 0, len( sentence_tagged ) ):
            if "VB" in sentence_tagged[ index ][ 1 ]:
                return self.find_subject( ' '.join( sentence_raw.split( ' ' )[ 0 : index ] ), sentence_tagged[ 0 : index ] )

        # Remove excess information
        updated_subject = ""
        for index in range( 0, len( sentence_tagged ) ):
            # Removing prepositions
            if "IN" in sentence_tagged[ index ][ 1 ]:
                for prep_index in range( index, len( sentence_tagged ) ):
                    if "NN" in sentence_tagged[ prep_index ][ 1 ]:
                        if index != 0:
                            updated_subject = ' '.join( sentence_raw.split( ' ' )[ 0 : index ] ) + ' '.join( sentence_raw.split( ' ' )[ prep_index + 1 : len( sentence_raw.split( ' ' ) ) ] )
                            updated_tag = sentence_tagged[ 0 : index ] + sentence_tagged[ prep_index + 1 : len( sentence_tagged ) ]
                        else:
                            updated_subject = ' '.join( sentence_raw.split( ' ' )[ prep_index + 1 : len( sentence_raw.split( ' ' ) ) ] )
                            updated_tag = sentence_tagged[ prep_index + 1 : len( sentence_tagged ) ]

                        updated_subject = self.find_subject( updated_subject, updated_tag )

                        break

                break
            # If there is a noun, add that noun to the subject
            elif "NN" in sentence_tagged[ index ][ 1 ] or "PRP" in sentence_tagged[ index ][ 1 ]:
                if updated_subject == "":
                    updated_subject = sentence_tagged[ index ][ 0 ]
                else:
                    updated_subject += ", " + sentence_tagged[ index ][ 0 ]


        # Return final subject
        return updated_subject

    def find_verb( self, raw_sentence, tagged_sentence ):
        # Creating the variable that will hold the verb(s) of the sentence
        updated_verb = ""

        # Finding verb
        for index in range( 0, len( tagged_sentence ) ):
            if "VB" in tagged_sentence[ index ][ 1 ]:
                if updated_verb == "":
                    updated_verb += tagged_sentence[ index ][ 0 ]
                else:
                    updated_verb += " " + tagged_sentence[ index ][ 0 ]

        # Returning the verb
        return updated_verb

    def find_object( self, raw_sentence, tagged_sentence, full_tagged_sentence ):
        # Creating the variable that will hold the object(s) of the sentence
        updated_object = ""

        # Finding objects
        # Removing the subject and the verb of the sentence
        for index in range( 0, len( tagged_sentence ) ):
            if "VB" in tagged_sentence[ index ][ 1 ]:
                return self.find_object( ' '.join( raw_sentence.split( ' ' )[ index + 1: len( raw_sentence.split( ' ' ) ) ] ), tagged_sentence[ index + 1 : len( tagged_sentence ) ], full_tagged_sentence )

        # Remove excess information
        for index in range( 0, len( tagged_sentence ) ):
            # Removing prepositions
            if "IN" in tagged_sentence[ index ][ 1 ]:
                for prep_index in range( index, len( tagged_sentence ) ):
                    if "NN" in tagged_sentence[ prep_index ][ 1 ]:
                        if index != 0:
                            updated_object = ' '.join( raw_sentence.split( ' ' )[ 0 : index ] ) + ' '.join( raw_sentence.split( ' ' )[ prep_index + 1 : len( raw_sentence.split( ' ' ) ) ] )
                            updated_tag = tagged_sentence[ 0 : index ] + tagged_sentence[ prep_index + 1 : len( tagged_sentence ) ]
                        else:
                            updated_object = ' '.join( raw_sentence.split( ' ' )[ prep_index + 1 : len( raw_sentence.split( ' ' ) ) ] )
                            updated_tag = tagged_sentence[ prep_index + 1 : len( tagged_sentence ) ]

                        updated_object = self.find_object( updated_object, updated_tag, full_tagged_sentence )

                        break

                break
            elif "NN" in tagged_sentence[ index ][ 1 ] or "PRP" in tagged_sentence[ index ][ 1 ]:
                if index + 1 < len( tagged_sentence ):
                    if "CC" in tagged_sentence[ index + 1 ][ 1 ]:
                        compound_object = tagged_sentence[ index ][ 0 ] + " " + tagged_sentence[ index + 1 ][ 0 ]

                        for compound_index in range( index + 1, len( tagged_sentence ) ):
                            if "NN" in tagged_sentence[ compound_index ][ 1 ] or "PRP" in tagged_sentence[ compound_index ][ 1 ]:
                                compound_object += " " + tagged_sentence[ compound_index ][ 0 ]

                                break
                        if updated_object == "":
                            updated_object = compound_object + ", "
                        else:
                            updated_object += " " + compound_object

                if "CC" not in tagged_sentence[ index - 1 ][ 1 ]:
                    if updated_object == "":
                        updated_object = tagged_sentence[ index ][ 0 ]
                    else:
                        add_to_updated_object, new_object = self.find_previous_instance( [ "NN", "PRP" ], full_tagged_sentence, len( full_tagged_sentence ) - ( len( tagged_sentence ) - index ), [ "VB" ], updated_object )

                        updated_object = new_object
                        """if add_to_updated_object == "True":
                            print new_object
                            print updated_object
                            updated_object = new_object + tagged_sentence[ index ][ 0 ]
                        else:
                            updated_object = new_object
            elif "CC" in tagged_sentence[ index ][ 1 ]:
                compound_object = tagged_sentence[ index - 1 ][ 0 ] + " " + tagged_sentence[ index ][ 0 ]

                for compound_index in range( index, len( tagged_sentence ) ):
                    if "NN" in tagged_sentence[ compound_index ][ 1 ] or "PRP" in tagged_sentence[ compound_index ][ 1 ]:
                        compound_object += " " + tagged_sentence[ compound_index ][ 0 ]

                        break
                if updated_object == "":
                    updated_object = compound_object + ", "
                else:
                    updated_object += compound_object"""

        # Returning the objects found
        return updated_object

    def find_previous_instance( self, instance_to_find, string_containing_instance, current_index, objects_to_fail, updated_object ):
        is_word_found = "False"

        for index in xrange( current_index - 1, 0, -1 ):
            for fail in objects_to_fail:
                if fail in string_containing_instance[ index ][ 1 ]:
                    return is_word_found, updated_object

            for find in instance_to_find:
                if find in string_containing_instance[ index ][ 1 ]:
                    if index + 1 > len( string_containing_instance ):
                        if "CC" not in string_containing_instance[ index - 1 ][ 1 ]:
                            is_word_found = "True"
                            updated_object = re.sub( string_containing_instance[ index ][ 0 ], "", updated_object )
                    elif index - 1 < 0:
                        if "CC" not in string_containing_instance[ index + 1 ][ 1 ]:
                            is_word_found = "True"
                            updated_object = re.sub( string_containing_instance[ index ][ 0 ], "", updated_object )
                    else:
                        if "CC" not in string_containing_instance[ index + 1 ][ 1 ] and "CC" not in string_containing_instance[ index - 1 ][ 1 ]:
                            is_word_found = "True"
                            updated_object = re.sub( string_containing_instance[ index ][ 0 ], "", updated_object )

        return is_word_found, updated_object

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
