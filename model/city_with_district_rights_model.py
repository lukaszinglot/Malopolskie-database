from model.district_model import District

class CityDistrictRight(District):
    district_city_list = []

    def __init__(self, district, commune, name, type_name):
        super().__init__(district, commune, name, type_name)
        CityDistrictRight.district_city_list.append(self)
