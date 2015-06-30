__author__ = 'Vale Tolpegin'

"""

The pattern_detail class is a container for all information related to a specific pattern. This information can include the:

- pattern
- subject ( if semantic pattern )
- verb ( if semantic pattern )
- object ( if semantic pattern )
- prepositional_phrases ( if semantic pattern )
- reliability score
- applicability score ( if semantic pattern )

All of these values can be referenced from an object of this class.

Class information:

- name: pattern_detail
- version: 1.1.3

"""

class pattern_detail:
    # Creating global values
    global pattern
    global subject
    global verb
    global object
    global prepositional_phrases
    global reliability_score
    global applicability_score

    def __init__( self, *args, **kwargs ):
        # Getting global variables
        global pattern
        global subject
        global verb
        global object
        global prepositional_phrases
        global reliability_score
        global applicability_score

        # Setting the global variables
        pattern               = ""
        subject               = ""
        verb                  = ""
        object                = []
        prepositional_phrases = []
        reliability_score     = 0
        applicability_score   = 0
