__author__ = 'Vale Tolpegin'

"""

The toolkit class manages all NLP related functions of regex4dummies. This allows regex4dummies to be separate from the toolkit, but in the same library.

Class information:
- name: toolkit
- version: 1.4.0

"""

from dependency import Dependency
from tokenizer import Tokenizer
from phrase_extractor import PhraseExtractor

class Toolkit:

    def __init__( self, *args, **kwargs ):
        """
        Constructor method.
        """

        self.extractor = PhraseExtractor()


    def extract_noun_phrases( self, text ):
        """
        Extracts the noun phrases out of a passed
        text.
        """

        # Getting noun phrases & returning them
        return self.extractor.extract_noun_phrases( text )


    def extract_verb_phrases( self, text ):
        """
        Extracts the verb phrases out of a passed
        text.
        """

        # Getting verb phrases & returning them
        return self.extractor.extract_verb_phrases( text )


    def extract_prepositional_phrases( self, text ):
        """
        Extracts the prepositional phrases out of a
        passed text.
        """

        # Getting the prepositional phrases & returning them
        return self.extractor.extract_prepositional_phrases( text )


    def tokenize( self, string_to_tokenize, parser ):
        """ Returns the tokenized string using a parser """

        string_tokenizer = Tokenizer()

        return string_tokenizer.tokenize( string_to_tokenize, parser )


    def find_dependencies( self, string_to_get_dependencies, parser ):
        """ Returns the string with dependencies identified using the given parser """

        dependency_finder = Dependency()

        return dependency_finder.find_dependencies( string_to_get_dependencies, parser )
