from model.location_model import Location

class Delegacy(Location):
    delegacy_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        Delegacy.delegacy_list.append(self)
