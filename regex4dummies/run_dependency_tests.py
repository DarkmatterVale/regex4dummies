__author__ = 'Vale Tolpegin'

# Importing operating system related libraries
import os
import sys

# Importing other libraries needed for testing
import nltk
import nlpnet
from textblob import TextBlob

# Importing parsing related classes
from compare import compare
from gui_downloader import gui_downloader

# Importing GUI related classes
import Tkinter as tk
import ttk as ttk
import tkMessageBox

"""

This class will test to see whether the dependencies for the given parser are installed. In the event that they are not already installed, the program will ask the user whether to install them. If the user agrees, it will download and install the dependencies

Class information:

- name: run_dependency_tests
- version: 1.3.2

"""

class run_dependency_tests:
    # Blank constructor method
    def __init__( self, *args, **kwargs ):
        pass

    def test( self, parser_name ):
        # Testing for textblob corpora which is used in most parsers
        self.test_for_textblob()

        # Testing for parser corpora for each parser
        if parser_name.lower() == 'nltk':
            self.test_for_nltk()
        elif parser_name.lower() == 'nlpnet':
            self.test_for_nlpnet()

        return

    def test_for_textblob( self ):
        # Attempting to use textblob. This will cause an error if the textblob corpora is not downloaded
        try:
            # Creating a textblob object
            my_blob = TextBlob( "This is the first test sentence. This is the second test sentence. This it the third and final test sentence." )

            # Testing to see whether the textblob corpora has been downloaded
            for sentence in my_blob.sentences:
                str_sentence = str( sentence )
        except:
            # If it didn't work, this means the dependencies are missing from the system
            # The user will be asked whether he/she wants to install the dependencies. If so, they will be installed.
            # Otherwise, the program will quit and an error will appear saying the dependencies must be installed to use that parser

            textblob_downloader = gui_downloader()
            textblob_downloader.download( "Would you like to download the dependencies for TextBlob? All parsers will not be able to be used until the dependencies are downloaded", "TextBlob Corpora", "45.7 MB" )

    def test_for_nltk( self ):
        # Attempting to use nltk. This will cause an error if the corpora is not downloaded
        try:
            # Creating a new compare object
            compare_nltk = compare()

            # Comparing using the nltk parser
            compare_nltk.compare_strings( [ "what time is it here?", "This is the cat's hat" ], False, 'nltk'  )

            # If that was successfuly, getting information
            sentence_information = compare_nltk.get_pattern_information()
            for sentence in sentence_information:
                my_pattern           = "[ Pattern ]          : " + sentence.pattern
                my_subject           = "[ Subject ]          : " + sentence.subject
                my_verb              = "[ Verb ]             : " + sentence.verb
                my_object            = "[ Object ]           : " + sentence.object[0]
                my_preps             = "[ Prep Phrases ]     : " + str( sentence.prepositional_phrases )
                my_reliability_score = "[ Reliability Score ]: " + str( sentence.reliability_score )
        except:
            # If it didn't work, this means the dependencies are missing from the system
            # The user will be asked whether he/she wants to install the dependencies. If so, they will be installed.
            # Otherwise, the program will quit and an error will appear saying the dependencies must be installed to use that parser

            nltk_downloader = gui_downloader()
            nltk_downloader.download( "Would you like to download the dependencies for nltk?\n\nThe nltk parser will not be able to be used until the dependencies are downloaded", "NLTK Corpora", "1 GB" )

    def test_for_nlpnet( self ):
        # Attempting to use nlpnet. This will cause an error if the required dependencies are not downloaded
        try:
            # Creating a new compare object
            compare_nlpnet = compare()

            # Comparing using the nltk parser
            compare_nlpnet.compare_strings( [ "what time is it here?", "This is the cat's hat" ], False, 'nlpnet'  )

            # If that was successfuly, getting information
            sentence_information = compare_nlpnet.get_pattern_information()
            for sentence in sentence_information:
                my_pattern           = "[ Pattern ]          : " + sentence.pattern
                my_subject           = "[ Subject ]          : " + sentence.subject
                my_verb              = "[ Verb ]             : " + sentence.verb
                my_object            = "[ Object ]           : " + sentence.object[0]
                my_preps             = "[ Prep Phrases ]     : " + str( sentence.prepositional_phrases )
                my_reliability_score = "[ Reliability Score ]: " + str( sentence.reliability_score )
        except:
            # If it didn't work, this means the dependencies are missing from the system
            # The user will be asked whether he/she wants to install the dependencies. If so, they will be installed.
            # Otherwise, the program will quit and an error will appear saying the dependencies must be installed to use that parser

            nlpnet_downloader = gui_downloader()
            nlpnet_downloader.download( "Would you like to download the dependencies for nlpnet?\n\nThe nlpnet parser will not be able to be used until the dependencies are downloaded", "NLPnet English Library", "400 MB" )
