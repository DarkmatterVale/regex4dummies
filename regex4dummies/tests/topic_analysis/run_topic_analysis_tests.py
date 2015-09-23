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

        # I DID NOT WRITE THIS TEXT...IT HAS BEEN GATHERED FROM A NEWS ARTICLE, which can be found online. I DO NOT TAKE CREDIT FOR THIS!!!!!
        string_to_test_topics = """
        To answer this question, student people first need to find another world where life could grow. After looking at all the worlds going around our sun, as far as we can tell our home world is the only one that is good enough for life. So we have to look further away.

We have found hundreds and hundreds of worlds going around far-away stars. But most of these far-away worlds are much bigger than our home world, and much closer to their stars, those are the ones that are easier to spot.

But now, student-people have found a world that is not too different from our own. This sister world is only about one and a half times as big as our home world, and it goes around its star in about the same time it takes us to go around the sun.
        """

        # Displaying the topics that were identified by the parsers in the most recently compared set of strings
        #print "Topics: " + str( regex.get_pattern_topics( [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it? It is currently four pm.", "what time is it here?", "what time is it", "This is the cat's hat", "That is the cat's hat" ] ) )
        print "Topics: " + str( regex.get_pattern_topics( [ string_to_test_topics ] ) )
        print ""

        # Displaying the important information found within the text
        print "Important information: " + str( regex.extract_important_information( [ string_to_test_topics ] ) )
        print ""

        # Clearing screen
        print ""
