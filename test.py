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

# Downloading all required dependencies for TextBlob
os.system("python -m textblob.download_corpora")

# Downloading all required dependencies for NLTK
from nltk.data import find
from nltk import download

try:
    find('stopwords.zip')
except LookupError:
    download('stopwords')

try:
    find('maxent_ne_chunker')
except LookupError:
    download('maxent_ne_chunker')

try:
    find('words')
except LookupError:
    download('words')

# Creating test object
regex = regex4dummies()
tool_tester = Toolkit()

# Testing version variable
print regex.__version__

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


# Installing required dependencies for the nlpnet parser
# Getting nltk data path
running = Popen(['python -c "import nltk;print nltk.data.path"'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
stdin, stdout = running.communicate()

# Setting the path that the nlpnet dependency will be downloaded from
path = re.sub(r"\'", "", re.sub(r"\[", '', str(stdin.split('\n')[0].split(',')[0])))
path = path.split(r"/")
path = '/'.join(path[0 : len(path) - 1]) + '/nlpnet_dependency/'

# Download the dependencies & extract
current_directory = os.getcwd()

os.mkdir(path)
os.chdir(path)

os.system("wget http://nilc.icmc.usp.br/nlpnet/data/dependency-en.tgz")
tar = tarfile.open(path + 'dependency-en.tgz', 'r:gz')
tar.extractall(path)
os.remove(path + 'dependency-en.tgz')

os.chdir(current_directory)

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
