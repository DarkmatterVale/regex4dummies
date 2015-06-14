__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Other
from compare import compare

# Main class that handles all interaction between the user/programmer and the compare class which does all of the heavy lifting
class regex4dummies:

    # Empty constructor method
    def init( self, *args, **kwargs ):
        pass

    # Function that is integral in communicating between a compare object and the user
    # This function returns a 3-tuple array containing reliability score, applicability score, and pattern
    def compare_strings( self, strings_to_process ):
        # Create a compare object
        string_compare = compare()

        # Call compare_strings of compare object
        # Return the output from compare_strings
        return string_compare.compare_strings( strings_to_process )

# If a user mistakingly runs this library believing it is a program, inform the user that it is not a program
if __name__ == '__main__':
    print ""
    print "This program is a library, and therefore is not meant to be run as a separate application"
    print "If you would like to use a GUI version of this library, please see the examples folder in the github repo."
    print "http://github.com/DarkmatterVale/regex4dummies"
    print ""

    regex = regex4dummies()

    print regex.compare_strings( [ "the cat is sitting, in the house, on the mat", "what time is it?", "This is the cat's hat" ] )
    exit( 0 )

    print regex.compare_strings( [ "This is the cat's hat", "the cat is sitting the mat and the hat", "the cat sat on the mat.", "the cat in the house sat on the mat" ] )
