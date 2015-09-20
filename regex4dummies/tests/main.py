"""
This class runs tests for all of the functions of regex4dummies.
"""


from semantic_tests import RunSemanticTests
from topic_analysis import RunTopicAnalysisTests
from toolkit_tests import ToolkiTests
from literal_tests import LiteralParserTests


class main_tests:

    def __init__( self, *args, **kwargs ):
        """
        Constructor method.
        """

        # Displaying test information
        print ""
        print "This program will test regex4dummies' functions. This is not an accuracy tester (see the program located under examples)"
        print ""
        print "The following functions will be tested: "
        print "- Semantic parsing ( nltk )"
        print "- Literal parsing ( default )"
        print "- Topic analysis"
        print "- Toolkit functions ( all )"
        print ""
        print "--------------------------------------------"
        print ""


    def run_tests( self, regex4dummies_object, toolkit_object ):
        """
        Runs tests on regex4dummies' functions,
        including:
        - semantic parsers
        - topic analysis
        - Toolkit functions
        """

        # Instantiating test objects
        semantic_test_runner = RunSemanticTests()
        topic_analysis_test_runner = RunTopicAnalysisTests()
        toolkit_test_runner = ToolkiTests()
        literal_test_runner = LiteralParserTests()

        # Running tests
        semantic_test_runner.run_tests( regex4dummies_object )
        topic_analysis_test_runner.run_tests( regex4dummies_object )
        toolkit_test_runner.run_tests( toolkit_object )
        literal_test_runner.run_tests( regex4dummies_object )


if __name__ == '__main__':
    """
    Run the tests
    """

    RunTests()
