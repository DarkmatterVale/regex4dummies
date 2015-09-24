__author__  = 'Vale Tolpegin'

"""

TopicFinder identifies the possible topics of a string.

Class information:
- name: TopicFinder
- version: 1.4.3

"""

import nltk
from nltk import FreqDist
from textblob import TextBlob

class TopicFinder:

    def __init__( self, *args, **kwargs ):
        """ Blank constructor method """

        pass


    def identify_topics( self, strings ):
        """Topic identifier function.

        inputs:
        -- string: A string that contains the set of sentences that topics would like to be identified in

        outputs:
        -- list: A list containing the topics of a string
        """

        # Creating final string from the addition of each string
        string = ""
        for individual_string in strings:
            string += " " + individual_string

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
        #print "Frequency Distribution: " + str( topics_freqdist.most_common( len( topics ) + 1 ) )

        for topic_index in range( 0, len( topics ) ):
            for word in string.split( ' ' ):
                if topics[ topic_index ] == word.lower():
                    topics[ topic_index ] = word

        # Getting the frequency distribution
        topics_frequencies_list = topics_freqdist.most_common( len( topics ) + 1 )

        # Testing to see whether any topics are mentioned more than once
        multiple_topic_references = False
        for topic in topics_frequencies_list:
            if topic[ 1 ] > 1:
                multiple_topic_references = True

                break

        # If there is at least 1 topic that is reference more than once, then remove all of the single-referenced topics
        final_topics = []
        if multiple_topic_references:
            for topic_index in range( 0, len( topics_frequencies_list ) ):
                if topics_frequencies_list[ topic_index ][ 1 ] == 1:
                    break
                else:
                    final_topics.append( [ topics_frequencies_list[ topic_index ][ 0 ], topics_frequencies_list[ topic_index ][ 1 ] ] )
        else:
            for topic_index in range( 0, len( topics_frequencies_list ) ):
                final_topics.append( [ topics_frequencies_list[ topic_index ][ 0 ], topics_frequencies_list[ topic_index ][ 1 ] ] )

        # Returning final topics list
        return final_topics


    def gather_important_information( self, text ):
        """
        Returns the most important information within a text
        based on its topics.
        """

        # Creating TextBlob to extract sentences from text
        input_textblob = TextBlob( ' '.join( text ) )

        # Getting the topics of a text ( ranked most important to least important )
        topics = self.identify_topics( text )

        # Getting the sentences with the topics in them
        important_sentences = []
        for sentence in input_textblob.sentences:
            sentence_text = str( sentence )
            add_to_important_sentences = False
            topic_counter = 0

            for topic in topics:
                if topic[ 0 ] in sentence_text:
                    add_to_important_sentences = True
                    topic_counter += 1

            if add_to_important_sentences:
                important_sentences.append( [ sentence_text, topic_counter ] )

        # Ranking the sentences
        ranked_sentences = []
        for sentence, topic_counter in important_sentences:
            if ranked_sentences == []:
                ranked_sentences.append( [ sentence, topic_counter ] )
            else:
                ranked_sentences = self.update_ranks( ranked_sentences, [ sentence, topic_counter ], 0 )

        # Removing unnecessary information from the sentences
        clean_sentences = []
        for sentence in ranked_sentences:
            clean_sentences.append( sentence[ 0 ] )

        # Returning the final important information
        return clean_sentences


    def update_ranks( self, ranked_sentences, sentence_info, add_index ):
        """
        Updates the ranks of the variable ranked_sentences
        """

        # Gathering information
        sentence = sentence_info[ 0 ]
        topic_counter = sentence_info[ 1 ]

        if add_index >= len( ranked_sentences ):
            ranked_sentences.insert( len( ranked_sentences ), [ sentence, topic_counter ] )
        else:
            # Updating information
            if ranked_sentences[ add_index ][ 1 ] > int( topic_counter ):
                ranked_sentences = self.update_ranks( ranked_sentences, [ sentence, topic_counter ], add_index + 1 )
            else:
                ranked_sentences.insert( add_index, [ sentence, topic_counter ] )

        # Returning updated ranked sentences
        return ranked_sentences


if __name__ == '__main__':
    exit( 0 )

    string_to_test_topics = [ """Test string goes here.""" ]

    topic_tester = TopicFinder()

    for item in topic_tester.gather_important_information( string_to_test_topics ):
        print item
        print ""
