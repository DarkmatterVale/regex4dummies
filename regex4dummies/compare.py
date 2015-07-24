__author__ = 'Vale Tolpegin'

# System related libraries
import os
import sys
import re

# Parsing related libraries
import re
from pattern_detail import pattern_detail
from literal_parsing import literal_parsing
from semantic_parsing import semantic_parsing
import nltk
from operator import itemgetter

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

Class information:

- name: compare
- version: 1.3.5

"""

class compare:
    global sentence_information
    global strings_parsed

    # Empty constructor
    def __init__( self, *args, **kwargs ):
        pass

    # This method is called by the main regex4dummies class, and calls all further methods to find strings
    def compare_strings( self, strings, literal, parser_name ):
        # Getting global variables
        global sentence_information
        global strings_parsed

        # Update global variables
        strings_parsed = strings

        # Reset variables
        patterns = []
        sentence_information = {}

        # Find the keyword
        keyword = ""
        for string in strings:
            if 'keyword=' in string:
                keyword = re.sub( 'keyword=', '', string )

        # Call find_patterns( strings )
        patterns = self.find_patterns( strings, 0, literal, [], parser_name )

        # After patterns are identified in strings, complete final processing
        #   1. Find reliability score
        #   2. Find applicability score
        #   3. If there is a keyword
        #       a. pare down pattern list to only those that have the keyword in them

        compiled_patterns = []
        for pattern in patterns:
            if keyword != '':
                if keyword in pattern:
                    compiled_patterns += [ self.get_reliability_score( pattern ), self.get_applicability_score( pattern ), pattern ]
            else:
                compiled_patterns += [ self.get_reliability_score( pattern ), self.get_applicability_score( pattern ), pattern ]

        return compiled_patterns

    # Recursive function that compares all strings and determins reliability score, applicability score, and pattern
    def find_patterns( self, strings, current_index, literal_find, patterns_arg, parser_name ):
        patterns = patterns_arg

        if not literal_find:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, False, patterns_arg, parser_name )

            for index in xrange( current_index, -1, -1 ):
                if strings[ index ] != strings[ current_index ]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.find_semantic_patterns( strings[ current_index ], strings[ index ], patterns, parser_name )
        else:
            if current_index < len( strings ) - 1:
                patterns = self.find_patterns( strings, current_index + 1, True, patterns_arg, parser_name )

            # for index in range( current_index, len( strings ) - 1 ):
            for index in xrange( current_index, -1, -1 ):
                if strings[ index ] != strings[ current_index ]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.find_literal_patterns( strings[ current_index ], strings[ index ], patterns, parser_name )

        # return patterns
        return patterns

    # This function identifies patterns in 2 strings
    def find_semantic_patterns( self, base_string, test_string, pattern_arg, parser_name ):
        # Getting global variables
        global sentence_information

        # Instantiating a new semantic_parsing class object
        semantic_pattern_parser = semantic_parsing()

        # Parsing information
        if parser_name == '':
            patterns, pattern_information = semantic_pattern_parser.parse( base_string, test_string, pattern_arg, parser_name )

            # Appending the pattern information to the global sentence_information variable
            sentence_information.update( pattern_information )

            return patterns
        else:
            patterns, pattern_information = semantic_pattern_parser.parse( base_string, test_string, pattern_arg, parser_name )

            # Appending the pattern information to the global sentence_information variable
            sentence_information.update( pattern_information )

            # return patterns
            return patterns

    def find_literal_patterns( self, base_string, test_string, pattern_arg, parser_name ):
        # Getting global variables
        global sentence_information

        # Instantiating a new literal_parsing class object
        literal_pattern_parser = literal_parsing()

        # Parsing information
        patterns, pattern_information = literal_pattern_parser.parse( base_string, test_string, pattern_arg, parser_name )

        # Appending the pattern information to the global sentence_information variable
        sentence_information.update( pattern_information )

        # Returning the patterns found
        return patterns

    # All patterns with associated information will be returned from this method as a list of pattern_detail classes
    def get_sentence_information( self ):
        # Getting global variables
        global sentence_information
        global strings_parsed

        # Creating a variable to hold the assembled pattern information. All of the pattern data will be converted into a pattern_detail object
        final_pattern_information = []

        # Getting patterns and printing them
        for sentence in sentence_information:
            pattern_info = pattern_detail()

            pattern_info.pattern               = sentence
            pattern_info.subject               = sentence_information[ sentence ][ 0 ]
            pattern_info.verb                  = sentence_information[ sentence ][ 1 ]
            pattern_info.object                = [ sentence_information[ sentence ][ 2 ] ]
            pattern_info.prepositional_phrases = sentence_information[ sentence ][ 3 ]
            pattern_info.reliability_score     = sentence_information[ sentence ][ 4 ] * 100 / len( strings_parsed )
            pattern_info.applicability_score   = sentence_information[ sentence ][ 5 ]

            final_pattern_information.append( pattern_info )

        # Returning the assembled information
        return final_pattern_information


    def get_pattern_topics( self ):
        """ This function will find all of the topics from the strings most recently compared """

        global strings_parsed

        """
        This is a backup simple topic determiner. It is only meant to be used in the event of something breaking with NLTK's NE chunker.

        topics = {}
        for string in strings_parsed:
            # Determine part of speech of each word
            words = nltk.pos_tag( nltk.word_tokenize( string ) )

            for word in words:
                if word[1] != "DT" and word[1] != "CC" and "PRP" not in word[1] and "VB" not in word[1] and word[1] != "IN" and word[1] != "." and word[1] != "," and word[1] != "POS" and word[1] != "WP" and "RB" not in word[1]:
                    if word[0] in topics:
                        topics[ word[0] ][1] += 1
                    else:
                        topics[ word[0] ] = [ word[0], 1 ]

        # Sort topics list
        organized_topics = []

        # Creating a list out of the compiled information
        for token in topics:
            organized_topics.append( [token, topics[ token ][1]] )

        # Removing topics that are only mentioned once. If the word in question is a topic, it will be used more than once
        topic_index = 0
        while topic_index < len( organized_topics ):
            if organized_topics[topic_index][1] == 1:
                del organized_topics[topic_index]

                topic_index = 0

            topic_index += 1

        # Sorting the final list
        organized_topics = sorted( organized_topics, key=itemgetter(1) )
        organized_topics = list(reversed( organized_topics ))

        # Removing numbers
        for topic_index in range(0, len(organized_topics)):
            organized_topics[topic_index] = organized_topics[topic_index][0]
        """

        topics = []
        for string in strings_parsed:
            named_entities = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize( string )), binary=True)
            named_entities =  nltk.chunk.tree2conlltags(named_entities)

            for entity in named_entities:
                if "NE" in entity[2]:
                    if entity not in topics:
                        topics.append( entity[0] )

        # Return organized_topics
        # A list is returned, with the most important topics on the left. For example,
        # [ "Most important/common pattern", "Second most important/common pattern", etc. ]
        return topics


    # This function is used to return the reliability score of a pattern
    def get_reliability_score( self, pattern ):
        # Getting global variables
        global sentence_information
        global strings_parsed

        for compiled_pattern in sentence_information:
            if compiled_pattern == pattern:
                return sentence_information[ compiled_pattern ][ 4 ] * 100 / len( strings_parsed )

    def get_applicability_score( self, pattern ):
        # Getting global variables
        global sentence_information
        global strings_parsed

        for compiled_pattern in sentence_information:
            if compiled_pattern == pattern:
                return sentence_information[ compiled_pattern ][ 5 ]
