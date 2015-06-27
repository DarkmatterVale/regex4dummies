__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Other
from compare import compare

# Main class that handles all interaction between the user/programmer and the compare class which does all of the heavy lifting
class regex4dummies:
    # Global compare object. This is global because multiple methods need to be called from the same object
    global compare_object

    # Empty constructor method
    def __init__( self, *args, **kwargs ):
        # Getting global information
        global compare_object

        # Instantiating compare object to be used
        compare_object = compare()

    # Function that is integral in communicating between a compare object and the user
    # This function returns a 3-tuple array containing reliability score, applicability score, and pattern
    def compare_strings( self, parser_name, literal_find, strings_to_process ):
        # Getting global variables
        global compare_object

        # Call compare_strings of compare object
        # Return the output from compare_strings
        return compare_object.compare_strings( strings_to_process, literal_find, parser_name )

    # This function returns the information for each sentence/pattern that was identified.
    # This is only useful if semantic parsing is implemented; otherwise, {} will be returned
    def get_sentence_information( self ):
        global compare_object

        return compare_object.get_sentence_information()

# If a user mistakingly runs this library believing it is a program, inform the user that it is not a program
if __name__ == '__main__':
    # Displaying information to the user
    print ""
    print "This program is a library, and therefore is not meant to be run as a separate application"
    print "If you would like to use a GUI version of this library, please see the examples folder in the github repo."
    print "http://github.com/DarkmatterVale/regex4dummies"
    print ""

    exit( 0 )

    # Test Set
    regex = regex4dummies()

    # Printing the semantic patterns within this string
    print regex.compare_strings( 'nltk', False, [ "Back at my desk, I poured him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )

    # Displaying all of the "meaning" in these sentences
    sentence_information = regex.get_sentence_information()
    for sentence in sentence_information:
        print "[ Pattern ]          : " + sentence.pattern
        print "[ Subject ]          : " + sentence.subject
        print "[ Verb ]             : " + sentence.verb
        print "[ Object ]           : " + sentence.object[0]
        print "[ Reliability Score ]: " + str( sentence.reliability_score )
