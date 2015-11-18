__author__ = 'Vale Tolpegin'

"""

The toolkit class manages all NLP related functions of regex4dummies. This allows regex4dummies to be separate from the toolkit, but in the same library.

Class information:
- name: toolkit
- version: 1.4.4

"""

from dependency import Dependency
from tokenizer import Tokenizer
from phrase_extractor import PhraseExtractor
from string_compare import CompareStrings


class Toolkit:

    def __init__( self, *args, **kwargs ):
        """
        Constructor method.
        """

        self.extractor = PhraseExtractor()


    def extract_noun_phrases( self, **kwargs ):
        """
        Extracts the noun phrases out of a passed
        text.
        """

        # Getting noun phrases & returning them
        return self.extractor.extract_noun_phrases( text=kwargs.get("text"), parser=kwargs.get("parser") )


    def extract_verb_phrases( self, **kwargs ):
        """
        Extracts the verb phrases out of a passed
        text.
        """

        # Getting verb phrases & returning them
        return self.extractor.extract_verb_phrases( text=kwargs.get("text"), parser=kwargs.get("parser") )


    def extract_prepositional_phrases( self, **kwargs ):
        """
        Extracts the prepositional phrases out of a
        passed text.
        """

        # Getting the prepositional phrases & returning them
        return self.extractor.extract_prepositional_phrases( text=kwargs.get("text"), parser=kwargs.get("parser") )


    def tokenize( self, **kwargs ):
        """ Returns the tokenized string using a parser """

        string_tokenizer = Tokenizer()

        return string_tokenizer.tokenize( kwargs.get("text"), kwargs.get("parser") )


    def find_dependencies( self, **kwargs ):
        """ Returns the string with dependencies identified using the given parser """

        dependency_finder = Dependency()

        return dependency_finder.find_dependencies( text=kwargs.get("text"), parser=kwargs.get("parser"), response_type=kwargs.get("response_type") )


    def compare_strings( self, **kwargs ):
        """
        Returns the numerical value of the similarity between
        two input strings.
        """

        string_comparer = CompareStrings()

        return string_comparer.process( kwargs.get("String1"), kwargs.get("String2") )
