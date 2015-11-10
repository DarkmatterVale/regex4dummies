__author__  = 'Vale Tolpegin'

from fuzzywuzzy import fuzz

"""
CompareStrings compares two strings and returns the numerical value of their similarity.

Class information:
- name: CompareStrings
- version: 1.4.4
"""


class CompareStrings:

    def __init__( self, *args, **kwargs ):
        """
        Blank constructor method.
        """

        pass


    def process( self, base_string, test_string ):
        """
        This method is what is called by regex4dummies to compare
        two strings. It compares the string, then identifies
        their numerical similarity. Finally, it returns this
        value.
        """

        # Creating variables
        similarity_value = 0

        # Getting similarity
        similarity_value = fuzz.ratio( base_string, test_string )

        # Returning the similarity value
        return similarity_value
