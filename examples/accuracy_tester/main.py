__author__ = 'Vale Tolpegin'

"""

Class information:

- name: main
- version: 1.3.4

"""

class main:
    # Constructor
    def __init__( self, *args, **kwargs ):
        print ""
        print "This is currently under development....Please check back soon for a working version."
        print ""

        return

        # Beginning of main program

        # Currently implemented functions that will be tested
        # This program performs a number of accuracy tests against the library. THey are:
        # 1. Each individual parser is tested
        #   a. Are the subject, verb, object, and prepositional phrases properly identified?
        #   b. Are the applicability score and the reliability score properly calculated?
        #   c. Are all of the patterns identified?
        # 2. All 3 parsers in one function call
        #   a. Are all of the patterns identified?
        #   b. Are the subject, verb, object, and prepositional phrases properly identified?
        #   c. Are the applicability score and the reliability score properly calculated?

        # Functions to be implemented that will be tested
        # 1. FreqDist to determine the possible topics that all to the strings relate to
        # 2. Topics for each pattern is correctly identified

        print ""
        print "*" * 75
        print "regex4dummies Accuracy Tester"
        print ""
        print "Each test is valued in the following way: "
        print "* 100 - 90     : regex4dummies is consistently performing well and should be able to handle complex data"
        print "* 89 - 80      : regex4dummies is performing well, but does not perform that way consistently and cannot handle very complicated data"
        print "* 79 - 70      : regex4dummies is lacking in performance consistently and is not capable of parsing compex strings"
        print "* 69 and below : regex4dummies is doing very poorly and is considered still under development. It should not be used in applications which will be used by users"
        print "*" * 75
        print ""
        print "***Beginning Tests***"
        # COMPLETE TESTS HERE
        print "***Tests Completed***"
        print ""
        print "Overall Score : " # ADD SCORE ( Referenced from above ) HERE
        # SHOW TEST INFORMATION HERE
        print ""

if __name__ == '__main__':
    main()
