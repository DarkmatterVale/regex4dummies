__author__ = 'Vale Tolpegin'

"""

The toolkit class manages all NLP related functions of regex4dummies. This allows regex4dummies to be separate from the toolkit, but in the same library.

Class information:
- name: toolkit
- version: 1.4.0

"""

from dependency import Dependency
from tokenizer import Tokenizer

class Toolkit:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def tokenize( self, string_to_tokenize, parser ):
        """ Returns the tokenized string using a parser """

        string_tokenizer = Tokenizer()

        return string_tokenizer.tokenize( string_to_tokenize, parser )


    def find_dependencies( self, string_to_get_dependencies, parser ):
        """ Returns the string with dependencies identified using the given parser """

        dependency_finder = Dependency()

        return dependency_finder.find_dependencies( string_to_get_dependencies, parser )
