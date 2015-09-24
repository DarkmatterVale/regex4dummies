__author__ = 'Vale Tolpegin'

"""

Class information:

- Name: NLTK
- Version: 1.4.3

NLTK is used to manage the NLTK parser

"""

import re
import os

from textblob import TextBlob
import nltk
from fuzzywuzzy import fuzz

from normalizer import Normalizer


class NLTK:
    global nltk_normalizer

    def __init__( self, *args, **kwargs ):
        """
        Constructor method, initializes variables.
        """

        global nltk_normalizer

        # Initializing variables
        nltk_normalizer = Normalizer()


    def tokenize( self, tokenize_string ):
        """ Returns the tokenized version of tokenize_string, which is just a normal English sentence """

        return nltk.pos_tag( nltk.word_tokenize( tokenize_string ) )


    def find_dependencies( self, dependency_string ):
        """ Returns dependency_string with sentence dependencies included """

        pos_sentence = nltk.pos_tag( nltk.word_tokenize( dependency_string ) )
        subject = self.find_subject( dependency_string, dependency_string.lower(), pos_sentence )
        verb    = self.find_verb( dependency_string, dependency_string.lower(), pos_sentence )
        sentence_object  = self.find_object( dependency_string, dependency_string.lower(), pos_sentence, pos_sentence )

        return [ ["subject", subject], ["verb", verb], ["object", sentence_object] ]


    def use_nltk( self, base_string, test_string, pattern_arg ):
        patterns = pattern_arg

        base_blob = TextBlob( base_string )
        base_sentence_info = []

        for base_sentence in base_blob.sentences:
            capitalized_data = base_sentence
            base_sentence = base_sentence.lower()

            raw_data              = str( base_sentence )
            pos_sentence          = nltk.pos_tag( nltk.word_tokenize( str( base_sentence ) ) )
            subject               = self.find_subject( capitalized_data, raw_data, pos_sentence )
            verb                  = self.find_verb( capitalized_data, raw_data, pos_sentence )
            object                = self.find_object( capitalized_data, raw_data, pos_sentence, pos_sentence )
            prepositional_phrases = self.find_prepositional_phrases( capitalized_data, raw_data, pos_sentence )
            prepositional_phrases = prepositional_phrases.split( '...' )

            #print "***BASE SENTENCE***"
            #print "Raw Sentence     : " + raw_data
            #print "POS Sentence     : " + str( pos_sentence )
            #print "[ Subject ]      : " + subject
            #print "[ Verb ]         : " + verb
            #print "[ Object ]       : " + str( object )
            #print "[ Prep Phrases ] : " + str( prepositional_phrases )

            add_sentence = True
            for sentence in base_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) - 1 ] == str( base_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                base_sentence_info.append( [ subject, verb, object, prepositional_phrases, str( base_sentence ) ] )

        test_blob = TextBlob( test_string )
        test_sentence_info = []

        for test_sentence in test_blob.sentences:
            capitalized_data = test_sentence
            test_sentence = test_sentence.lower()

            raw_data              = str( test_sentence )
            pos_sentence          = nltk.pos_tag( nltk.word_tokenize( str( test_sentence ) ) )
            subject               = self.find_subject( capitalized_data, raw_data, pos_sentence )
            verb                  = self.find_verb( capitalized_data, raw_data, pos_sentence )
            object                = self.find_object( capitalized_data, raw_data, pos_sentence, pos_sentence )
            prepositional_phrases = self.find_prepositional_phrases( capitalized_data, raw_data, pos_sentence )
            prepositional_phrases = prepositional_phrases.split( '...' )

            #print "***TEST SENTENCE***"
            #print "Raw Sentence     : " + raw_data
            #print "POS Sentence     : " + str( pos_sentence )
            #print "[ Subject ]      : " + subject
            #print "[ Verb ]         : " + verb
            #print "[ Object ]       : " + str( object )
            #print "[ Prep Phrases ] : " + str( prepositional_phrases )

            add_sentence = True
            for sentence in test_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) - 1 ] == str( test_sentence ):
                        add_sentence = False

                        break

            if add_sentence:
                test_sentence_info.append( [ subject, verb, object, prepositional_phrases, str( test_sentence ) ] )

        return self.identify_common_patterns( base_sentence_info, test_sentence_info, patterns )


    #def separate_clauses( self, sentence ):
    #    """ Independent and dependent clauses must be separated. Otherwise, the parser will get skewed results. This method accomplishes that """

    #    # Setting up variables containing sentence information
    #    clauses = []

    #    # Until all of the clauses have been separated, continue separating the clauses within a sentence
    #    while True:
    #        sentence_verb = self.find_verb( sentence )
    #        if sentence_verb != "":


    #    return clauses


    def find_subject( self, capitalized_sentence, sentence_raw, sentence_tagged ):
        # Getting full subject
        for index in range( 0, len( sentence_tagged ) ):
            if "VB" in sentence_tagged[ index ][ 1 ]:
                return self.find_subject( capitalized_sentence, ' '.join( sentence_raw.split( ' ' )[ 0 : index ] ), sentence_tagged[ 0 : index ] )

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

                        updated_subject = self.find_subject( capitalized_sentence, updated_subject, updated_tag )

                        break

                break
            # If there is a noun, add that noun to the subject
            elif "NN" in sentence_tagged[ index ][ 1 ] or "PRP" in sentence_tagged[ index ][ 1 ]:
                if updated_subject == "":
                    updated_subject = sentence_tagged[ index ][ 0 ]
                else:
                    updated_subject += ", " + sentence_tagged[ index ][ 0 ]

        # Correcting any spelling errors
        for word in capitalized_sentence.split( ' ' ):
            if word.lower() in updated_subject:
                updated_subject = re.sub( word.lower(), word, updated_subject )

        # Return final subject
        return updated_subject


    def find_verb( self, capitalized_sentence, raw_sentence, tagged_sentence ):
        # Creating the variable that will hold the verb(s) of the sentence
        updated_verb = ""

        # Finding verb
        for index in range( 0, len( tagged_sentence ) ):
            if "VB" in tagged_sentence[ index ][ 1 ]:
                if updated_verb == "":
                    updated_verb += tagged_sentence[ index ][ 0 ]
                else:
                    updated_verb += " " + tagged_sentence[ index ][ 0 ]

        # Determing if it is a compound verb. If so, generating the final verb correctly
        if len( updated_verb.split( ' ' ) ) >= 1:
            if len( updated_verb.split( ' ' ) ) == 1:
                pass
            elif len( updated_verb.split( ' ' ) ) == 2:
                # Splitting the verbs into sub verbs
                updated_verb = updated_verb.split( ' ' )

                # Since there are only two, a single conjunction can be used to bring the two together
                updated_verb[ 0 ] = updated_verb[ 0 ] + " and"

                updated_verb = ' '.join( updated_verb )
            else:
                # Splitting the verbs into sub verbs
                updated_verb = updated_verb.split( ' ' )

                # Correctly bringing all of those verbs together ( adding commas )
                for index in range( 0, len( updated_verb ) - 2 ):
                    updated_verb[ index ] = updated_verb[ index ] + ","

                # Adding a conjunction between the second-to-last and last verbs
                updated_verb[ len( updated_verb ) - 2 ] = updated_verb[ len( updated_verb ) - 2 ] + " and"

                updated_verb = ' '.join( updated_verb )

        # Correcting any spelling errors
        for word in capitalized_sentence.split( ' ' ):
            if word.lower() in updated_verb:
                updated_verb = re.sub( word.lower(), word, updated_verb )

        # Returning the verb
        return updated_verb


    def find_object( self, capitalized_sentence, raw_sentence, tagged_sentence, full_tagged_sentence ):
        # Creating the variable that will hold the object(s) of the sentence
        updated_object = ""

        # Finding objects
        # Removing the subject and the verb of the sentence
        for index in range( 0, len( tagged_sentence ) ):
            if "VB" in tagged_sentence[ index ][ 1 ]:
                return self.find_object( capitalized_sentence, ' '.join( raw_sentence.split( ' ' )[ index + 1: len( raw_sentence.split( ' ' ) ) ] ), tagged_sentence[ index + 1 : len( tagged_sentence ) ], full_tagged_sentence )

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

                        updated_object = self.find_object( capitalized_sentence, updated_object, updated_tag, full_tagged_sentence )

                        break

                break
            elif "NN" in tagged_sentence[ index ][ 1 ] or "PRP" in tagged_sentence[ index ][ 1 ]:
                if index + 1 < len( tagged_sentence ):
                    if "CC" in tagged_sentence[ index + 1 ][ 1 ]:
                        compound_object = tagged_sentence[ index ][ 0 ]

                        for compound_index in range( index + 1, len( tagged_sentence ) ):
                            if "NN" in tagged_sentence[ compound_index ][ 1 ] or "PRP" in tagged_sentence[ compound_index ][ 1 ]:
                                compound_object +=  " " + tagged_sentence[ index + 1 ][ 0 ] + " " + tagged_sentence[ compound_index ][ 0 ]

                                break
                        if updated_object == "":
                            updated_object = compound_object + ", "
                        else:
                            add_to_updated_object, new_object = self.find_previous_instance( [ "NN", "PRP" ], full_tagged_sentence, len( full_tagged_sentence ) - ( len( tagged_sentence ) - index ), [ "VB" ], updated_object + compound_object )

                            updated_object = new_object

                if "CC" not in tagged_sentence[ index - 1 ][ 1 ]:
                    if updated_object == "":
                        updated_object = tagged_sentence[ index ][ 0 ]
                    elif tagged_sentence[ index - 1 ][ 0 ] not in updated_object:
                        add_to_updated_object, new_object = self.find_previous_instance( [ "NN", "PRP" ], full_tagged_sentence, len( full_tagged_sentence ) - ( len( tagged_sentence ) - index ), [ "VB" ], updated_object )

                        if add_to_updated_object == "True":
                            updated_object = new_object + tagged_sentence[ index ][ 0 ]
                        else:
                            updated_object = new_object

        # Correcting any spelling errors
        for word in capitalized_sentence.split( ' ' ):
            if word.lower() in updated_object:
                updated_object = re.sub( word.lower(), word, updated_object )

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
                    updated_object = re.sub( string_containing_instance[ index ][ 0 ], "", updated_object )
                    is_word_found = "True"

        return is_word_found, updated_object


    def find_prepositional_phrases( self, capitalized_sentence, raw_sentence, tagged_sentence ):
        prepositional_phrases = ""

        for index in range( 0, len( tagged_sentence ) ):
            # Removing prepositions
            if "IN" in tagged_sentence[ index ][ 1 ]:
                for prep_index in range( index, len( tagged_sentence ) ):
                    if "NN" in tagged_sentence[ prep_index ][ 1 ]:
                        if index != 0:
                            temporary_phrase = ""
                            for phrase_index in range( index, prep_index + 1 ):
                                temporary_phrase += " " + tagged_sentence[ phrase_index ][ 0 ]

                            if temporary_phrase not in prepositional_phrases:
                                prepositional_phrases += temporary_phrase + "..."

                        break

        return prepositional_phrases


    def normalize_sentence_info( self, sentence_info ):
        """ Normalizes all of the incoming text to a standard """

        global nltk_normalizer

        # Normalizing text
        sentence_info = nltk_normalizer.normalize_sentence_info( sentence_info )

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
