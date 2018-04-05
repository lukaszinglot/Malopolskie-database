from model.commune_model import Commune

class UrbanCommune(Commune):
    urban_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        UrbanCommune.urban_list.append(self)
