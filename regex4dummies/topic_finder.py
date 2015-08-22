__author__  = 'Vale Tolpegin'

"""

TopicFinder identifies the possible topics of a string.

Class information:
- name: TopicFinder
- version: 1.4.0

"""

import nltk
from nltk import FreqDist

class TopicFinder:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def identify_topics( self, string ):
        """Topic identifier function.

        inputs:
        -- string: A string that contains the set of sentences that topics would like to be identified in

        outputs:
        -- list: A list containing the topics of a string
        """

        topics = []
        named_entities = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize( string )), binary=True)
        named_entities = nltk.chunk.tree2conlltags(named_entities)

        # Getting named entities in a text
        for entity in named_entities:
            if "NE" in entity[2]:
                if entity not in topics:
                    topics.append( entity[0] )

        # Getting other nounds in a text. These could be topics as well as named entities
        lowered_string = string.lower()
        for tag in nltk.pos_tag(nltk.word_tokenize( lowered_string )):
            if "NN" in tag[ 1 ]:
                add_to_topics = True

                for topic in topics:
                    if topic.lower() == tag[ 0 ]:
                        add_to_topics = False

                if add_to_topics:
                    topics.append( tag[ 0 ] )

        topics_freqdist = FreqDist( topics )
        #
        #print "Unshortened           : " + str( topics )
        #print ""
        #print "Shortened             : " + str( list( set( topics ) ) )
        #print ""
        print "Frequency Distribution: " + str( topics_freqdist.most_common( len( topics ) + 1 ) )

        for topic_index in range( 0, len( topics ) ):
            for word in string.split( ' ' ):
                if topics[ topic_index ] == word.lower():
                    topics[ topic_index ] = word

        return topics


if __name__ == '__main__':
    pass
