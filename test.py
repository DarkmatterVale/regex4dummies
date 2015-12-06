import os
from subprocess import *
import re
import sys
import tarfile
import nltk
from regex4dummies import regex4dummies
from regex4dummies import Toolkit


"""
Test information:

    Tests:
    - nltk parser
    - literal parser
    - pattern parser
    - nlpnet parser

Version: 1.4.4
"""

# Creating test object
regex = regex4dummies()
tool_tester = Toolkit()

# Testing version variable
print(regex.__version__)

# Testing the 'nltk' parser
print regex.compare_strings(parser='nltk', pattern_detection="semantic", text=["Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat"])
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str(sentence.reliability_score)

# Testing the 'pattern' parser
print regex.compare_strings(parser='pattern', pattern_detection="semantic", text=["Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat"])
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str(sentence.reliability_score)

# Testing the 'nlpnet' parser
print regex.compare_strings(parser='nlpnet', pattern_detection="semantic", text=["Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat"])
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str(sentence.reliability_score)

# Testing literal parsing
print regex.compare_strings(parser='default', pattern_detection="literal", text=["Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat"])
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str(sentence.reliability_score)

# Testing toolkit functions
# Testing NLTK functions
print "NLTK Toolkit tests:"
# tokenizer function
print tool_tester.tokenize(text="This is a test string.", parser="nltk")
# dependency function
print tool_tester.find_dependencies(text="This is a test string.", parser="nltk")
print ""

# Testing Pattern functions
print "Pattern Toolkit tests:"
# tokenizer function
print tool_tester.tokenize(text="This is a test string.", parser="pattern")
# dependency function
print tool_tester.find_dependencies(text="This is a test string.", parser="pattern")
print tool_tester.find_dependencies(text="This is a test string.", parser="pattern", response_type="simplified")
print ""

# Testing Nlpnet functions
print "Nlpnet Toolkit tests:"
# tokenizer function
print tool_tester.tokenize(text="This is a test string.", parser="nlpnet")
# dependency function
print tool_tester.find_dependencies(text="This is a test string.", parser="nlpnet")
print tool_tester.find_dependencies(text="This is a test string.", parser="nlpnet", response_type="simplified")
print ""

# Testing string compare functions
print "String Comparison tests:"
print tool_tester.compare_strings(String1="This is a test string.", String2="This is a test string.")
print ""

# Testing general functions
print "General Toolkit tests:"
# tokenizer function
print "Tokenized average: " + str(tool_tester.tokenize(text="This is a test string.", parser=""))
print "Noun Phrases: " + str(tool_tester.extract_noun_phrases(text="This is a test string."))
print "Verb Phrases(NLTK): " + str(tool_tester.extract_verb_phrases(text="This is a test string.", parser="nltk"))
print "Verb Phrases(Pattern): " + str(tool_tester.extract_verb_phrases(text="This is a test string.", parser="pattern"))
print "Verb Phrases(Nlpnet): " + str(tool_tester.extract_verb_phrases(text="This is a test string.", parser="nlpnet"))
print "Prepositional Phrases: " + str(tool_tester.extract_prepositional_phrases(text="This is a test string in the house."))
print ""

# Testing topic analysis
print "Topics: " + str(regex.get_topics(text=["This is my test string!!!!"]))
print ""

# Displaying the important information found within the text
print "Important information: " + str(regex.extract_important_information(text=["This is my test string!!!!"]))
print ""
