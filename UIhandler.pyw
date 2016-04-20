from PyQt4 import QtCore, QtGui
# -*- coding: UTF-8 -*-
from load_picle_copy import data_process

outputData = u'''
    الإيمان بالله
'''

class FormGui(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FormGui, self).__init__(parent)

        self.urlLabel = QtGui.QLabel("URL:")
        self.urlLineEdit = QtGui.QLineEdit()
        self.urlLineEdit.setText('http://abuaminaelias.com/brotherhood-in-the-quran-and-sunnah/')

        self.hitListLabel = QtGui.QLabel("Hit List:")
        self.addressText = QtGui.QTextEdit()
        self.addressText.setReadOnly(True)

        self.evalButton = QtGui.QPushButton("Eval")
        self.evalButton.show()
        
        self.evalButton.clicked.connect(self.doEval)
        
        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.urlLabel, 0, 0)
        mainLayout.addWidget(self.urlLineEdit, 0, 1)
        mainLayout.addWidget(self.hitListLabel, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 1, 1)
        mainLayout.addWidget(self.evalButton, 1, 2, QtCore.Qt.AlignTop)

        self.setLayout(mainLayout)
        self.setWindowTitle("Quran ayat checker")
        self.setMinimumSize(800, 450)
    
    def doEval(self):
        self.urlLineEdit.setReadOnly(True)
        self.addressText.setHtml(data_process(str(self.urlLineEdit.text())))
        # self.addressText.setText(outputData)
        
        # print url, outputData

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    addressBook = FormGui()
    addressBook.show()

    sys.exit(app.exec_())
