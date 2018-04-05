from model.commune_model import Commune

class VillageRegion(Commune):
    village_region_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        VillageRegion.village_region_list.append(self)
