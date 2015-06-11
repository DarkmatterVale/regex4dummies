__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

"""

    This class accomplishes the bulk of regex4dummies' work. Below is a short list of how this class works and what it does.

    1. Find patterns in a set of strings ( including or excluding a keyword search )
    2. Determine patterns' applicability and reliability
        a. Is the string's meaning different than another string? ( applicability )
        b. How many sources contain this pattern? ( reliability )
    3. Returns an array of patterns with the following values per array item
        a. Pattern: this is the string that was identified
        b. Reliability Score: 0 - 100 based off of how many times this pattern/string is seen on websites
        c. Applicability Score: 0 - 100 based off of how applicable/relevant this pattern/string is to the original query

"""

class compare:
    def init( self, *args, **kwargs ):
        pass

    def compare_strings( self, strings ):
        # Find the keyword

        # Call find_patterns( strings )

        # After patterns are identified in strings, complete final processing
        #   1. Find reliability score
        #   2. Find applicability score
        #   3. If there is a keyword
        #       a. pare down pattern list to only those that have the keyword in them

        pass

    def find_patterns( self strings, current_index ):
        if current_index < len( strings ) - 1:
            patterns = find_patters( strings, current_index + 1 )

        # for index in range( current_index, len( strings ) - 1 ):
            # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )

        # return patterns

    def identify_patterns( base_string, test_string ):
        pass
