__author__ = 'Vale Tolpegin'

# Importing GUI related libraries
import Tkinter as tk
import ttk as ttk
import tkMessageBox
import tarfile

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

    def download( self, summary, dependency_name, dependency_size ):
        self.summary = summary
        self.dependency_name = dependency_name
        self.dependency_size = dependency_size

        self.initialize( summary, dependency_name, dependency_size )

        self.mainloop()

    def initialize( self, summary, dependency_name, dependency_size ):
        self.grid()

        self.lbl_summary = ttk.Label( self, anchor=tk.E, text=summary)
        self.lbl_summary.grid( column=0, row=0, sticky='nesw', padx=15, pady=10)

        self.lbl_name = ttk.Label(self, anchor=tk.E, text=' Dependency Name:  ' + dependency_name)
        self.lbl_name.grid(column=0, row=1, sticky='w', padx=15)

        self.lbl_size = ttk.Label(self, anchor=tk.E, text=' Dependency Size:     ' + dependency_size)
        self.lbl_size.grid(column=0, row=2, sticky='w', padx=15)

        self.btn_download = ttk.Button( self, text='Download', command=self.download_dependency)
        self.btn_download.grid( column=0, row=3, columnspan=2, sticky='s')

        self.btn_close = ttk.Button(self, text='Exit', command=self.handle_close)
        self.btn_close.grid(column=0, row=4, columnspan=2, sticky='s', pady=15)

        self.resizable(False, False)
        self.minsize(200, 200)

        self.protocol("WM_DELETE_WINDOW", self.handle_close)

    def handle_close( self ):
        print ""
        print "The dependencies must be downloaded to use this parser. Either remove that piece of code or download the dependencies."
        print ""

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

            # Download the dependencies & extract
            current_directory = os.getcwd()

            os.mkdir( path )
            os.chdir( path )

            os.system( "wget http://nilc.icmc.usp.br/nlpnet/data/dependency-en.tgz" )
            tar = tarfile.open( path + 'dependency-en.tgz', 'r:gz' )
            tar.extractall( path )
            os.remove( path + 'dependency-en.tgz' )

            os.chdir( current_directory )

        self.quit()

if __name__ == '__main__':
    pass

    #my_GUI = gui_downloader()
    #my_GUI.download( "This is a test of text", "nlpnet Corpora", "1 GB" )

    #my_GUI.mainloop()
