from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QColor
from PyQt5.Qt import Qt
from random import randint
from abstractmodel import AbstractModel


class Model(AbstractModel):
    columns = (
        ("manufactured", "Rok produkcji"),
        ("brand", "Marka")
    )
