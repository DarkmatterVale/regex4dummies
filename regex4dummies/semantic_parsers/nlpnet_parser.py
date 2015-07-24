__author__ = 'Vale Tolpegin'

"""

Class information:

- Name: NLPNET
- Version: 1.3.5

NLPNET is used to manage the nlpnet parser

"""

import re
from subprocess import *

from textblob import TextBlob
import nlpnet


class NLPNET:


    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def use_nlpnet( self, base_string, test_string, pattern_arg ):
        """ Main interface method from the NLPNET class to the rest of the program """

        # Getting nltk data path
        running = Popen( [ 'python -c "import nltk;print nltk.data.path"' ], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True )
        stdin, stdout = running.communicate()

        # Setting the path that the nlpnet dependency was downloaded to
        path = re.sub( r"\'", "", re.sub( r"\[", '', str( stdin.split( '\n' )[ 0 ].split( ',' )[ 0 ] ) ) )
        path = path.split( r"/" )
        path = '/'.join( path[ 0 : len( path ) - 1 ] ) + '/nlpnet_dependency/dependency'

        # Setting up the nlpnet parser
        nlpnet.set_data_dir( path )
        dependency_parser = nlpnet.DependencyParser()
        pos_parser = nlpnet.POSTagger()

        # Getting the passed patterns
        patterns = pattern_arg

        # Parsing the base_string
        base_parse = dependency_parser.parse( base_string )
        base_blob = TextBlob( base_string )
        base_sentences = base_blob.sentences
        base_sentence_info = []

        for index in range( 0, len( base_parse ) ):
            # Grabbing sentence information
            raw_data = str( base_sentences[ index ] )
            pos_sentence = pos_parser.tag( str( base_sentences[ index ] ) )
            subject, verb, object, prepositional_phrases = self.identify_sentence_parts_nlpnet( base_parse[ index ].tokens, base_parse[ index ].labels )

            # Displaying information for debugging purposes
            #print "***BASE***"
            #print "Raw Sentence     : " + raw_data
            #print "POS Sentence    : " + str( pos_sentence )
            #print "[ Tokens ]       : " + str( base_parse[ index ].tokens )
            #print "[ Labels ]       : " + str( base_parse[ index ].labels )
            #print "[ Subject ]     : " + subject
            #print "[ Verb ]        : " + verb
            #print "[ Object ]      : " + object
            #print "[ Prep Phrases ] : " + str( prepositional_phrases )

            # Deciding whether the sentence/pattern should be added
            add_sentence = True
            for sentence in base_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) ] == raw_data:
                        add_sentence = False

                        break

            # If the sentence should be added to the possible patterns, add it
            if add_sentence:
                base_sentence_info.append( [ subject, verb, object, [], raw_data ] )

        # Parsing the test_string
        test_parse = dependency_parser.parse( test_string )
        test_blob = TextBlob( test_string )
        test_sentences = test_blob.sentences
        test_sentence_info = []

        for index in range( 0, len( test_parse ) ):
            # Grabbing sentence information
            raw_data = str( test_sentences[ index ] )
            pos_sentence = pos_parser.tag( str( test_sentences[ index ] ) )
            subject, verb, object, prepositional_phrases = self.identify_sentence_parts_nlpnet( test_parse[ index ].tokens, test_parse[ index ].labels )

            #print "***TEST***"
            #print "Raw Sentence     : " + raw_data
            #print "POS Sentence    : " + str( pos_sentence )
            #print "[ Tokens ]       : " + str( test_parse[ index ].tokens )
            #print "[ Labels ]       : " + str( test_parse[ index ].labels )
            #print "[ Subject ]     : " + subject
            #print "[ Verb ]        : " + verb
            #print "[ Object ]      : " + object
            #print "[ Prep Phrases ] : " + str( prepositional_phrases )


            # Deciding whether the sentence/pattern should be added
            add_sentence = True
            for sentence in test_sentence_info:
                if sentence != []:
                    if sentence[ len( sentence ) ] == raw_data:
                        add_sentence = False

                        break

            # If the sentence should be added to the possible patterns, add it
            if add_sentence:
                test_sentence_info.append( [ subject, verb, object, [], raw_data ] )

        # Returning the patterns found in the text
        return self.identify_common_patterns( base_sentence_info, test_sentence_info, patterns )

    def identify_sentence_parts_nlpnet( self, tokens, labels ):
        subject               = ""
        verb                  = ""
        object                = ""
        prepositional_phrases = ""

        for index in range( 0, len( labels ) ):
            if "SBJ" in labels[ index ] and verb == "":
                subject += tokens[ index ] + " "
            elif "ROOT" in labels[ index ]:
                verb += tokens[ index ]
            elif "PRD" in labels[ index ] or "OBJ" in labels[ index ]:
                object += tokens[ index ] + " "
            elif "LOC" in labels[ index ]:
                for prep_index in range( index, len( labels ) ):
                    if "PMOD" in labels[ prep_index ] and ' '.join( tokens[ index : prep_index + 1 ] ) not in prepositional_phrases:
                        prepositional_phrases += ' '.join( tokens[ index : prep_index + 1 ] ) + "..."

                        break


        return subject, verb, object, prepositional_phrases.split( "..." )


    def normalize_sentence_info( self, sentence_info ):
        """ Normalizes all of the incoming text to a standard """

        # Create a stemmer object
        stemmer = PorterStemmer()

        # Normalizing sthe patterns
        # Make the subject, verb, and object lowercase
        sentence_info[0] = sentence_info[0].lower()
        sentence_info[1] = sentence_info[1].lower()
        sentence_info[2] = sentence_info[2].lower()

        # Implement stemming
        sentence_info[0] = stemmer.stem( sentence_info[0] )
        sentence_info[1] = stemmer.stem( sentence_info[1] )
        sentence_info[2] = stemmer.stem( sentence_info[2] )

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
                                sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 100 )

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

                                    # Adding applicability score
                                    try:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 5 ] = 100
                                    except:
                                        sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 100 )
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
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ][ 5 ] = 100
                                except:
                                    sentence_information[ base_sentence[ len( base_sentence ) - 1 ] ].append( 100 )
                        else:
                            # If there are patterns already found
                            if patterns != []:
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ] = test_sentence[ 0 : len( test_sentence ) - 1 ]
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 2 )
                                sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 100 )

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

                                    # Adding applicability score
                                    try:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 5 ] = 100
                                    except:
                                        sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 100 )
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
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ][ 5 ] = 100
                                except:
                                    sentence_information[ test_sentence[ len( test_sentence ) - 1 ] ].append( 100 )

        return patterns, sentence_information
