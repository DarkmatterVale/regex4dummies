__author__ = 'Vale Tolpegin'

"""

Dependency is the interface method to get the sentence dependencies using different parsers ( i.e. subject, verb, object, etc )

Class information:
- name: Dependency
- version: 1.4.0

"""

from nltk_parser import NLTK
from pattern_parser import PATTERN
from nlpnet_parser import NLPNET

class Dependency:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def get_dependencies( self, string_to_find_dependencies, parser ):
        """ Interface method to regex4dummies returning the sentence dependencies gathered by given parser """

        if parser.lower() == "nltk":
            return self.return_nltk_dependencies( string_to_find_dependencies )
        elif parser.lower() == "pattern":
            return self.return_pattern_dependencies( string_to_find_dependencies )
        elif parser.lower() == "nlpnet":
            return self.return_pattern_dependencies( string_to_find_dependencies )
        else:
            print "A valid parser was not chosen to identify the sentence dependencies. Please choose one of the following:"
            print "- nltk"
            print "- pattern"
            print "- nlpnet"
            print ""

            exit( 0 )


    def return_nltk_dependencies( self, string_to_find_dependencies ):
        """ Interface method to get the sentence dependencies using nltk """

        pass


    def return_pattern_dependencies( self, string_to_find_dependencies ):
        """ Interface method to get the sentence dependencies using pattern """

        pass


    def return_nlpnet_dependencies( self, string_to_find_dependencies ):
        """ Interface method to get the sentence dependencies using nlpnet """

        pass
