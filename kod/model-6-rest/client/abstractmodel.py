from PyQt5.Qt import Qt
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import pyqtSignal
from delegate import ComboDelegate


class AbstractModel(QAbstractTableModel):
    itemsUpdated = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        self.items = []
        self.cols_indexes_cache = None
        self.cols_roles_cache = None
        super(AbstractModel, self).__init__(*args, **kwargs)
        self.getColNum()

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

        colname = self.getColName(column)

        # if colname in self.model_mapping and role == Qt.EditRole:
        #     colname = '%s_id' % colname

        self.items[row][colname] = value

        self.dataChanged.emit(index, index)
        self.itemsUpdated.emit(self.items)
        return True

    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role in self.cols_roles_cache:
            return self.items[row].get(self.cols_roles_cache[role])

        value = self.items[row].get(self.getColName(column))

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if value and self.getColName(column) in self.model_mapping and role == Qt.DisplayRole:
                foreign_model = self.model_mapping[self.getColName(column)]
                foreign_index = foreign_model.index(value - 1, foreign_model.getColNum("name"))
                return foreign_model.data(foreign_index, Qt.DisplayRole)
            return value

        return QVariant()

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

    def registerDelegates(self, view):
        for column, model_class in self.model_mapping.items():
            view.setItemDelegateForColumn(
                self.getColNum(column),
                ComboDelegate(view, model_class)
            )

    # ######### !!!! UWAGA !!!! ########
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    #### POMOCNICZE ######

    def getColNum(self, colname=None):
        if not self.cols_indexes_cache:
            self.cols_indexes_cache = {}
            self.cols_roles_cache = {}
            for colno, column in enumerate(self.columns):
                col_name, col_label, col_attrs = column
                self.cols_indexes_cache[col_name] = colno
                if col_attrs and 'role' in col_attrs:
                    self.cols_roles_cache[col_attrs['role']] = col_name

        if colname:
            return self.cols_indexes_cache[colname]

    def getColName(self, colnum):
        return self.columns[colnum][0]

