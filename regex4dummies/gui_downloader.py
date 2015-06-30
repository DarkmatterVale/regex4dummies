__author__ = 'Vale Tolpegin'

# Importing GUI related libraries
import Tkinter as tk
import ttk as ttk
import tkMessageBox
import ScrolledText

# Importing OS related libraries
import os, sys, re
from subprocess import *

"""

This class serves as a generic downloader GUI. It will enable the run_dependency_tests class to download libraries using a single set of code, rather than multiple sets of the same code.

Class information:

- name: gui_downloader
- version: 1.0.0

"""

class gui_downloader( tk.Tk ):
    def __init__( self, *args, **kwargs ):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title( 'GUI Downloader' )

    def download( self, dependency_name, dependency_size ):
        self.dependency_name = dependency_name
        self.dependency_size = dependency_size

        self.initialize( dependency_name, dependency_size )

    def initialize( self, dependency_name, dependency_size ):
        self.grid()

        self.lbl_name = ttk.Label(self, anchor=tk.E, text=' Dependency Name:  ' + dependency_name)
        self.lbl_name.grid(column=0, row=0, sticky='w', padx=15)

        self.lbl_size = ttk.Label(self, anchor=tk.E, text=' Dependency Size:     ' + dependency_size)
        self.lbl_size.grid(column=0, row=1, sticky='w', padx=15)

        self.btn_close = ttk.Button(self, text='Exit', command=self.handle_close)
        self.btn_close.grid(column=0, row=3, columnspan=2, sticky='s', pady=15)

        self.btn_download = ttk.Button( self, text='Download', command=self.download_dependency)
        self.btn_download.grid( column=0, row=4, columnspan=2, sticky='s')

        self.resizable(False, False)
        self.minsize(200, 200)

        self.protocol("WM_DELETE_WINDOW", self.handle_close)

    def handle_close( self ):
        self.quit()

    def download_dependency( self ):
        if 'nltk' in self.dependency_name.lower():
            # Downloading the dependency
            os.system( "python -m nltk.downloader all" )
        elif 'textblob' in self.dependency_name.lower():
            # Downloading the dependency
            os.system( "python -m textblob.download_corpora" )
        elif 'nlpnet' in self.dependency_name.lower():
            # Getting nltk data path
            running = Popen( [ 'python -c "import nltk;print nltk.data.path"' ], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True )
            stdin, stdout = running.communicate()

            # Setting the path that the nlpnet dependency will be downloaded from
            path = re.sub( r"\'", "", re.sub( r"\[", '', str( stdin.split( '\n' )[ 0 ].split( ',' )[ 0 ] ) ) )
            path = path.split( r"/" )
            path = '/'.join( path[ 0 : len( path ) - 1 ] ) + '/nlpnet_dependency/'

            # Save path to the data file
            path_file = open( 'data.txt', 'w' )
            path_file.write( path )
            path_file.close()

            # Download the dependencies
            os.mkdir( path )
            os.chdir( path )
            #os.system( "wget https://github.com/DarkmatterVale/regex4dummies/" )

if __name__ == '__main__':
    #pass

    my_GUI = gui_downloader()
    my_GUI.download( "nlpnet Corpora", "1 GB" )

    my_GUI.mainloop()
