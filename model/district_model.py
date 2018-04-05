from model.location_model import Location

class District(Location):
    district_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        District.district_list.append(self)
