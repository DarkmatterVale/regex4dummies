__author__ = 'Vale Tolpegin'

import Tkinter as tk
import ttk as ttk
import tkMessageBox
import tkFileDialog
import ScrolledText
import threading
import time

from textblob import TextBlob

from regex4dummies import regex4dummies
from regex4dummies import Toolkit

"""

Class information:
- Name: main
- Version: 1.4.4

"""

class Main( tk.Tk ):
    def __init__( self, *args, **kwargs ):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title( 'regex4dummies' )

        self.initialize()

    def initialize( self ):
        self.grid()

        # Grid Design:
        # |---------------------------------------------|
        # |  Input:                                     |
        # |  |---------------------------------------|  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |---------------------------------------|  |
        # |                                             |
        # | ------------------------------------------- |
        # |                                             |
        # |  Output:                                    |
        # |  |---------------------------------------|  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |                                       |  |
        # |  |---------------------------------------|  |
        # |                                             |
        # |                   (Leave)                   |
        # |                                             |
        # |---------------------------------------------|

        self.grid()

        self.lbl_ip_address = ttk.Label(self, anchor=tk.E, text=' Input: ')
        self.lbl_ip_address.grid(column=0, row=0, sticky='w')

        self.input_text = ScrolledText.ScrolledText(self, state='normal')
        self.input_text.grid(column=0, row=1, columnspan=2, sticky='nesw', padx=3, pady=3)
        self.input_text.insert(tk.END, "Enter text to parse")

        self.lbl_ip_address = ttk.Label(self, anchor=tk.E, text=' Output: ')
        self.lbl_ip_address.grid(column=0, row=2, sticky='w')

        self.output_text = ScrolledText.ScrolledText(self, state='disabled')
        self.output_text.grid(column=0, row=3, columnspan=2, sticky='nesw', padx=3, pady=3)

        self.btn_convert = ttk.Button(self, text='Exit', command=self.handle_close)
        self.btn_convert.grid(column=0, row=3, columnspan=2, sticky='s', pady=15)

        self.resizable(True, True)
        self.minsize(300, 300)

        self.protocol("WM_DELETE_WINDOW", self.handle_close)

        text = threading.Thread( target=self.generate_parsed_text)
        text.daemon = True
        text.start()


    def handle_close( self ):
        exit( 0 )


    def generate_parsed_text( self ):
        while True:
            input_text = self.input_text.get( "1.0", tk.END )
            output_text = self.output_text.get( "1.0", tk.END )

            if str( input_text ) != "Enter text to parse\n":
                input_sentences = TextBlob( input_text ).sentences
                sentences = []

                for sentence in input_sentences:
                    sentences.append( str( sentence ) )

                regex = regex4dummies()

                # Getting tokenized string and dependencies ( if library is up to date )
                if regex.__version__ == "1.4.5":
                    final_literal_text = regex.compare_strings( parser='default', pattern_detection="literal", text=sentences )
                    final_literal_information = ""

                    # Getting parsed data to display
                    sentence_information = regex.get_pattern_information()
                    for sentence in sentence_information:
                        final_literal_information = "[ Pattern ]          : " + sentence.pattern
                        final_literal_information = "[ Subject ]          : " + sentence.subject + "\n"
                        final_literal_information = "[ Verb ]             : " + sentence.verb + "\n"
                        final_literal_information = "[ Object ]           : " + sentence.object[0] + "\n"
                        final_literal_information = "[ Reliability Score ]: " + str( sentence.reliability_score ) + "\n"

                    final_semantic_text = regex.compare_strings( parser='', pattern_detection="semantic", text=sentences )
                    final_semantic_information = ""

                    sentence_information = regex.get_pattern_information()
                    for sentence in sentence_information:
                        final_semantic_information = "[ Pattern ]          : " + sentence.pattern
                        final_semantic_information = "[ Subject ]          : " + sentence.subject + "\n"
                        final_semantic_information = "[ Verb ]             : " + sentence.verb + "\n"
                        final_semantic_information = "[ Object ]           : " + sentence.object[0] + "\n"
                        final_semantic_information = "[ Reliability Score ]: " + str( sentence.reliability_score ) + "\n"

                    # Getting possible topics for semantic information
                    topics = regex.get_topics( text=sentences )

                    # Instantiating toolkit object
                    gui_toolkit = Toolkit()

                    # Getting the tokenized input
                    tokenized_input = gui_toolkit.tokenize( text=input_text, parser="pattern" )

                    # Getting the dependency input
                    dependency_input = gui_toolkit.find_dependencies( text=input_text, parser="pattern" )

                    # Preparing final display data
                    final_text = "Literal Parse:\n" + str( final_literal_text ) + "\n\nInformation:\n" + final_literal_information + "\n---------------------------------\n\n" + "Semantic Parse:\n" + str( final_semantic_text ) + "\n\nInformation:\n" + final_semantic_information + "\n\nTopics:\n" + str( topics ) + "\n\nTokenized input:\n" + str( tokenized_input ) + "\n\nDependencies of input:\n" + str( dependency_input )
                else:
                    final_literal_text = regex.compare_strings( 'default', True, sentences )
                    final_literal_information = ""

                    # Getting parsed data to display
                    sentence_information = regex.get_sentence_information()
                    for sentence in sentence_information:
                        final_literal_information = "[ Pattern ]          : " + sentence.pattern
                        final_literal_information = "[ Subject ]          : " + sentence.subject + "\n"
                        final_literal_information = "[ Verb ]             : " + sentence.verb + "\n"
                        final_literal_information = "[ Object ]           : " + sentence.object[0] + "\n"
                        final_literal_information = "[ Reliability Score ]: " + str( sentence.reliability_score ) + "\n"

                    final_semantic_text = regex.compare_strings( '', False, sentences )
                    final_semantic_information = ""

                    sentence_information = regex.get_sentence_information()
                    for sentence in sentence_information:
                        final_semantic_information = "[ Pattern ]          : " + sentence.pattern
                        final_semantic_information = "[ Subject ]          : " + sentence.subject + "\n"
                        final_semantic_information = "[ Verb ]             : " + sentence.verb + "\n"
                        final_semantic_information = "[ Object ]           : " + sentence.object[0] + "\n"
                        final_semantic_information = "[ Reliability Score ]: " + str( sentence.reliability_score ) + "\n"

                    # Getting possible topics for semantic information
                    topics = regex.get_pattern_topics()

                    # Preparing final display data
                    final_text = "Literal Parse:\n" + str( final_literal_text ) + "\n\nInformation:\n" + final_literal_information + "\n---------------------------------\n\n" + "Semantic Parse:\n" + str( final_semantic_text ) + "\n\nInformation:\n" + final_semantic_information + "\n\nTopics:\n" + str( topics )

                # Displaying final data
                self.output_text['state'] = 'normal'
                self.output_text.delete( "1.0", tk.END )
                self.output_text.insert( "1.0", final_text )
                self.output_text['state'] = 'disabled'
            elif output_text != "":
                self.output_text['state'] = 'normal'
                self.output_text.delete( "1.0", tk.END )
                self.output_text['state'] = 'disabled'

            time.sleep( 1 )


if __name__ == '__main__':
    main_gui = Main()

    main_gui.mainloop()
