__author__ = "Vale Tolpegin"

from textblob import TextBlob

"""

Class information:

- name: literal_parsing
- version: 1.4.2

"""

class literal_parsing:
    def __init__( self, *args, **kwargs ):
        """ Blank constructor """

        pass

    def parse( self, base_string, test_string, pattern_arg, parser ):
        """ Returns the parsed version of the incoming text """

        if parser == "default":
            return self.default_parser( base_string, test_string, pattern_arg )
        else:
            print ""
            print "A valid parser was not chosen. Please choose any of the following parsers: "
            print "- 'default'"
            print ""

            exit( 0 )

    def default_parser( self, base_string, test_string, pattern_arg ):
        """ Parsing code for the default literal parser """
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

                    if ' '.join( pattern ) in str( test_string ) and pattern != '' and pattern != []:
                        if ' '.join( pattern ) not in patterns and ' '.join( pattern ) not in base_sentence_info:
                            base_sentence_info += [ str( ' '.join( pattern ) ) ]

                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', [], 2, 0 ]
                        else:
                            try:
                                sentence_information[ str( ' '.join( pattern ) ) ][ 4 ] += 1
                            except:
                                pass

        # Find patterns for multiple sentences
        for outer_length in xrange( len( base_blob.sentences ), 2, -1 ):
            for outer_end in xrange( len( base_blob.sentences ), 0, -1 ):
                sentence_list = [ str( sentence ) for sentence in base_blob.sentences ]
                sentences = ' '.join( sentence_list )
                words = sentences.split( ' ' )

                for length in xrange( len( words ), 1, -1 ):
                    for end in xrange( len( words ), 0, -1 ):
                        if end - length < 0:
                            break

                        pattern = words[ outer_end - outer_length : outer_end ]

                        if ' '.join( pattern ) in str( test_string ) and pattern != '' and pattern != []:
                            if ' '.join( pattern ) not in patterns and ' '.join( pattern ) not in base_sentence_info:
                                base_sentence_info += [ str( ' '.join( pattern ) ) ]

                                sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', [], 2, 0 ]
                            else:
                                pass

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

                    if ' '.join( pattern ) in str( base_string ) and pattern != '' and pattern != []:
                        if ' '.join( pattern ) not in patterns and ' '.join( pattern ) not in base_sentence_info:
                            test_sentence_info += [ str( ' '.join( pattern ) ) ]

                            sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', [], 2, 0 ]
                        else:
                            try:
                                sentence_information[ str( ' '.join( pattern ) ) ][ 4 ] += 1
                            except:
                                pass

        # Find patterns for multiple sentences
        for outer_length in xrange( len( test_blob.sentences ), 2, -1 ):
            for outer_end in xrange( len( test_blob.sentences ), 0, -1 ):
                sentence_list = [ str( sentence ) for sentence in test_blob.sentences ]
                sentences = ' '.join( sentence_list )
                words = sentences.split( ' ' )

                for length in xrange( len( words ), 1, -1 ):
                    for end in xrange( len( words ), 0, -1 ):
                        if end - length < 0:
                            break

                        pattern = words[ outer_end - outer_length : outer_end ]

                        if ' '.join( pattern ) in str( test_string ) and pattern != '' and pattern != []:
                            if ' '.join( pattern ) not in patterns and ' '.join( pattern ) not in test_sentence_info:
                                test_sentence_info += [ str( ' '.join( pattern ) ) ]

                                sentence_information[ str( ' '.join( pattern ) ) ] = [ '', '', '', [], 2, 0 ]
                            else:
                                pass

        patterns += test_sentence_info

        return self.remove_sub_patterns( patterns, sentence_information, [ base_string, test_string ] )


    def remove_sub_patterns( self, patterns, pattern_information, strings ):
        """ Removes sub patterns, which are patterns within patterns.

        The sub patterns are not referenced in any context other than the context of the "parent" pattern, therefore making them sub patterns and
        not individual patterns that just happen to occur within other patterns.
        """

        # Creating new variables that will store the final information to
        final_patterns = []
        final_pattern_information = {}

        # Looking for sub patterns in each of the strings
        if patterns != []:
            if len( patterns ) != 1:
                for outer_pattern_index in range( 0, len( patterns ) - 1 ):
                    for inner_pattern_index in range( outer_pattern_index, len( patterns ) ):
                        outer_add_to_pattern = True
                        inner_add_to_pattern = True
                        for pattern in final_patterns:
                            if patterns[ outer_pattern_index ] in pattern:
                                outer_add_to_pattern = False

                            if patterns[ inner_pattern_index ] in pattern:
                                inner_add_to_pattern = False

                            if inner_add_to_pattern == False and outer_add_to_pattern == False:
                                break

                        if inner_add_to_pattern == True and outer_add_to_pattern == True:
                            if len( patterns[ outer_pattern_index ] ) > len( patterns[ inner_pattern_index ] ):
                                final_patterns.append( patterns[ outer_pattern_index ] )

                                try:
                                    final_pattern_information[ patterns[ outer_pattern_index ] ] = pattern_information[ patterns[ outer_pattern_index ] ]
                                except:
                                    pass
                            else:
                                final_patterns.append( patterns[ inner_pattern_index ] )

                                try:
                                    final_pattern_information[ patterns[ inner_pattern_index ] ] = pattern_information[ patterns[ inner_pattern_index ] ]
                                except:
                                    pass
                        elif inner_add_to_pattern == True and outer_add_to_pattern == False:
                            final_patterns.append( patterns[ inner_pattern_index ] )

                            try:
                                final_pattern_information[ patterns[ inner_pattern_index ] ] = pattern_information[ patterns[ inner_pattern_index ] ]
                            except:
                                pass
                        elif inner_add_to_pattern == False and outer_add_to_pattern == True:
                            final_patterns.append( patterns[ outer_pattern_index ] )

                            try:
                                final_pattern_information[ patterns[ outer_pattern_index ] ] = pattern_information[ patterns[ outer_pattern_index ] ]
                            except:
                                pass

        if final_patterns == []:
            final_patterns = patterns

        return final_patterns, final_pattern_information
