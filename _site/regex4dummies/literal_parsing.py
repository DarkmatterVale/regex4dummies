__author__ = "Vale Tolpegin"

from textblob import TextBlob

"""

Class information:

- name: literal_parsing
- version: 1.3.2

"""

class literal_parsing:
    def __init__( self, *args, **kwargs ):
        pass

    def parse( self, base_string, test_string, pattern_arg, parser ):
        if parser == "default":
            return self.default_parser( base_string, test_string, pattern_arg );
        else:
            print ""
            print "A valid parser was not chosen. Please choose any of the following parsers: "
            print "- 'default'"
            print ""

            exit( 0 )

    def default_parser( self, base_string, test_string, pattern_arg ):
        # Setting basic sentence information
        sentence_information = {}

        # Getting the current patterns already found
        patterns = pattern_arg

        # Literal translation from base_string -> test_string
        base_blob = TextBlob( base_string )
        base_sentence_info = []

        # Find patterns for individual sentences
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

        # Find patterns for multiple sentences
        for outer_length in xrange( len( base_blob.sentences ), 2, -1 ):
            for outer_end in xrange( len( base_blob.sentences ), 0, -1 ):
                sentences = ' '.join( base_blob.sentences[ outer_end - outer_length : outer_end ] )
                words = sentences.split( ' ' )

                for length in xrange( len( words ), 1, -1 ):
                    for end in xrange( len( words ), 0, -1 ):
                        if end - length < 0:
                            break

                        pattern = words[ outer_end - outer_length : outer_end ]

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
