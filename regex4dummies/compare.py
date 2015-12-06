import re
from pattern_detail import pattern_detail
from literal_parsers import *
from semantic_parsing import semantic_parsing
from textblob import TextBlob
from topic_finder import TopicFinder

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

- name: Compare
- version: 1.4.4
- author: Vale Tolpegin
"""


class Compare:
    def __init__(self, *args, **kwargs):
        """
        Blank constructor.
        """

        pass

    def compare_strings(self, **kwargs):
        """
        This method is called by the main regex4dummies class, and calls all
        further methods find patterns within strings.
        """

        # Update self variables
        self.strings_parsed = kwargs.get("text")

        # Reset variables
        patterns = []
        self.sentence_information = {}

        # Find the keyword
        keyword = ""
        if len( kwargs.get("text") ) > 1:
            for string in kwargs.get("text"):
                if 'keyword=' in string:
                    keyword = re.sub('keyword=', '', string)

            # Call find_patterns( strings )
            patterns = self.find_patterns(kwargs.get("text"), 0, kwargs.get("pattern_detection"), [], kwargs.get("parser"))
        else:
            # Identifying patterns based on sentences
            strings = self.split_string(kwargs.get("text"))

            # Identifying patterns
            patterns = self.find_patterns(strings, 0, kwargs.get("pattern_detection"), [], kwargs.get("parser"))

        """
        After patterns are identified in strings, complete final processing
           1. Find reliability score
           2. Find applicability score
           3. If there is a keyword
               a. pare down pattern list to only those that have the keyword in them
        """

        compiled_patterns = []
        for pattern in patterns:
            if keyword != '':
                if keyword in pattern:
                    compiled_patterns += [[self.get_reliability_score(pattern), self.get_applicability_score(pattern), pattern]]
            else:
                compiled_patterns += [[self.get_reliability_score(pattern), self.get_applicability_score(pattern), pattern]]

        return compiled_patterns

    def find_patterns(self, strings, current_index, literal_find, patterns_arg, parser_name):
        """
        Recursive function that compares all strings and determins
        reliability score, applicability score, and pattern.
        """

        # Setting up variables
        patterns = patterns_arg

        if not literal_find:
            if current_index < len(strings) - 1:
                patterns = self.find_patterns(strings, current_index + 1, False, patterns_arg, parser_name)

            for index in xrange(current_index, -1, -1):
                if strings[index] != strings[current_index]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.find_semantic_patterns(strings[current_index], strings[index], patterns, parser_name)
        else:
            if current_index < len(strings) - 1:
                patterns = self.find_patterns(strings, current_index + 1, True, patterns_arg, parser_name)

            # for index in range( current_index, len( strings ) - 1 ):
            for index in xrange(current_index, -1, -1):
                if strings[index] != strings[current_index]:
                    # patterns += identify_patterns( strings[ index ], strings[ index + 1 ] )
                    patterns = self.find_literal_patterns(strings[current_index], strings[index], patterns, parser_name)

        # return patterns
        return patterns

    def find_semantic_patterns(self, base_string, test_string, pattern_arg, parser_name):
        """
        This function identifies semantic patterns in 2 strings.
        """

        # Instantiating a new semantic_parsing class object
        semantic_pattern_parser = semantic_parsing()

        # Parsing information
        if parser_name == '':
            patterns, pattern_information = semantic_pattern_parser.parse(base_string, test_string, pattern_arg, parser_name)

            # Appending the pattern information to the global sentence_information variable
            self.sentence_information.update(pattern_information)

            return patterns
        else:
            patterns, pattern_information = semantic_pattern_parser.parse(base_string, test_string, pattern_arg, parser_name)

            # Appending the pattern information to the global sentence_information variable
            self.sentence_information.update(pattern_information)

            # return patterns
            return patterns

    def find_literal_patterns(self, base_string, test_string, pattern_arg, parser_name):
        """
        Identifies literal patterns in 2 strings.
        """

        # Instantiating a new literal_parsing class object
        literal_pattern_parser = literal_parsing()

        # Parsing information
        patterns, pattern_information = literal_pattern_parser.parse(base_string, test_string, pattern_arg, parser_name)

        # Appending the pattern information to the global sentence_information variable
        self.sentence_information.update(pattern_information)

        # Returning the patterns found
        return patterns

    def get_pattern_information( self ):
        """
        All patterns with associated information will be returned from this
        method as a list of pattern_detail classes.
        """

        # Creating a variable to hold the assembled pattern information. All of the pattern data will be converted into a pattern_detail object
        final_pattern_information = []

        # Getting patterns and printing them
        for sentence in self.sentence_information:
            pattern_info = pattern_detail()

            pattern_info.pattern = sentence
            pattern_info.subject = self.sentence_information[sentence][0]
            pattern_info.verb = self.sentence_information[sentence][1]
            pattern_info.object = [ self.sentence_information[sentence][2]]
            pattern_info.prepositional_phrases = self.sentence_information[sentence][3]
            pattern_info.reliability_score = self.sentence_information[sentence][4] * 100 / len(self.strings_parsed)
            pattern_info.applicability_score = self.sentence_information[sentence][5]

            final_pattern_information.append(pattern_info)

        # Returning the assembled information
        return final_pattern_information

    def get_pattern_topics(self, strings_to_categorize):
        """
        This function will find all of the topics from the strings most
        recently compared.
        """

        string_topic_finder = TopicFinder()

        topics = string_topic_finder.identify_topics(strings_to_categorize)

        return topics

    def extract_important_information(self, string_to_summarize):
        """
        Returns the important information within the text given.
        """

        # Creating all variables needed
        topic_object = TopicFinder()

        # Getting the important information
        important_information = topic_object.gather_important_information(string_to_summarize)

        # Returning the important information
        return important_information

    def get_reliability_score(self, pattern):
        """
        Used to return the reliability score of a pattern.
        """

        for compiled_pattern in self.sentence_information:
            if compiled_pattern == pattern:
                score = self.sentence_information[compiled_pattern][4] * 100 / len(self.strings_parsed)

                if score > 100:
                    return 100
                else:
                    return score

    def get_applicability_score(self, pattern):
        """
        Used to get the applicability score of a pattern.
        """

        for compiled_pattern in self.sentence_information:
            if compiled_pattern == pattern:
                return self.sentence_information[compiled_pattern][5]

    def split_string(self, strings):
        """
        Returns the first string in strings, splitup by sentences.
        """

        # Setting up a variables
        string_to_split = strings[0]
        updated_strings = []

        # Creating a textblob from the string_to_split
        string_textblob = TextBlob(string_to_split)

        # Going through the sentences & splitting
        for sentence in string_textblob.sentences:
            updated_strings.append(str(sentence))

        # Returning sentences
        return updated_strings
