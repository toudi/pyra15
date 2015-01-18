#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.model = QStringListModel(["foo", "bar", "baz"])
        self.setupUi()
        self.combo.setModel(self.model)
        self.list.setModel(self.model)
        self.table.setModel(self.model)

    def setupUi(self):
        mainLayout = QVBoxLayout()

        layout = QHBoxLayout()
        self.combo = QComboBox()
        self.list = QListView()
        self.table = QTableView()

        layout.addWidget(self.combo)
        layout.addWidget(self.list)
        layout.addWidget(self.table)

        button = QPushButton("Guzior")
        button2 = QPushButton("Paszoł won")
        button.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.removeEntry)
        mainLayout.addLayout(layout)
        mainLayout.addWidget(button)
        mainLayout.addWidget(button2)
        self.setLayout(mainLayout)

    def buttonClicked(self):
        _list = self.model.stringList()

        for i in range(100):
            _list.append('%d red baloons' % i)

        self.model.setStringList(_list)

    def removeEntry(self):
        self.model.removeRows(3, 100)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
