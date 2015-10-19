__author__  = 'Vale Tolpegin'

"""

PhraseExtractor extracts different kinds of phrases from a text

Class information:
- name: PhraseExtractor
- version: 1.4.4

TODO:
- Implement multi parser phrase extraction (do not rely on a single parser to get the phrases extracted)

"""


import re

from textblob import TextBlob
from dependency import Dependency


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
        verb_phrase_extractor = Dependency()

        # Getting verb phrases using the Pattern parser
        dependencies = verb_phrase_extractor.find_dependencies( text, 'pattern' ).split( ' ' )

        for dependency_index in range( 0, len( dependencies ) ):
            # Check to see if the word is a verb or part of a verb phrase
            if "VP-" in dependencies[ dependency_index ]:
                # Check to see if the last word was part of a verb phrase
                if dependency_index != 0 and "VP-" in dependencies[ dependency_index - 1 ]:
                    # Since it was, append this verb onto the last verb phrase
                    verb_phrases[ len( verb_phrases ) ] += " " + re.sub( '/.*', '', dependencies[ dependency_index ] )

                    # Continue on to the next word in the sentence
                    continue

                # Remove the ending information, leaving the word
                cleaned_word = re.sub( '/.*', '', dependencies[ dependency_index ] )

                # Add the word to the verb phrase
                verb_phrases.append( cleaned_word )

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
