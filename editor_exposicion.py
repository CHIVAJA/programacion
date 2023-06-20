# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:43:36 2023

@author: pared
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Editor')
        self.show()

    def createActions(self):
        self.newAct = QAction('New', self)
        self.newAct.setShortcut('Ctrl+N')
        self.newAct.triggered.connect(self.newFile)

        self.openAct = QAction('Open', self)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.triggered.connect(self.openFile)

        self.saveAct = QAction('Save', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.triggered.connect(self.saveFile)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setPlainText(file.read())

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())