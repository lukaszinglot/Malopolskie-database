from model.location_model import Location

class Commune(Location):
    commune_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        Commune.commune_list.append(self)
