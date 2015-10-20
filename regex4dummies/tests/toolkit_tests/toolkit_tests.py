"""
Class Version: 1.4.4
"""

class ToolkiTests:

    def __init__( self, **kwargs ):
        """
        Blank constructor method
        """

        pass


    def run_tests( self, tool_tester ):
        """
        Runs tests, then returns
        """

        # Clearing screen
        print "Toolkit Tests: "
        print "---------------"
        print ""

        # Testing NLTK functions
        print "NLTK Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( text="This is a test string.", parser="nltk" )
        # dependency function
        print tool_tester.find_dependencies( text="This is a test string.", parser="nltk" )
        print ""

        # Testing Pattern functions
        print "Pattern Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( text="This is a test string.", parser="pattern" )
        # dependency function
        print tool_tester.find_dependencies( text="This is a test string.", parser="pattern" )
        print ""

        # Testing Nlpnet functions
        print "Nlpnet Toolkit tests:"
        # tokenizer function
        print tool_tester.tokenize( text="This is a test string.", parser="nlpnet" )
        # dependency function
        print tool_tester.find_dependencies( text="This is a test string.", parser="nlpnet" )
        print ""

        # Testing general functions
        print "General Toolkit tests:"
        # tokenizer function
        print "Tokenized average: " + str( tool_tester.tokenize( text="This is a test string.", parser="" ) )
        print "Noun Phrases: " + str( tool_tester.extract_noun_phrases( text="This is a test string." ) )
        print "Verb Phrases: " + str( tool_tester.extract_verb_phrases( text="This is a test string." ) )
        print "Prepositional Phrases: " + str( tool_tester.extract_prepositional_phrases( text="This is a test string in the house." ) )
        print ""

        # Clearing screen
        print ""
