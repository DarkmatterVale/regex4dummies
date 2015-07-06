__author__ = "Vale Tolpegin"

from textblob import TextBlob

"""

Class information:

- name: literal_parsing
- version: 1.1.3

"""

class literal_parsing:
    def __init__( self, *args, **kwargs ):
        pass

    def parse( self, base_string, test_string, pattern_arg ):
        # Setting basic sentence information
        sentence_information = {}

        # Getting the current patterns already found
        patterns = pattern_arg

        # Literal translation from base_string -> test_string
        base_blob = TextBlob( base_string )
        base_sentence_info = []

        # Find patterns
        for sentence in base_blob.sentences:
            words = sentence.split( ' ' )

            for length in xrange( len( words ), 1, -1 ):
                for end in xrange( len( words ), 0, -1 ):
                    if end - length < 0:
                        break

                    pattern = words[ end - length: end ]

                    if ' '.join( pattern ) in str( test_string ):
                        if ' '.join( pattern ) not in patterns:
                            base_sentence_info += [ str( ' '.join( pattern ) ) ]

                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', 2 ]
                        else:
                            sentence_information[ str( ' '.join( pattern ) ) ][ 3 ] += 1

        patterns += base_sentence_info

        # Literal translation from base_string -> test_string
        test_blob = TextBlob( test_string )
        test_sentence_info = []

        # Find patterns
        for sentence in test_blob.sentences:
            words = sentence.split( ' ' )

            for length in xrange( len( words ), 1, -1 ):
                for end in xrange( len( words ), 0, -1 ):
                    if end - length < 0:
                        break

                    pattern = words[ end - length: end ]

                    if ' '.join( pattern ) in str( base_string ):
                        if ' '.join( pattern ) not in patterns:
                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', 2 ]

                            test_sentence_info += [ str( ' '.join( pattern ) ) ]
                        else:
                            sentence_information[ str( ' '.join( pattern ) ) ][ 3 ] += 1

        patterns += test_sentence_info

        return patterns, sentence_information

    def identify_syntactic_patterns( self, base_string, test_string, pattern_arg ):
        pass
