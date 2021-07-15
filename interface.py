from  PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
#from PyQt5.uic import loadUiType
#MainUI,_ = loadUiType('xml.ui')
#import re

from NEW_ERROR_FINAL import *

from main import Ui_MainWindow


class Main(QMainWindow,Ui_MainWindow):


    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.show_file.setEnabled(False)
        self.pretty_button.setEnabled(False)
        self.minify_button.setEnabled(False)
        self.compress_button.setEnabled(False)
        self.decompress_button.setEnabled(False)
        self.jason_button.setEnabled(False)
        #self.original_button.setEnabled(False)

        self.check_consistency.clicked.connect(self.print_error)
        self.check_consistency.clicked.connect(self.open_consistency)  # function
        #self.check_consistency.clicked.connect(self.activate_original)


        self.show_file.clicked.connect(self.open_file_consistency) # show file button
        self.show_file.clicked.connect(self.open_button)


        self.pretty_button.clicked.connect(self.print_pretty)
        self.minify_button.clicked.connect(self.print_minify)
        self.compress_button.clicked.connect(self.print_compress)
        self.decompress_button.clicked.connect(self.print_decompress)
        self.jason_button.clicked.connect(self.print_jason)

        #self.original_button.clicked.connect(self.open_original)



def main():
    app=QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()