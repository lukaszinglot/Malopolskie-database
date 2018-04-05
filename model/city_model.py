from model.district_model import District

class City(District):
    city_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        City.city_list.append(self)
