__author__ = 'Vale Tolpegin'

"""

Dependency is the interface method to get the sentence dependencies using different parsers ( i.e. subject, verb, object, etc )

Class information:
- name: Dependency
- version: 1.4.4

"""

from semantic_parsers import *
import re


class Dependency:

    def __init__( self, *args, **kwargs ):
        """
        Blank constructor method.
        """

        pass


    def find_dependencies( self, **kwargs ):
        """
        Interface method to regex4dummies returning
        the sentence dependencies gathered by given parser.
        """

        if type(kwargs.get("response_type")) == str:
            if kwargs.get("response_type") == "simplified":
                if kwargs.get("parser").lower() == "nltk":
                    return self.return_nltk_dependencies( text=kwargs.get("text") )
                elif kwargs.get("parser").lower() == "pattern":
                    return self.simplify( text=self.return_pattern_dependencies( text=kwargs.get("text") ) )
                elif kwargs.get("parser").lower() == "nlpnet":
                    return self.simplify( text=self.return_pattern_dependencies( text=kwargs.get("text") ) )
            else:
                if kwargs.get("parser").lower() == "nltk":
                    return self.return_nltk_dependencies( text=kwargs.get("text") )
                elif kwargs.get("parser").lower() == "pattern":
                    return self.return_pattern_dependencies( text=kwargs.get("text") )
                elif kwargsf.get("parser").lower() == "nlpnet":
                    return self.return_pattern_dependencies( text=kwargs.get("text") )
        else:
            if kwargs.get("parser").lower() == "nltk":
                return self.return_nltk_dependencies( text=kwargs.get("text") )
            elif kwargs.get("parser").lower() == "pattern":
                return self.return_pattern_dependencies( text=kwargs.get("text") )
            elif kwargs.get("parser").lower() == "nlpnet":
                return self.return_pattern_dependencies( text=kwargs.get("text") )

        print "A valid parser was not chosen to identify the sentence dependencies. Please choose one of the following:"
        print "- nltk"
        print "- pattern"
        print "- nlpnet"
        print ""

        exit( 0 )


    def return_nltk_dependencies( self, **kwargs ):
        """
        Interface method to get the sentence dependencies using nltk.
        """

        nltk_dependency_finder = NLTK()

        return nltk_dependency_finder.find_dependencies( kwargs.get("text") )


    def return_pattern_dependencies( self, **kwargs ):
        """
        Interface method to get the sentence dependencies using pattern.
        """

        pattern_dependency_finder = PATTERN()

        return pattern_dependency_finder.find_dependencies( kwargs.get("text") )


    def return_nlpnet_dependencies( self, **kwargs ):
        """
        Interface method to get the sentence dependencies using nlpnet.
        """

        nlpnet_dependency_finder = NLPNET()

        return nlpnet_dependency_finder.find_dependencies( kwargs.get("text") )


    def simplify( self, **kwargs ):
        """
        Returns the simplified version of the input text.
        """

        # Instantiating variables
        processed_text = kwargs.get("text")
        svo_simplified = []
        subject = ""
        verb = ""
        object = ""

        # Getting the subject
        for word in processed_text.split( ' ' ):
            # If the word is the subject of the sentence, add it as the subject
            if "SBJ-" in word:
                subject += " " + re.sub( '/.*', '', word )
            elif "VP-" in word:
                verb += " " + re.sub( '/.*', '', word )
            elif "OBJ-" in word:
                object += " " + re.sub( '/.*', '', word )

        # Removing extra spaces
        subject = subject[ 1 : ]
        verb = verb[ 1 : ]
        object = object[ 1 : ]

        # Assembling information
        svo_simplified = [ [ "subject", subject ], [ "verb", verb ], [ "object", object ] ]

        # Returning information
        return svo_simplified
