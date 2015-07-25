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

        # Displaying current message saying the example does not work yet
        print ""
        print "This is currently under development....Please check back soon for a working version."
        print ""

        #return

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

        # Functions to be implemented that will be tested
        # 3. Topics are correctly identified

        # Weighting of each aspect of the final score ( from the above list )
        # #1: 50%
        # #2: 25%
        # #3: 25%
        # The test sets total up to 100%, giving a complete score. This score is meant to represent
        #   how important each aspect of the library is relative to the other aspects of the library.

        print ""
        print "*" * 75
        print "regex4dummies Accuracy Tester"
        print ""
        print "Each test is valued in the following way ( 0 - 100 ): "
        print "* 100 - 90     : regex4dummies is consistently performing well and should be able to handle complex data"
        print "* 89 - 80      : regex4dummies is performing well, but does not perform that way consistently and cannot handle very complicated data"
        print "* 79 - 70      : regex4dummies is lacking in performance consistently and is not capable of parsing compex strings"
        print "* 69 and below : regex4dummies is doing very poorly and is considered still under development. It should not be used by anyone except developers"
        print "*" * 75
        print ""
        print "***Beginning Tests***"

        # Completing tests
        self.complete_tests()

        print "***Tests Completed***"
        print ""
        print ""
        print "***Score information***"
        print "Overall Score : " + str( overall_score )
        print ""
        print "NLTK Score    : " + str( nltk_score )
        print "Pattern Score : " + str( pattern_score )
        print "nlpnet Score  : " + str( nlpnet_score )
        print ""

        # Showing other test-related information
        print "NLTK test details    "
        print "---------------------"
        print nltk_score_info
        print ""

        print "Pattern test details "
        print "---------------------"
        print pattern_score_info
        print ""

        print "nlpnet test details  "
        print "---------------------"
        print nlpnet_score_info
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

        # Setting all of the scores to restart
        overall_score = 0
        nltk_score    = 0
        pattern_score = 0
        nlpnet_score  = 0

        nltk_score_info    = ""
        pattern_score_info = ""
        nlpnet_score_info  = ""

        # Creating test-containing strings
        # TODO: Increase "corpora" size & add much more data to test
        test_1 = "This is the first test string. Cats are very unique animals. In addition to being pets, they are wild animals. There are a number of different kinds of cats. Lions and cheetahs are included, there are three categories of cats."
        test_2 = "This is the second test string. Dogs, unlike cats, are not a unique kind of animal. Dogs are pets, wild animals, and some are even in between being wild and pets. Unlike cats, there are many different kinds of dogs. Wolves, for instance, are a kind of dog."
        test_3 = "This is the third test string. This string is about computers. Many people argue that artificially intelligent computers will take over the world. In fact, I disagree with this view. I believe that computers will not turn against us."
        test_4 = "This is the fourth test string. Like the last string, this string is about computers and is a continuation of the last conversation. Computers are very likely to instead help us. Although many scientists believe that I am incorrect, a number of other very smart scientists agree with me."

        """
        Tests to make sure the above strings work without any issues/bugs arising.
        """
        regex = regex4dummies()

        # Printing the semantic patterns within this string
        print "Patterns: " + str( regex.compare_strings( 'nltk', False, [ test_1, test_2, test_3, test_4 ] ) )

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
        correct_patterns            = []
        correct_pattern_information = {}
        correct_topics = [ "cats", "dogs", "computers" ]

        # ************************************************************
        # Beginning tests
        # ************************************************************

        # Structure of the correct information
        # The correct information is in this format:
        # [ [ patterns ] ]
        # 1. First array ( [ patterns ] ):
        #   a. pattern_detail object(s) containing patterns

        # Instantiating a regex4dummies object that will be used in the tests
        regex = regex4dummies()

        # Testing the NLTK parser
        #nltk_result = regex.compare_strings( 'nltk', False, [ test_1, test_2, test_3, test_4 ] )

        # Processing the raw data
        # nltk_score, nltk_score_info = self.process_raw_data( nltk_result, correct_patterns, correct_pattern_information )

        # Testing the Pattern parser
        #pattern_result = regex.compare_strings( 'pattern', False, [ test_1, test_2, test_3, test_4 ] )

        # Processing the raw data
        # pattern_score, pattern_score_info = self.process_raw_data( pattern_result, correct_patterns, correct_pattern_information )

        # Testing the nlpnet parser
        #nlpnet_result = regex.compare_strings( 'nlpnet', False, [ test_1, test_2, test_3, test_4 ] )

        # Processing the raw data
        # nlpnet_score, nlpnet_score_info = self.process_raw_data( nlpnet_result, correct_patterns, correct_pattern_information )


    def process_raw_data_semantic( self, parser_name, raw_data, information ):
        """ This function processes the raw data and turns it into useful information.
            That data provides useful statistics about the library's current "health".
            The function returns the overall score for the data, and specific statistics of the data """

        regex = regex4dummies()

        # Getting the semantic patterns within the test strings
        regex.compare_strings( parser_name, False, information[ 0 ] )

        # Identifying topics discovered by the parsers in the most recently compared set of strings
        test_topics = regex.get_pattern_topics()

        # Gathering and comparing the "meaning" in these sentences
        compare_index = 0
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

            # Getting information from the correct sentence

            # Comparing and generating score
            compare_index += 1

        # Generating the semantic score

        # Comparing topics & Generating topic score

        # Generating overall score

        # Returning the final score and all other relevant information


    def process_raw_data_literal( self, parser_name, raw_data, information ):
        """ This function processes the raw data and turns it into useful information.
            That data provides useful statistics about the library's current "health".
            The function returns the overall score for the data, and specific statistics of the data """

        regex = regex4dummies()

        # Printing the semantic patterns within this string
        test_patterns = regex.compare_strings( parser_name, True, information[ 0 ] )

        # Compare test_patterns to correct patterns ( patterns in the "golden standard" )

        # Generating overall score

        # Returning the final score and all other relevant information


if __name__ == '__main__':
    Main()
