__author__ = 'Vale Tolpegin'

import os
from pattern.en import parse
from textblob import TextBlob
from regex4dummies import regex4dummies
from regex4dummies import Toolkit

"""

Class information:

- name: main
- version: 1.4.6

This is an accuracy tester for regex4dummies. It will test all components of the library and determine how effective it is at accomplishing its goal

"""

class Main:
    def __init__(self, *args, **kwargs):
        """
        Constructor method that will complete the tests and display the results.
        """

        # Currently implemented functions that will be tested
        # This program performs a number of accuracy tests against the library. THey are:
        # 1. Each individual parser is tested
        #   a. Are the subject, verb, object, and prepositional phrases properly identified?
        #   b. Are the applicability score and the reliability score properly calculated?
        #   c. Are all of the patterns identified?
        #   d. Is everything pertaining to the literal parser properly identified?
        # 2. All 3 parsers in one function call
        #   a. Are all of the patterns identified?
        #   b. Are the subject, verb, object, and prepositional phrases properly identified?
        #   c. Are the applicability score and the reliability score properly calculated?
        # 3. Topic identification
        #   a. Are all of the correct topics identified?
        #   b. Are there no extra topics found?

        # Weighting of each aspect of the final score ( from the above list )
        # #1: 50%
        # #2: 25%
        # #3: 25%
        # The test sets total up to 100%, giving a complete score. This score is meant to represent
        #   how important each aspect of the library is relative to the other aspects of the library.

        print("")
        print("*" * 75)
        print("regex4dummies Accuracy Tester")
        print("")
        print("Each test is valued in the following way ( 0 - 100 ): ")
        print("* 100 - 90     : regex4dummies is consistently performing well and should be able to handle complex data")
        print("* 89 - 80      : regex4dummies is performing well, but does not perform well consistently and probably cannot handle very complicated data")
        print("* 79 - 70      : regex4dummies' performance is consistently poor and regex4dummies is probably not capable of parsing compex strings")
        print("* 69 and below : regex4dummies is doing poorly and is considered still under development"
        print("")
        print("Please understand that these scores will not be a very accurate representation of regex4dummies' performance across the board. English is complicated and it is difficult to test every possible 'kind' of sentence.")
        print("*" * 75)
        print("")
        print("***Beginning Tests***")

        # Completing tests
        self.complete_tests()

        print("***Tests Completed***")
        print("")
        print("")
        print("***Score information***")
        print("Overall Score    : " + str(self.overall_score))
        print("")
        print("NLTK Score       : " + str(self.nltk_score))
        print("Pattern Score    : " + str(self.pattern_score))
        print("nlpnet Score     : " + str(self.nlpnet_score))
        print("Literal Score    : " + str(self.literal_score))
        print("Tri-parser Score : " + str(self.tri_parser_score))
        print("Topic Score      : " + str(self.topic_score))
        print("")

        # Showing other test-related information
        print("NLTK test details       ")
        print("------------------------")
        print(self.nltk_score_info)
        print("")

        print("Pattern test details    ")
        print("------------------------")
        print(self.pattern_score_info)
        print("")

        print("nlpnet test details     ")
        print("------------------------")
        print(self.nlpnet_score_info)
        print("")

        print("Literal test details    ")
        print("------------------------")
        print(self.literal_score_info)
        print("")

        print("Tri-parser test details ")
        print("------------------------")
        print(self.tri_parser_score_info)
        print("")

        print("Topic Score test details")
        print("------------------------")
        print(self.topic_score_info)
        print("")

        print("")

    def complete_tests(self):
        """
        This function will perform the above tests, and set the appropriate variables with test information.
        """

        # Setting all of the scores to restart
        self.overall_score = 0
        self.nltk_score = 0
        self.pattern_score = 0
        self.nlpnet_score = 0
        self.literal_score = 0
        self.tri_parser_score = 0
        self.topic_score = 0

        self.nltk_score_info = ""
        self.pattern_score_info = ""
        self.nlpnet_score_info = ""
        self.literal_score_info = ""
        self.tri_parser_score_info = ""
        self.topic_score_info = ""

        # Creating test-containing strings
        test_1 = "In The Catcher in the Rye and The Lord of the Flies, Ralphs conch and Holdens red hunting hat both have emotional attachments to many characters, and they are both used and applied differently in separate situations. Many different situations required the need of a leader in the Lord of the Flies, and the conch enabled Ralph to act as a leader by giving him authority over others, while Holden gets no power over others with the red hunting hat. Although the conch is a symbol of order and peace, in Catcher and the Rye the red hunting hat does not at all help keep peace or help Holden maintain order. In both books though, the conch and the red hunting hat are emotionally connected to the people that use them, helping people stay sane and happy."
        test_2 = "Throughout the Lord of the Flies, the conch is seen as a symbol of authority and power over others while the red hunting hat that Holden has does not have control over other people. Over the course of the whole book, Holden Caulfield struggles with depression and gets drunk numerous times in an attempt to make himself feel better. During one of his nights out, he shows his hat to a hat check girl in an attempt to get her to go out on a date with him. Although Holden attempts to get her to go on a date with him by using the red hunting hat, it doesnt work. This shows that the hunting hat has no authority and control over others. Immediately after Ralph and the kids crash on the island in the Lord of the Flies, Piggy and Ralph find a conch. The conch represents, in this example, a way to call others and gather as a community. When the others come, the conch becomes a sign of power and authority since it is the only way to communicate over long distances. In these examples, the red hunting hat has no control overs others, while the conch gives Ralph, or anyone else who has it, the power over others during a conversation or debate. Therefore, the two are used very differently and have very different purposes."
        test_3 = "Throughout the Catcher in the Rye, the red hunting hat does not help keep order, whereas the conch is used to assist the children in helping keep order during conversations, debates, and even fights. Although the red hunting hat represents an important emotional connection with Holden, it is not used at all to help keep order and peace within the Catcher in the Rye. Instead, the red hunting hat symbolizes growing up and independence, which is shown when he uses it whenever he is sad or upset. Once the boys get stuck on the island they know they must create rules to maintain order. To help keep order, Ralph uses the location of the conch as a meeting place. The creation of these rules, including the meeting rule, helps maintain order on the island and keep people safe. For a large portion of the book, the group of kids follows the rules and everything goes well for them. The purpose of the conch, therefore, is very different from the purpose of the hat. The hunting hat is an emotional symbol whereas the conch is a symbol of power and order by maintaining the peace on the island."
        test_4 = "In both the Catcher and the Rye and the Lord of the Flies, the red hunting hat and the conch both have emotional attachments to the people that use them. Near the end of the Catcher in the Rye, Holden is spending time with his little sister in a park when it begins to rain. To help keep her from getting wet, he gives it to her. He does this because she is growing up, although it makes him sad that he is losing his most prized possession. The conch eventually fails to keep the peace, however, and two separate groups emerge one vicious and violent led by Jack, and another calm and controlled led by Ralph. At the end of the book Ralph attempts to gain control over Jack and his violent followers, but he fails miserably with Piggy dying and the conch being destroyed, followed by a time where the silence was complete. This quote shows that the conch was something very important, and the destruction of it was unexpected and not intended. Although the conch and Holdens red hunting hat are very different, they both have strong emotional connections with the people that surround them, helping Holden stay sane by keeping him happy and showing him the bright side of things, and helping Ralph and the others stay positive about their chances of rescue."
        test_5 = "Both the conch in the Lord of the Flies and the red hunting hat in the Catcher in the Rye have emotional connections with other characters although they are very different in other purposes and usages of them. Possessions, like the conch and the red hunting hat, can be used in many different ways. Many possessions, regardless or their cost, can be emotionally attached the to the consumer. In addition, possessions can have many different uses. These could range from emotional attachments to being a toy for kids."

        # Creating correct information
        correct_patterns = []
        correct_pattern_information = {}
        correct_topics = ["Catcher", "Rye", "Lord", "Flies", "Ralph", "Holden"]
        correct_literal_patterns = [[100, 0, 'the red hunting hat'], [100, 0, 'the conch'], [100, 0, 'and the'], [100, 0, 'of the'], [50, 0, 'the Rye'], [100, 0, 'the Catcher'], [75, 0, 'the Catcher in the Rye,'], [75, 0, 'To help keep'], [75, 0, 'he is'], [50, 0, 'of the book'], [75, 0, 'Although the'], [50, 0, 'emotional connection'], [50, 0, 'growing up'], [50, 0, 'very different'], [50, 0, 'the peace'], [50, 0, 'Throughout the Catcher in the Rye, the red hunting'], [75, 0, 'the Lord of the Flies, the'], [50, 0, 'in a'], [75, 0, 'The conch'], [100, 0, 'control over'], [75, 0, 'attempts to'], [75, 0, 'shows that the'], [75, 0, 'Ralph and the'], [75, 0, 'the others'], [50, 0, 'and control'], [50, 0, 'Throughout the Lord of the Flies, the conch is seen'], [75, 0, 'to the people that use'], [75, 0, 'both have emotional attachments to'], [75, 0, 'Catcher and the Rye'], [100, 0, 'and the conch'], [75, 0, 'the Rye and'], [75, 0, 'In both'], [75, 0, 'conch and Holdens red hunting hat'], [75, 0, 'red hunting hat are'], [75, 0, 'the conch and'], [75, 0, 'Although the conch'], [75, 0, 'stay sane'], [75, 0, 'them, helping'], [75, 0, 'with the'], [50, 0, 'In The Catcher in'], [75, 0, 'does not'], [75, 0, 'it is'], [100, 0, 'on the island'], [100, 0, 'as a'], [75, 0, 'of power and'], [75, 0, 'a symbol of'], [50, 0, 'to a'], [75, 0, 'the red hunting hat does not'], [50, 0, 'order and peace'], [75, 0, 'at all'], [75, 0, 'maintain order.'], [75, 0, 'the conch is a symbol of'], [50, 0, 'and they'], [100, 0, 'power over others'], [75, 0, 'in the Lord of the Flies,'], [75, 0, 'others, while'], [50, 0, 'of a']]
        # ************************************************************
        # Beginning tests
        # ************************************************************

        # Structure of the correct information
        # The correct information is in this format:
        # [ [ patterns ] ]
        # 1. First array ( [ patterns ] ):
        #   a. pattern_detail object(s) containing patterns

        # Processing the raw data for the nltk parser
        print("Beginning nltk tests")
        self.nltk_score, self.nltk_score_info = self.process_raw_data_semantic( "nltk", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print("nltk tests completed")

        # Processing the raw data for the pattern parser
        print("Beginning pattern tests")
        self.pattern_score, self.pattern_score_info = self.process_raw_data_semantic( "pattern", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print("pattern tests completed")

        # Processing the raw data for the nlpnet parser
        print("Beginning nlpnet tests")
        self.nlpnet_score, self.nlpnet_score_info = self.process_raw_data_semantic( "nlpnet", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print("nlpnet tests completed")

        # Processing the raw data for the literal parser
        print("Beginning literal parser tests")
        self.literal_score, self.literal_score_info = self.process_raw_data_literal( "default", [test_1, test_2, test_3, test_4], correct_literal_patterns )
        print("literal parser tests completed")

        print("Beginning tri-parser tests")
        self.tri_parser_score, self.tri_parser_score_info = self.process_raw_data_semantic( "", [[test_1, test_2, test_3, test_4], correct_pattern_information], correct_topics )
        print("tri-parser tests completed")

        print("Beginning topic score tests")
        self.topic_score, self.topic_score_info = self.process_topics( [test_1, test_2, test_3, test_4], correct_topics )
        print("topic score tests completed")

        self.overall_score = ((self.nltk_score + self.pattern_score + self.nlpnet_score + self.literal_score) / 4) * 0.50
        self.overall_score += self.topic_score * 0.25
        self.overall_score += self.tri_parser_score * 0.25

    def process_raw_data_semantic(self, parser_name, information, correct_topics):
        """
        This function processes the raw data and turns it into useful information.
        That data provides useful statistics about the library's current "health".
        The function returns the overall score for the data, and specific statistics of the data.
        """

        regex = regex4dummies()

        # Getting the semantic patterns within the test strings
        regex.compare_strings(parser=parser_name, pattern_detection="semantic", text=information[ 0 ])

        # Gathering and comparing the "meaning" in these sentences
        test_information = {}
        sentence_information = regex.get_pattern_information()
        for sentence in sentence_information:
            # Getting information from the test sentence
            test_pattern = sentence.pattern
            test_subject = sentence.subject
            test_verb = sentence.verb
            test_object = sentence.object[0]
            test_prepositional_phrases = sentence.prepositional_phrases
            test_reliability_score = sentence.reliability_score
            test_applicability_score = sentence.applicability_score

            test_information[test_pattern] = [test_subject, test_verb, test_object, test_prepositional_phrases, test_reliability_score, test_applicability_score]

        compatibility_score = 0.00
        compare_index = 0
        for pattern in information[1]:
            base_pattern = pattern
            base_subject = information[1][base_pattern][0]
            base_verb = information[1][base_pattern][1]
            base_object = information[1][base_pattern][2]
            base_prepositional_phrases = information[1][base_pattern][3]
            base_reliability_score = information[1][base_pattern][4]
            base_applicability_score = information[1][base_pattern][5]

            try:
                test_pattern = base_pattern
                test_subject = test_information[ test_pattern ][ 0 ]
                test_verb = test_information[ test_pattern ][ 1 ]
                test_object = test_information[ test_pattern ][ 2 ]
                test_prepositional_phrases = test_information[ test_pattern ][ 3 ]
                test_reliability_score = test_information[ test_pattern ][ 4 ]
                test_applicability_score = test_information[ test_pattern ][ 5 ]

                if test_subject == base_subject:
                    compatibility_score += 100 / 6
                if test_verb == base_verb:
                    compatibility_score += 100 / 6
                if test_object == base_object:
                    compatibility_score += 100 / 6
                if test_prepositional_phrases == base_prepositional_phrases:
                    compatibility_score += 100 / 6
                if test_reliability_score == base_reliability_score:
                    compatibility_score += 100 / 6
                if test_applicability_score == base_applicability_score:
                    compatibility_score += 100 / 6
            except:
                compare_index += 1

                # The pattern was not in the gathered data. The score will not have anything additional added to it, and the loop will continue
                continue

            # Comparing and generating score
            compare_index += 1

        # Generating the semantic score
        if compare_index != 0:
            compatibility_score = compatibility_score / compare_index
        else:
            compatibility_score = 100

        compatibility_score_info = str(test_information) + "\n\n"
        compatibility_score_info += str(information[1])

        # Returning the final score and all other relevant information
        return compatibility_score, compatibility_score_info

    def process_raw_data_literal(self, parser_name, strings, correct_patterns):
        """
        This function processes the raw data and turns it into useful information.
        That data provides useful statistics about the library's current "health".
        The function returns the overall score for the data, and specific statistics of the data.
        """

        regex = regex4dummies()

        # Printing the semantic patterns within this string
        test_patterns = regex.compare_strings(parser=parser_name, pattern_detection="literal", text=strings)

        # Compare test_patterns to correct patterns ( patterns in the "golden standard" )
        score = 0.00
        score_info = ""
        for compare_index in range(0, len(test_patterns)):
            for correct_pattern in correct_patterns:
                if test_patterns[compare_index][2] == correct_pattern[2]:
                    score += 100.00 / len(correct_patterns)

                    break

        score_info += "Test pattern: " + str(test_patterns) + "\n\n" + "Correct pattern: " + str(correct_patterns) + "\n\n"

        # Returning the final score and all other relevant information
        return score, score_info

    def process_topics(self, strings, correct_topics):
        """
        process_topics finds the topics of the given strings and returns the topic score.
        """

        regex = regex4dummies()

        # Identifying topics discovered by the parsers in the most recently compared set of strings
        test_topics = regex.get_topics(text=strings)

        # Comparing topics & Generating topic score
        topic_score = 0
        for topic in correct_topics:
            for test_topic in test_topics:
                if topic == test_topic[0]:
                    topic_score += 100 / len(correct_topics)

                    break

        # Creating the information surrounding the test used to debug regex4dummies
        topic_score_info = "Topics Identified: " + str(test_topics) + "\n\n" + "Correct Topics: " + str(correct_topics)

        # Returning the final information
        return topic_score, topic_score_info

if __name__ == '__main__':
    Main()
