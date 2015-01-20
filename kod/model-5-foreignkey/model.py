from abstractmodel import AbstractModel
from PyQt5.Qt import Qt


class CarBrand(AbstractModel):
    columns = (
        ("id", "ID", {'role': Qt.EditRole}),
        ("name", "Nazwa", {'role': Qt.DisplayRole})
    )

brand = CarBrand()
brand.items = [{'id': 1, 'name': 'BMW'}, {'id': 2, 'name': 'Volkswagen'}]


class CarModel(AbstractModel):
    columns = (
        ("manufactured", "Rok produkcji", {}),
        ("brand", "Marka", {})
    )
    model_mapping = {"brand": brand}
