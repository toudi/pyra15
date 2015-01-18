from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QColor
from PyQt5.Qt import Qt
from random import randint


class Model(QStandardItemModel):
    def addItem(self, label):
        item = QStandardItem(label)
        item.setData(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), Qt.DecorationRole)
        self.appendRow(item)
