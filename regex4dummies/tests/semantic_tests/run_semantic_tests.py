class RunSemanticTests:

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
        print "Semantic Parser Tests: "
        print "-----------------------"
        print ""

        # Printing the semantic patterns within this string
        print "Semantic Patterns ( single phrase ): " + str( regex.compare_strings( 'nltk', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake. Back at your desk, I poured and killed him a rattlesnake and some more rattlesnake. How does that sound." ] ) )

        # Printing the semantic patterns with a keyword within this string
        print "Semantic Patterns ( keyword ): " + str( regex.compare_strings( 'nltk', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it? It is currently four pm.", "what time is it here?", "what time is it", "This is the cat's hat", "That is the cat's hat", "keyword=cat" ] ) )

        # Printing the semantic patterns within this string
        print "Semantic Patterns: " + str( regex.compare_strings( 'nltk', False, [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it? It is currently four pm.", "what time is it here?", "what time is it", "This is the cat's hat", "That is the cat's hat" ] ) )

        # Displaying all of the "meaning" in these sentences
        sentence_information = regex.get_pattern_information()
        for sentence in sentence_information:
            print "[ Pattern ]            : " + sentence.pattern
            print "[ Subject ]            : " + sentence.subject
            print "[ Verb ]               : " + sentence.verb
            print "[ Object ]             : " + sentence.object[0]
            print "[ Prep Phrases ]       : " + str( sentence.prepositional_phrases )
            print "[ Reliability Score ]  : " + str( sentence.reliability_score )
            print "[ Applicability Score ]: " + str( sentence.applicability_score )
            print ""

        # Clearing screen
        print ""
