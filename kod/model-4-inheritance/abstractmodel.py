from PyQt5.Qt import Qt
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import QAbstractTableModel


class AbstractModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.cols_indexes_cache = None
        super(AbstractModel, self).__init__(*args, **kwargs)

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return len(self.columns)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.columns[col][1])
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        column = index.column()

        self.items[row][self.getColName(column)] = value

        self.dataChanged.emit(index, index)
        return True

    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole: # or True: # !!! UWAGA !!!
            return self.items[row].get(self.getColName(column), '')
        return None

    def insertRows(self, row, count, parent):
        self.beginInsertRows(QModelIndex(), row, row + count - 1)
        self.items.append({})
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent):
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        n = row
        while n < row + count:
            self.items.pop(n)
            n+=1
        self.endRemoveRows()
        return True

    #### POMOCNICZE ######

    def getColNum(self, colname):
        if not self.cols_indexes_cache:
            self.cols_indexes_cache = {}
            for colno, column in enumerate(self.columns):
                self.cols_indexes_cache[column[0]] = colno

        return self.cols_indexes_cache[colname]

    def getColName(self, colnum):
        return self.columns[colnum][0]

