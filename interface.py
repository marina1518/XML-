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

    def open_consistency(self):
        self.show_file.setEnabled(True)


    def open_button(self):
        self.pretty_button.setEnabled(True)
        self.minify_button.setEnabled(True)
        self.compress_button.setEnabled(True)
        self.decompress_button.setEnabled(True)
        self.jason_button.setEnabled(True)

    def import_file(self):
        file_filter='Data File(*.xml)'

        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File(*.xml)'
        )
        print(response[0])
        word_url =str(response[0]).replace('[','')
        word_url = word_url.replace(']', '')
        word_url = word_url.replace("'", '')
        self.lineEdit_2.setText(word_url)
        #file_name = re.split('/', word_url)
        #print(file_name[-1])
        os.startfile(word_url)
        return word_url


    def print_error(self):
        error=send_error(show_file(consistency(import_url(self.import_file()))))
        if error==0:
            error="zero"
        self.lineEdit_1.setText(str(error))

    def open_file_consistency(self):
        os.startfile("consistency.xml")


    def print_pretty(self):
        os.startfile("pretty.xml")

    def print_minify(self):
        os.startfile("minify.xml")

    def print_compress(self):
        os.startfile("compressed.txt")

    def print_decompress(self):
        os.startfile("decompressed.txt")

    def print_jason(self):
        os.startfile("jason.json")


def main():
    app=QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()