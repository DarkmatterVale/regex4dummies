import os
import sys
import re
from subprocess import *
import tarfile
import nltk
import nlpnet
from textblob import TextBlob
from compare import Compare

"""
This class will test to see whether the dependencies for the given parser
are installed. In the event that they are not already installed, the program
will ask the user whether to install them. If the user agrees, it will
download and install the dependencies.

Class information:

- name: run_dependency_tests
- version: 1.4.6
- author: Vale Tolpegin
"""


class RunDependencyTests:
    def __init__(self, *args, **kwargs):
        """
        Test for dependencies.
        """

        self.test()

    def test(self):
        """
        Testing each dependency
        """

        # Testing for textblob corpora which is used in most parsers
        self.test_for_textblob()

        # Testing for parser corpora for each parser
        self.test_for_nltk()
        self.test_for_nlpnet()

    def test_for_textblob(self):
        """
        Install textblob dependencies. It automatically
        checks to see if dependencies are already
        installed, so I do not need to do that.
        """

        # Installing data
        os.system("python -m textblob.download_corpora")

    def test_for_nltk(self):
        """
        Downloading all required NLTK dependencies.
        """

        from nltk.data import find
        from nltk import download

        # Download data if needed
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

    def test_for_nlpnet(self):
        """
        Attempting to use nlpnet. This will cause an
        error if the required dependencies are not
        downloaded.
        """

        try:
            # Creating a new compare object
            compare_nlpnet = Compare()

            # Comparing using the nltk parser
            compare_nlpnet.compare_strings(text=["what time is it here?", "This is the cat's hat"], pattern_detection=False, parser="nlpnet")

            # If that was successfuly, getting information
            sentence_information = compare_nlpnet.get_pattern_information()
            for sentence in sentence_information:
                my_pattern = "[ Pattern ]          : " + sentence.pattern
                my_subject = "[ Subject ]          : " + sentence.subject
                my_verb = "[ Verb ]             : " + sentence.verb
                my_object = "[ Object ]           : " + sentence.object[0]
                my_preps = "[ Prep Phrases ]     : " + str(sentence.prepositional_phrases)
                my_reliability_score = "[ Reliability Score ]: " + str(sentence.reliability_score)
        except:
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
