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
from semantic_parsers import NLTK
import nltk


class PhraseExtractor:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def extract_phrases( self, **kwargs ):
        """
        Returns the phrases found in a sentence,
        in the form of a dictionary.
        """

        # Getting the different kinds of phrases
        noun_phrases = self.extract_noun_phrases( kwargs.get("text") )
        verb_phrases = self.extract_verb_phrases( kwargs.get("text") )
        prepositional_phrases = self.extract_prepositional_phrases( kwargs.get("text") )

        # Returing the dictionary/JSON-encoded response
        return { "noun_phrases" : noun_phrases, "verb_phrases" : verb_phrases, "prepositional_phrases" : prepositional_phrases }


    def extract_noun_phrases( self, **kwargs ):
        """
        Returns the noun phrases found within
        a text.
        """

        # Instantiating variables
        noun_phrases = []

        # Creating a TextBlob object to get the noun phrases from the text
        phrase_chunker_blob = TextBlob( kwargs.get("text") )
        for phrase in phrase_chunker_blob.noun_phrases:
            noun_phrases.append( str( phrase ) )

        # Returning the found noun_phrases
        return noun_phrases


    def extract_verb_phrases( self, **kwargs ):
        """
        Returns the verb phrases found within
        a text.
        """

        # Instantiating variables
        verb_phrases = []
        verb_phrase_extractor = Dependency()

        if kwargs.get("parser").lower() != "nltk":
            # Getting verb phrases using the passed parser (Pattern or NLPNET)
            dependencies = verb_phrase_extractor.find_dependencies( text=kwargs.get("text"), parser=kwargs.get("parser") ).split( ' ' )

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
        else:
            # Getting verb phrases using the NLTK parser
            dependencies = verb_phrase_extractor.find_dependencies( text=kwargs.get("text"), parser=kwargs.get("parser") )

            # Adding the verbs to the verb_phrases
            verb_phrases.append( dependencies[1][1] )

        # Returning the found verb_phrases
        return verb_phrases


    def extract_prepositional_phrases( self, **kwargs ):
        """
        Returns the prepositional phrases found
        within a text.
        """

        # Instantiating variables
        prepositional_phrases = []
        prepositional_phrase_extractor = NLTK()

        # Getting prepositional phrases
        prepositional_phrases = prepositional_phrase_extractor.find_prepositional_phrases( kwargs.get("text"), kwargs.get("text"), nltk.pos_tag( nltk.word_tokenize( str( kwargs.get("text") ) ) ) ).split( '...' )
        prepositional_phrases = prepositional_phrases[ 0 : len( prepositional_phrases ) - 1 ]

        # Normalizing the phrases
        prepositional_phrases = self.normalize_text( prepositional_phrases )

        # Returning the found prepositional_phrases
        return prepositional_phrases


    def normalize_text( self, text ):
        """
        Returns the normalized version
        of the passed text variable.
        """

        # Instantiating variables
        normalized_text = text

        # Removing spaces at the start of each entry
        for phrase_index in range( 0, len( normalized_text ) ):
            if normalized_text[ phrase_index ] != '':
                if normalized_text[ phrase_index ][ 0 ] == " ":
                    normalized_text[ phrase_index ] = normalized_text[ phrase_index ][ 1 : ]

        # Returning normalized text
        return normalized_text
