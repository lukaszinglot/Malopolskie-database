from controller.data_controller import *

class Location:
    location_list = []

    def __init__(self, district, commune, name, type_name):
        self.district = district
        self.commune = commune
        self.name = name
        self.type_name = type_name
        self.__class__.location_list.append(self)
