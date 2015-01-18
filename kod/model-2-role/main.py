#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from model import Model


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        rolemodel = Model()
        rolemodel.addItem("Foo")
        rolemodel.addItem("Bar")
        rolemodel.addItem("Baz")

        self.setupUi()
        self.combo.setModel(rolemodel)
        self.list.setModel(rolemodel)
        self.table.setModel(rolemodel)

    def setupUi(self):
        mainLayout = QVBoxLayout()

        layout = QHBoxLayout()
        self.combo = QComboBox()
        self.list = QListView()
        self.table = QTableView()

        layout.addWidget(self.combo)
        layout.addWidget(self.list)
        layout.addWidget(self.table)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
