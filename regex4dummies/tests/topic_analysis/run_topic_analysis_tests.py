class RunTopicAnalysisTests:

    def __init__( self, *args, **kwargs ):
        """
        Blank constructor method
        """

        pass


    def run_tests( self, regex ):
        """
        Runs tests, then returns
        """

        # Clearing screen
        print "Topic Analysis Tests: "
        print "----------------------"
        print ""

        # Displaying the topics that were identified by the parsers in the most recently compared set of strings
        print "Topics: " + str( regex.get_pattern_topics( [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it? It is currently four pm.", "what time is it here?", "what time is it", "This is the cat's hat", "That is the cat's hat" ] ) )
        print ""

        # Clearing screen
        print ""
