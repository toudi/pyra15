from restmodel import RestModel
from PyQt5.Qt import Qt

HOST = 'localhost:8080'


class CarBrand(RestModel):
    columns = (
        ("id", "ID", {'role': Qt.EditRole}),
        ("name", "Nazwa", {'role': Qt.DisplayRole})
    )
    host = HOST
    service = 'brands'


brand = CarBrand()


class CarModel(RestModel):
    columns = (
        ("id", "ID", {}),
        ("manufactured", "Rok produkcji", {}),
        ("brand_id", "Marka", {})
    )
    model_mapping = {"brand_id": brand}
    host = HOST
    service = 'cars'
