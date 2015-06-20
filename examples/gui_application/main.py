__author__ = 'Vale Tolpegin'

import os, sys
import TKinter as tk
import ttk as ttk

class main:
    def __init__( self, *args, **kwargs ):
        tk.Tk.__init__(self, *args, **kwargs)

        self.initialize()

    def initialize( self ):
        self.grid()

        # Grid Design:
        # |---------------------------------------------|
        # |  Input Text:      Parsing To Apply: (Menu)  |
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

    def generate_frame( self ):
        pass

if __name__ == '__main__':
    pass
