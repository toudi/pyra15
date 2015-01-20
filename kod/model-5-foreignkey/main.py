#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.Qt import Qt
from model import CarModel
from json import dumps


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.index = None

        self.model = CarModel()
        self.model.items = [
            {'manufactured': 1999, 'brand': 'Volvo'}
        ]

        self.setupUi()
        self.table.setModel(self.model)
        # self.table.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed | QAbstractItemView.AnyKeyPressed)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.table.setSelectionMode()
        self.model.registerDelegates(self.table)
        self.model.itemsUpdated.connect(lambda it: self.dumper.setPlainText(dumps(it, indent=3)))

    def addItem(self):
        self.model.insertRows(self.model.rowCount(None), 1, None)

    def selectItem(self, index):
        self.index = index

    def removeItem(self):
        index = self.table.selectedIndexes()
        if index and index[0].isValid():
            self.model.removeRow(index[0].row())

    def setupUi(self):
        mainLayout = QVBoxLayout()

        layout = QHBoxLayout()
        gb = QGroupBox("Edycja")
        self.dumper = QPlainTextEdit()

        self.table = QTableView()

        layout.addWidget(self.table)
        layout.addWidget(gb)
        layout.addWidget(self.dumper)

        editLayout = QVBoxLayout()
        buttonAdd = QPushButton("Dodaj")
        buttonRemove = QPushButton("Won")
        editLayout.addWidget(buttonAdd)
        editLayout.addWidget(buttonRemove)
        gb.setLayout(editLayout)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)
        buttonAdd.clicked.connect(self.addItem)
        buttonRemove.clicked.connect(self.removeItem)
        # self.table.clicked.connect(self.selectItem)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
