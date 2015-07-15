__author__ = 'Vale Tolpegin'

# Importing required libraries
from regex4dummies import regex4dummies

from pattern.en import parse
from textblob.parsers import PatternParser
from textblob import TextBlob
import nltk
import nlpnet
import os

"""

Class information:

- name: main
- version: 1.3.4

"""

class main:
    # Global variables
    global overall_score
    global pattern_score
    global pattern_score_info
    global nltk_score
    global nltk_score_info
    global nlpnet_score
    global nlpnet_score_info

    # Constructor
    def __init__( self, *args, **kwargs ):
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
        # 2. All 3 parsers in one function call
        #   a. Are all of the patterns identified?
        #   b. Are the subject, verb, object, and prepositional phrases properly identified?
        #   c. Are the applicability score and the reliability score properly calculated?

        # Functions to be implemented that will be tested
        # 3. FreqDist to determine the possible topics that all to the strings relate to
        # 4. Topics for each pattern is correctly identified

        # Weighting of each aspect of the final score
        # Test-Set #1: 40%
        # Test-Set #2: 40%
        # Test-Set #3: 10%
        # Test-Set #4: 10%
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


    # This function will perform the above tests, and set the appropriate variables with test information
    def complete_tests( self ):
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
        test_1 = """This is the first test string.

In this particular test string, a number of theories are discussed, with topics ranging from astrophysics to neural networking in computer science.
        """
        test_2 = """
        """
        test_3 = """
        """
        test_4 = """
        """

        # Creating correct information
        correct_patterns            = []
        correct_pattern_information = []

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


    # This function processes the raw data and turns it into useful information.
    # That data provides useful statistics about the library's current "health"
    # The function returns the overall score for the data, and specific statistics of the data
    def process_raw_data( self, raw_data, correct_patterns, correct_pattern_information ):
        pass


if __name__ == '__main__':
    main()
