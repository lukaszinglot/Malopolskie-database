from model.commune_model import Commune

class MixedCommune(Commune):
    mixed_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        MixedCommune.mixed_list.append(self)
