__author__ = 'Vale Tolpegin'

from compare import Compare
from test_dependencies import run_dependency_tests
from toolkit import Toolkit

"""

Class information:

- name: regex4dummies
- version: 1.4.5

"""

# Main class that handles all interaction between the user/programmer and the compare class which does all of the heavy lifting
class regex4dummies:
    # Setting global version variable which contains the version of this library
    __version__ = '1.4.5'


    def __init__( self, **kwargs ):
        """
        Constructor method.
        """

        # Instantiating compare object to be used
        self.compare_object = Compare()


    def compare_strings( self, **kwargs ):
        """
        Function that is integral in communicating between a compare object and the user
        This function returns a 3-tuple array containing reliability score, applicability score, and pattern
        """

        # Testing the system to make sure all dependencies are installed
        if kwargs.get("pattern_detection") == "literal":
            if kwargs.get("parser") == '':
                test_install = run_dependency_tests()
                test_install.test( 'pattern nltk nlpnet' )
            else:
                test_install = run_dependency_tests()
                test_install.test( kwargs.get("parser") )

        # Call compare_strings of compare object & return output
        if kwargs.get("pattern_detection") == "literal":
            return self.compare_object.compare_strings( text=kwargs.get("text"), pattern_detection=True, parser=kwargs.get("parser") )
        else:
            return self.compare_object.compare_strings( text=kwargs.get("text"), pattern_detection=False, parser=kwargs.get("parser") )


    def get_pattern_information( self ):
        """
        This function returns the information for each sentence/pattern that was identified.
        This is only useful if semantic parsing is implemented; otherwise, {} will be returned
        """

        return self.compare_object.get_pattern_information()


    def get_topics( self, **kwargs ):
        """ Returns the list of topics that the parsers identified """

        return self.compare_object.get_pattern_topics( kwargs.get("text") )


    def extract_important_information( self, **kwargs ):
        """
        Returns the important information within the given text.
        """

        return self.compare_object.extract_important_information( kwargs.get("text") )


# If a user mistakingly runs this library believing it is a program, inform the user that it is not a program
if __name__ == '__main__':
    # Displaying information to the user
    print ""
    print "This program is a library, and therefore is not meant to be run as a separate application"
    print "If you would like to use a GUI version of this library, please see the examples folder in the github repo."
    print "http://github.com/DarkmatterVale/regex4dummies"
    print ""

    # Quitting the program
    exit( 0 )
