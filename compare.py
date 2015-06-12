__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Parsing related libraries
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

    # Empty constructor
    def init( self, *args, **kwargs ):
        pass

    # This method is called by the main regex4dummies class, and calls all further methods to find strings
    def compare_strings( self, strings ):
        # Find the keyword
        keyword = ""
        for string in strings:
            if 'keyword=' in string:
                keyword = re.sub( 'keyword=', '', string )

        # Call find_patterns( strings )
        patterns = self.find_patterns( strings )

        # After patterns are identified in strings, complete final processing
        #   1. Find reliability score
        #   2. Find applicability score
        #   3. If there is a keyword
        #       a. pare down pattern list to only those that have the keyword in them

        compiled_patterns = {}
        for pattern in patterns:
            if keyword != '':
                if keyword in pattern:
                    compiled_patterns += [ self.find_reliability_score( pattern ), self.find_applicability_score( pattern ), pattern ]
            else:
                compiled_patterns += [ self.find_reliability_score( pattern ), self.find_applicability_score( pattern ), pattern ]

        return compiled_patterns

    # Recursive function that compares all strings and determins reliability score, applicability score, and pattern
    def find_patterns( self strings, current_index ):
        patterns = {}

        if current_index < len( strings ) - 1:
            patterns = self.find_patterns( strings, current_index + 1 )

        # for index in range( current_index, len( strings ) - 1 ):
        for index in range( current_index, len( strings ) - 1 ):
            # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
            patterns += self.identify_patterns( strings[ index ], strings[ index + 1 ] )

        # return patterns
        return patterns

    # This function identifies patterns in 2 strings
    def identify_patterns( base_string, test_string ):
        # patterns = {}
        patterns = {}

        # Compare substrings of base_string to test_string
        #   1. Split based on "." to find substrings
        #   2. Split based on " " to find individual words in a substring
        #   3. Compare words in substring to all substrings of test_string
        #       a. If over 75% of words in substring is in other string
        #           i. add substring to patterns object
        #   4. Repeat for remainder of substrings in file

        lines = base_string.split( '.' )
        for line in lines:
            words = line.split( ' ' )

            for sentence in test_string.split( '.' ):
                word_count = 0
                for word in words:
                    if word in sentence:
                        word_count += 1

                if word_count / len( words ) > 0.50:
                    patterns += line

                    break

        # Compare substrings of test_string to base_string
        #   1. Split based on "." to find substrings
        #   2. Split based on " " to find individual words in a substring
        #   3. Compare words in substring to all substrings of base_string
        #       a. If over 75% of words in substring is in other string
        #           i. add substring to patterns object
        #   4. Repeat for remainder of substrings

        lines = test_string.split( '.' )
        for line in lines:
            words = line.split( ' ' )

            for sentence in base_string.split( '.' ):
                word_count = 0
                for word in words:
                    if word in sentence:
                        word_count += 1

                if word_count / len( words ) > 0.50:
                    patterns += line

                    break

        # return patterns
        return patterns

    def find_reliability_score( self, pattern ):
        return 0

    def find_applicability_score( self, pattern ):
        return 0
