# Importing other required libraries
import os
from subprocess import *
import re
import sys

import tarfile

# Importing the main library
from regex4dummies import regex4dummies


"""

Test information:

    Tests:
    - nltk parser
    - literal parser
    - pattern parser
    - nlpnet parser

Version: 1.3.6

"""


# Creating test object
regex = regex4dummies()

# Testing version variable
print regex.__version__

# Testing the 'nltk' parser
print regex.compare_strings( 'nltk', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str( sentence.reliability_score )


# Testing the 'pattern' parser
print regex.compare_strings( 'pattern', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str( sentence.reliability_score )


# Installing required dependencies for the nlpnet parser
# Getting nltk data path
running = Popen( [ 'python -c "import nltk;print nltk.data.path"' ], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True )
stdin, stdout = running.communicate()

# Setting the path that the nlpnet dependency will be downloaded from
path = re.sub( r"\'", "", re.sub( r"\[", '', str( stdin.split( '\n' )[ 0 ].split( ',' )[ 0 ] ) ) )
path = path.split( r"/" )
path = '/'.join( path[ 0 : len( path ) - 1 ] ) + '/nlpnet_dependency/'

# Download the dependencies & extract
current_directory = os.getcwd()

os.mkdir( path )
os.chdir( path )

os.system( "wget http://nilc.icmc.usp.br/nlpnet/data/dependency-en.tgz" )
tar = tarfile.open( path + 'dependency-en.tgz', 'r:gz' )
tar.extractall( path )
os.remove( path + 'dependency-en.tgz' )

os.chdir( current_directory )

# Testing the 'nlpnet' parser
print regex.compare_strings( 'nlpnet', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str( sentence.reliability_score )


# Testing literal parsing
print regex.compare_strings( 'default', True, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ] )
sentence_information = regex.get_pattern_information()
for sentence in sentence_information:
    print "[ Pattern ]          : " + sentence.pattern
    print "[ Subject ]          : " + sentence.subject
    print "[ Verb ]             : " + sentence.verb
    print "[ Object ]           : " + sentence.object[0]
    print "[ Reliability Score ]: " + str( sentence.reliability_score )
