__author__ = 'Vale Tolpegin'

import os

from pattern.en import parse
from textblob import TextBlob
import nltk
import nlpnet

# Importing required libraries
from regex4dummies import regex4dummies

"""

Class information:

- name: main
- version: 1.3.7

This is an accuracy tester for regex4dummies. It will test all components of the library and determine how effective it is at accomplishing its goal

"""

class Main:
    # Global variables
    global overall_score
    global pattern_score
    global pattern_score_info
    global nltk_score
    global nltk_score_info
    global nlpnet_score
    global nlpnet_score_info
    global literal_score
    global literal_score_info
    global tri_parser_score
    global tri_parser_score_info


    def __init__( self, *args, **kwargs ):
        """ Constructor method that will complete the tests and display the results """

        # Getting global variables
        global overall_score
        global pattern_score
        global pattern_score_info
        global nltk_score
        global nltk_score_info
        global nlpnet_score
        global nlpnet_score_info
        global literal_score
        global literal_score_info
        global tri_parser_score
        global tri_parser_score_info

        # Currently implemented functions that will be tested
        # This program performs a number of accuracy tests against the library. THey are:
        # 1. Each individual parser is tested
        #   a. Are the subject, verb, object, and prepositional phrases properly identified?
        #   b. Are the applicability score and the reliability score properly calculated?
        #   c. Are all of the patterns identified?
        #   d. Is everything pertaining to the literal parser properly identified?
        # 2. All 3 parsers in one function call
        #   a. Are all of the patterns identified?
        #   b. Are the subject, verb, object, and prepositional phrases properly identified?
        #   c. Are the applicability score and the reliability score properly calculated?

        # Weighting of each aspect of the final score ( from the above list )
        # #1: 75%
        # #2: 25%
        # The test sets total up to 100%, giving a complete score. This score is meant to represent
        #   how important each aspect of the library is relative to the other aspects of the library.

        print ""
        print "*" * 75
        print "regex4dummies Accuracy Tester"
        print ""
        print "Each test is valued in the following way ( 0 - 100 ): "
        print "* 100 - 90     : regex4dummies is consistently performing well and should be able to handle complex data"
        print "* 89 - 80      : regex4dummies is performing well, but does not perform well consistently and probably cannot handle very complicated data"
        print "* 79 - 70      : regex4dummies' performance is consistently poor and regex4dummies is probably not capable of parsing compex strings"
        print "* 69 and below : regex4dummies is doing poorly and is considered still under development"
        print ""
        print "Please understand that these scores will not be a very accurate representation of regex4dummies' performance across the board. English is complicated and it is difficult to test every possible 'kind' of sentence."
        print "*" * 75
        print ""
        print "***Beginning Tests***"

        # Completing tests
        self.complete_tests()

        print "***Tests Completed***"
        print ""
        print ""
        print "***Score information***"
        print "Overall Score    : " + str( overall_score )
        print ""
        print "NLTK Score       : " + str( nltk_score )
        print "Pattern Score    : " + str( pattern_score )
        print "nlpnet Score     : " + str( nlpnet_score )
        print "Literal Score    : " + str( literal_score )
        print "Tri-parser Score : " + str( tri_parser_score )
        print ""

        # Showing other test-related information
        print "NLTK test details       "
        print "------------------------"
        print nltk_score_info
        print ""

        print "Pattern test details    "
        print "------------------------"
        print pattern_score_info
        print ""

        print "nlpnet test details     "
        print "------------------------"
        print nlpnet_score_info
        print ""

        print "Literal test details    "
        print "------------------------"
        print literal_score_info
        print ""

        print "Tri-parser test details "
        print "------------------------"
        print tri_parser_score_info
        print ""

        print ""


    def complete_tests( self ):
        """ This function will perform the above tests, and set the appropriate variables with test information """

        # Getting global variables
        global overall_score
        global pattern_score
        global pattern_score_info
        global nltk_score
        global nltk_score_info
        global nlpnet_score
        global nlpnet_score_info
        global literal_score
        global literal_score_info
        global tri_parser_score
        global tri_parser_score_info

        # Setting all of the scores to restart
        overall_score    = 0
        nltk_score       = 0
        pattern_score    = 0
        nlpnet_score     = 0
        literal_score    = 0
        tri_parser_score = 0

        nltk_score_info       = ""
        pattern_score_info    = ""
        nlpnet_score_info     = ""
        literal_score_info    = ""
        tri_parser_score_info = ""

        # Creating test-containing strings
        # TODO: Increase "corpora" size & add much more data to test
        test_1 = "This is the first test string. Cats are very unique animals. In addition to being pets, they are wild animals. There are a number of different kinds of cats. Lions and cheetahs included, there are three kinds of cats."
        test_2 = "This is the second test string. Dogs, unlike cats, are not a unique kind of animal. Dogs are pets, wild animals, and some are even in between being wild and pets. Unlike cats, there are many different kinds of dogs. Wolves, for instance, are a kind of dog."
        test_3 = "This is the third test string. This string is about computers. Many people argue that artificially intelligent computers will take over the world. In fact, I disagree with this view. I believe that computers will not turn against us."
        test_4 = "This is the fourth test string. Like the last string, this string is about computers and is a continuation of the last conversation. Computers are very likely to instead help us. Although many scientists believe that I am incorrect, a number of other very smart scientists agree with me."

        """
        Tests to make sure the above strings work without any issues/bugs arising.

        regex = regex4dummies()

        # Printing the semantic patterns within this string
        print "Patterns: " + str( regex.compare_strings( 'nlpnet', False, [ test_1, test_2, test_3, test_4 ] ) )

        # Displaying the topics that were identified by the parsers in the most recently compared set of strings
        print "Topics: " + str( regex.get_pattern_topics() )
        print ""

        # Displaying all of the "meaning" in these sentences
        sentence_information = regex.get_sentence_information()
        for sentence in sentence_information:
            print "[ Pattern ]            : " + sentence.pattern
            print "[ Subject ]            : " + sentence.subject
            print "[ Verb ]               : " + sentence.verb
            print "[ Object ]             : " + sentence.object[0]
            print "[ Prep Phrases ]       : " + str( sentence.prepositional_phrases )
            print "[ Reliability Score ]  : " + str( sentence.reliability_score )
            print "[ Applicability Score ]: " + str( sentence.applicability_score )
            print ""
        #"""

        # Creating correct information
        correct_patterns            = [ 100, 100, "This is the first test string.", 100, 100, "This is the second test string.", 100, 100, "This is the third test string." ]
        correct_pattern_information = { "This is the first test string." : ["This", "is", "string", [], 75, 100], "This is the second test string." : ["This", "is", "string", [], 75, 100], "This is the third test string." : ["This", "is", "string", [], 75, 100] }
        correct_topics = [ "cats", "dogs", "computers" ]

        correct_literal_patterns    = [ [ 0, 100, "This is" ], [ 0, 100, "This is the" ], [ 0, 100, "test string." ], [ 0, 100, "is about computers" ], [ 0, 100, "this string" ], [ 0, 100, "about computers" ], [ 0, 100, "kinds of" ], [ 0, 100, "are a" ], [ 0, 100, "is the" ], [ 0, 100, "string is" ] ]

        # ************************************************************
        # Beginning tests
        # ************************************************************

        # Structure of the correct information
        # The correct information is in this format:
        # [ [ patterns ] ]
        # 1. First array ( [ patterns ] ):
        #   a. pattern_detail object(s) containing patterns

        # Processing the raw data for the nltk parser
        print "Beginning nltk tests"
        nltk_score, nltk_score_info = self.process_raw_data_semantic( "nltk", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print "nltk tests completed"

        # Processing the raw data for the pattern parser
        print "Beginning pattern tests"
        pattern_score, pattern_score_info = self.process_raw_data_semantic( "pattern", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print "pattern tests completed"

        # Processing the raw data for the nlpnet parser
        print "Beginning nlpnet tests"
        nlpnet_score, nlpnet_score_info = self.process_raw_data_semantic( "nlpnet", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print "nlpnet tests completed"

        # Processing the raw data for the literal parser
        print "Beginning literal parser tests"
        literal_score, literal_score_info = self.process_raw_data_literal( "default", [test_1, test_2, test_3, test_4], correct_literal_patterns )
        print "literal parser tests completed"

        print "Beginning tri-parser tests"
        tri_parser_score, tri_parser_score_info = self.process_raw_data_semantic( "", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print "tri-parser tests completed"

        overall_score = ( ( nltk_score + pattern_score + nlpnet_score + literal_score ) / 4 ) * 0.75
        overall_score += tri_parser_score * 0.25


    def process_raw_data_semantic( self, parser_name, information, correct_topics ):
        """ This function processes the raw data and turns it into useful information.
            That data provides useful statistics about the library's current "health".
            The function returns the overall score for the data, and specific statistics of the data """

        regex = regex4dummies()

        # Getting the semantic patterns within the test strings
        regex.compare_strings( parser_name, False, information[ 0 ] )

        # Identifying topics discovered by the parsers in the most recently compared set of strings
        test_topics = regex.get_pattern_topics()

        # Gathering and comparing the "meaning" in these sentences
        test_information = {}
        sentence_information = regex.get_sentence_information()
        for sentence in sentence_information:
            # Getting information from the test sentence
            test_pattern = sentence.pattern
            test_subject = sentence.subject
            test_verb = sentence.verb
            test_object = sentence.object[0]
            test_prepositional_phrases = sentence.prepositional_phrases
            test_reliability_score = sentence.reliability_score
            test_applicability_score = sentence.applicability_score

            test_information[ test_pattern ] = [ test_subject, test_verb, test_object, test_prepositional_phrases, test_reliability_score, test_applicability_score ]

        compatibility_score = 0.00
        compare_index = 0
        for pattern in information[1]:
            base_pattern               = pattern
            base_subject               = information[1][base_pattern][0]
            base_verb                  = information[1][base_pattern][1]
            base_object                = information[1][base_pattern][2]
            base_prepositional_phrases = information[1][base_pattern][3]
            base_reliability_score     = information[1][base_pattern][4]
            base_applicability_score   = information[1][base_pattern][5]

            try:
                test_pattern               = base_pattern
                test_subject               = test_information[ test_pattern ][ 0 ]
                test_verb                  = test_information[ test_pattern ][ 1 ]
                test_object                = test_information[ test_pattern ][ 2 ]
                test_prepositional_phrases = test_information[ test_pattern ][ 3 ]
                test_reliability_score     = test_information[ test_pattern ][ 4 ]
                test_applicability_score   = test_information[ test_pattern ][ 5 ]

                if test_subject == base_subject:
                    compatibility_score += 70 / 6
                if test_verb == base_verb:
                    compatibility_score += 70 / 6
                if test_object == base_object:
                    compatibility_score += 70 / 6
                if test_prepositional_phrases == base_prepositional_phrases:
                    compatibility_score += 70 / 6
                if test_reliability_score == base_reliability_score:
                    compatibility_score += 70 / 6
                if test_applicability_score == base_applicability_score:
                    compatibility_score += 70 / 6
            except:
                compare_index += 1

                # The pattern was not in the gathered data. The score will not have anything additional added to it, and the loop will continue
                continue

            # Comparing and generating score
            compare_index += 1

        # Generating the semantic score
        compatibility_score = compatibility_score / compare_index

        # Comparing topics & Generating topic score
        for topic in correct_topics:
            if topic in test_topics:
                compatibility_score += 30 / len( correct_topics )

        compatibility_score_info = str( test_information ) + "\n\n"
        compatibility_score_info += str( information[1] )

        # Returning the final score and all other relevant information
        return compatibility_score, compatibility_score_info


    def process_raw_data_literal( self, parser_name, strings, correct_patterns ):
        """ This function processes the raw data and turns it into useful information.
            That data provides useful statistics about the library's current "health".
            The function returns the overall score for the data, and specific statistics of the data """

        regex = regex4dummies()

        # Printing the semantic patterns within this string
        test_patterns = regex.compare_strings( parser_name, True, strings )

        # Compare test_patterns to correct patterns ( patterns in the "golden standard" )
        score = 0.00
        score_info = ""
        for compare_index in xrange( 0, len( test_patterns ) - 2, 3 ):
            for correct_pattern in correct_patterns:
                if test_patterns[ compare_index + 2 ] == correct_pattern[ 2 ]:
                    score += 100.00 / len( correct_patterns )

                    break

        score_info += "Test pattern: " + str( test_patterns ) + "\n" + "Correct pattern: " + str( correct_patterns ) + "\n\n"

        # Returning the final score and all other relevant information
        return score, score_info


if __name__ == '__main__':
    Main()
