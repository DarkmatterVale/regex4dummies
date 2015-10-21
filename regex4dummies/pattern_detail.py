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
- version: 1.4.4

"""


class pattern_detail:

    def __init__( self, **kwargs ):
        """
        Constructor.
        """

        # Setting up variables
        self.pattern               = ""
        self.subject               = ""
        self.verb                  = ""
        self.object                = []
        self.prepositional_phrases = []
        self.reliability_score     = 0
        self.applicability_score   = 0
