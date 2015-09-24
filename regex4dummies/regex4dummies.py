__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Other
from compare import compare
from run_dependency_tests import run_dependency_tests
from toolkit import Toolkit

"""

Class information:

- name: regex4dummies
- version: 1.4.3

"""

# Main class that handles all interaction between the user/programmer and the compare class which does all of the heavy lifting
class regex4dummies:
    # Global compare object. This is global because multiple methods need to be called from the same object
    global compare_object

    # Setting global version variable which contains the version of this library
    __version__ = '1.4.3'


    # Empty constructor method
    def __init__( self, *args, **kwargs ):
        # Getting global information
        global compare_object

        # Instantiating compare object to be used
        compare_object = compare()


    # Function that is integral in communicating between a compare object and the user
    # This function returns a 3-tuple array containing reliability score, applicability score, and pattern
    def compare_strings( self, parser_name, literal_find, strings_to_process ):
        # Testing the system to make sure all dependencies are installed
        if not literal_find:
            if parser_name == '':
                test_install = run_dependency_tests()
                test_install.test( 'pattern nltk nlpnet' )
            else:
                test_install = run_dependency_tests()
                test_install.test( parser_name )

        # Getting global variables
        global compare_object

        # Call compare_strings of compare object
        # Return the output from compare_strings
        return compare_object.compare_strings( strings_to_process, literal_find, parser_name )


    # This function returns the information for each sentence/pattern that was identified.
    # This is only useful if semantic parsing is implemented; otherwise, {} will be returned
    def get_pattern_information( self ):
        global compare_object

        return compare_object.get_pattern_information()


    def get_pattern_topics( self, strings_to_categorize ):
        """ Returns the list of topics that the parsers identified """

        global compare_object

        return compare_object.get_pattern_topics( strings_to_categorize )

    def extract_important_information( self, text_to_summarize ):
        """
        Returns the important information within the
        given text
        """

        global compare_object

        return compare_object.extract_important_information( text_to_summarize )


# If a user mistakingly runs this library believing it is a program, inform the user that it is not a program
if __name__ == '__main__':
    # Displaying information to the user
    print ""
    print "This program is a library, and therefore is not meant to be run as a separate application"
    print "If you would like to use a GUI version of this library, please see the examples folder in the github repo."
    print "http://github.com/DarkmatterVale/regex4dummies"
    print ""

    exit( 0 )
