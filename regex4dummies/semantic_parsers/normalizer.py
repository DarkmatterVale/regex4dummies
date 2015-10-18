__author__ = 'Vale Tolpegin'

"""

- name: Normalizer
- version: 1.4.3

Normalizes the incoming text and returns said normalized text

"""


from nltk.stem.porter import *
import nltk


class Normalizer:


    def __init__( self ):
        """ Blank constructor """

        pass


    def normalize_sentence_info( self, sentence_info ):
        """ Method to normalize text

        This is accomplished by:
        - Removing punctuation
        - Removing possession
        - Removing capitalization
        - Correcting spelling

        Input:
        - text: String containing the text to normalize
        """

        # Create a stemmer object
        stemmer = PorterStemmer()

        # Normalizing sthe patterns
        # Make the subject, verb, and object lowercase
        sentence_info[0] = sentence_info[0].lower()
        sentence_info[1] = sentence_info[1].lower()
        sentence_info[2] = sentence_info[2].lower()

        # Implement stemming
        sentence_info[0] = stemmer.stem( sentence_info[0] )
        sentence_info[1] = stemmer.stem( sentence_info[1] )
        sentence_info[2] = stemmer.stem( sentence_info[2] )

        # Return normalized information
        return sentence_info
