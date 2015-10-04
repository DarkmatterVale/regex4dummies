__author__  = 'Vale Tolpegin'

"""

PhraseExtractor extracts different kinds of phrases from a text

Class information:
- name: PhraseExtractor
- version: 1.4.4

"""


from textblob import TextBlob


class PhraseExtractor:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def extract_phrases( self, text ):
        """
        Returns the phrases found in a sentence,
        in the form of a dictionary.
        """

        # Getting the different kinds of phrases

        # Returing the dictionary/JSON-encoded response
        return {}


    def extract_noun_phrases( self, text ):
        """
        Returns the noun phrases found within
        a text.
        """

        # Instantiating variables
        noun_phrases = []

        # Creating a TextBlob object to get the noun phrases from the text
        phrase_chunker_blob = TextBlob( text )
        for phrase in phrase_chunker_blob.noun_phrases:
            noun_phrases.append( str( phrase ) )

        # Returning the found noun_phrases
        return noun_phrases


    def extract_verb_phrases( self, text ):
        """
        Returns the verb phrases found within
        a text.
        """

        # Instantiating variables
        verb_phrases = []

        # Returning the found verb_phrases
        return verb_phrases


    def extract_prepositional_phrases( self, text ):
        """
        Returns the prepositional phrases found
        within a text.
        """

        # Instantiating variables
        prepositional_phrases = []

        # Returning the found prepositional_phrases
        return prepositional_phrases
