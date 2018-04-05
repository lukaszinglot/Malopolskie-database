from model.commune_model import Commune

class VillageCommune(Commune):
    village_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        VillageCommune.village_list.append(self)
