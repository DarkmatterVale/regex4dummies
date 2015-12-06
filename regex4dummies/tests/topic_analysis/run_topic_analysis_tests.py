class RunTopicAnalysisTests:
    def __init__(self, *args, **kwargs):
        """
        Blank constructor method
        """

        pass

    def run_tests(self, regex):
        """
        Runs tests, then returns
        """

        # Clearing screen
        print("Topic Analysis Tests: ")
        print("----------------------\n")

        # I DID NOT WRITE THIS TEXT...IT HAS BEEN GATHERED FROM A NEWS ARTICLE, which can be found online. I DO NOT TAKE CREDIT FOR THIS!!!!!
        string_to_test_topics = """
        To answer this question, student people first need to find another world where life could grow. After looking at all the worlds going around our sun, as far as we can tell our home world is the only one that is good enough for life. So we have to look further away.

We have found hundreds and hundreds of worlds going around far-away stars. But most of these far-away worlds are much bigger than our home world, and much closer to their stars, those are the ones that are easier to spot.

But now, student-people have found a world that is not too different from our own. This sister world is only about one and a half times as big as our home world, and it goes around its star in about the same time it takes us to go around the sun.
        """

        # Displaying the topics that were identified by the parsers in the most recently compared set of strings
        print("Topics: " + str(regex.get_topics(text=[string_to_test_topics])) + "\n")

        # Displaying the important information found within the text
        print("Important information: " + str(regex.extract_important_information(text=[string_to_test_topics])) + "\n")
