# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xml.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 338)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 231, 231, 121), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.check_consistency = QtWidgets.QPushButton(self.centralwidget)
        self.check_consistency.setGeometry(QtCore.QRect(660, 90, 131, 51))
        self.check_consistency.setObjectName("check_consistency")
        self.pretty_button = QtWidgets.QPushButton(self.centralwidget)
        self.pretty_button.setGeometry(QtCore.QRect(10, 220, 141, 51))
        self.pretty_button.setObjectName("pretty_button")
        self.jason_button = QtWidgets.QPushButton(self.centralwidget)
        self.jason_button.setGeometry(QtCore.QRect(650, 220, 141, 51))
        self.jason_button.setObjectName("jason_button")
        self.minify_button = QtWidgets.QPushButton(self.centralwidget)
        self.minify_button.setGeometry(QtCore.QRect(170, 220, 141, 51))
        self.minify_button.setObjectName("minify_button")
        self.compress_button = QtWidgets.QPushButton(self.centralwidget)
        self.compress_button.setGeometry(QtCore.QRect(330, 220, 141, 51))
        self.compress_button.setObjectName("compress_button")
        self.decompress_button = QtWidgets.QPushButton(self.centralwidget)
        self.decompress_button.setGeometry(QtCore.QRect(490, 220, 141, 51))
        self.decompress_button.setObjectName("decompress_button")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(170, 160, 171, 31))
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.show_file = QtWidgets.QPushButton(self.centralwidget)
        self.show_file.setGeometry(QtCore.QRect(360, 160, 121, 31))
        self.show_file.setObjectName("show_file")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 481, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#00007f;\">Xml Editor</span></p></body></html>"))
        self.check_consistency.setText(_translate("MainWindow", "import file "))
        self.pretty_button.setText(_translate("MainWindow", "Show Prettify Xml file"))
        self.jason_button.setText(_translate("MainWindow", "Show json file"))
        self.minify_button.setText(_translate("MainWindow", "Show minify xml file "))
        self.compress_button.setText(_translate("MainWindow", "Show compress file"))
        self.decompress_button.setText(_translate("MainWindow", "Show decompress file"))
        self.lineEdit_1.setPlaceholderText(_translate("MainWindow", "      Number of errors"))
        self.show_file.setText(_translate("MainWindow", "Show corrected file"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline; color:#550000;\">Directory Name</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
