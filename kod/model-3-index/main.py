#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from model import Model


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.index = None

        rolemodel = Model()
        rolemodel.addItem("Foo")
        rolemodel.addItem("Bar")
        rolemodel.addItem("Baz")
        self.model = rolemodel

        self.setupUi()
        self.list.setModel(rolemodel)

    def selectItem(self, index):
        self.edit.setText(self.model.data(index))
        self.index = index

    def addItem(self):
        self.model.addItem(self.edit.text())

    def saveItem(self):
        self.model.setData(self.index, self.edit.text())

    def removeItem(self):
        self.model.takeRow(self.index.row())
        self.edit.setText('')

    def setupUi(self):
        mainLayout = QVBoxLayout()

        layout = QHBoxLayout()
        gb = QGroupBox("Edycja")

        self.list = QListView()
        self.table = QTableView()

        layout.addWidget(self.list)
        layout.addWidget(gb)

        editLayout = QVBoxLayout()
        self.edit = QLineEdit()
        buttonAdd = QPushButton("Dodaj")
        buttonSave = QPushButton("Zapisz")
        buttonRemove = QPushButton("Paszoł won")
        editLayout.addWidget(self.edit)
        editLayout.addWidget(buttonSave)
        editLayout.addWidget(buttonAdd)
        editLayout.addWidget(buttonRemove)
        gb.setLayout(editLayout)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)
        buttonAdd.clicked.connect(self.addItem)
        buttonSave.clicked.connect(self.saveItem)
        buttonRemove.clicked.connect(self.removeItem)
        self.list.clicked.connect(self.selectItem)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
