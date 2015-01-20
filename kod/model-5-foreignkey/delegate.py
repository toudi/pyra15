from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.Qt import Qt


class ComboDelegate(QItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent, model):
        super(ComboDelegate, self).__init__(parent)
        # QItemDelegate.__init__(self, parent)
        self.model = model

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.setModel(self.model)
        combo.currentIndexChanged.connect(self.currentIndexChanged)
        return combo

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(
            editor.findData(
                index.model().data(index, Qt.EditRole),
                Qt.EditRole
            )
        )
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(
            index,
            editor.itemData(editor.currentIndex(), Qt.EditRole), Qt.EditRole
        )
        model.setData(
            index,
            editor.itemData(editor.currentIndex(), Qt.DisplayRole), Qt.DisplayRole
        )

    # @pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())
