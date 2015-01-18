#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.Qt import Qt
from model import Model


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.index = None

        self.model = Model()

        self.setupUi()
        self.table.setModel(self.model)

    def selectItem(self, index):
        self.edityear.setValue(
            int(self.model.data(index.sibling(
                index.row(),
                self.model.getColNum("manufactured")), Qt.DisplayRole) or 1900)
        )
        self.editbrand.setText(
            self.model.data(index.sibling(
                index.row(),
                self.model.getColNum("brand")), Qt.DisplayRole)
        )
        self.index = index

    def addItem(self):
        self.model.insertRows(self.model.rowCount(None), 1, None)

    def saveItem(self):
        self.model.setData(
            self.index.sibling(self.index.row(), self.model.getColNum("manufactured")),
            self.edityear.value(),
            Qt.DisplayRole
        )
        self.model.setData(
            self.index.sibling(self.index.row(), self.model.getColNum("brand")),
            self.editbrand.text(),
            Qt.DisplayRole
        )

    def removeItem(self):
        if self.index:
            self.model.removeRow(self.index.row())
            self.index = None

    def setupUi(self):
        mainLayout = QVBoxLayout()

        layout = QHBoxLayout()
        gb = QGroupBox("Edycja")

        self.table = QTableView()

        layout.addWidget(self.table)
        layout.addWidget(gb)

        editLayout = QVBoxLayout()
        self.edityear = QSpinBox()
        self.edityear.setMinimum(1900)
        self.edityear.setMaximum(9999)
        self.editbrand = QLineEdit()
        buttonAdd = QPushButton("Dodaj")
        buttonSave = QPushButton("Zapisz")
        buttonRemove = QPushButton("Won")
        editLayout.addWidget(self.edityear)
        editLayout.addWidget(self.editbrand)
        editLayout.addWidget(buttonSave)
        editLayout.addWidget(buttonAdd)
        editLayout.addWidget(buttonRemove)
        gb.setLayout(editLayout)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)
        buttonAdd.clicked.connect(self.addItem)
        buttonSave.clicked.connect(self.saveItem)
        buttonRemove.clicked.connect(self.removeItem)
        self.table.clicked.connect(self.selectItem)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
