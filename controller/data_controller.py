from view.common_view import *
from model.location_model import Location
from model.district_model import District
from model.urban_commune import UrbanCommune
from model.village_commune import VillageCommune
from model.village_region_model import VillageRegion
from model.delegacy_model import Delegacy
from model.city_with_district_rights_model import CityDistrictRight
from model.mixed_commune_model import MixedCommune
from model.city_model import City
import operator
from operator import attrgetter
import csv
from collections import Counter


def start_data_controller():
    '''
    Function that start data_controller by taking data from csv file
    -----------------------------
    Return:
        None
    '''
    location = show_location()
    data_counter(show_location())


def data_counter(location_list):
    '''
    Function that counts elements by index
    -----------------------------
    Return:
        None
    '''
    location_count = Counter(x for sublist in location_list for x in sublist)
    location_type = Counter(sublist[5] for sublist in location_list)
    print_list(location_type)


def show_location():
    '''
    Function that take data from csv and ascrabe it to class.
    -------------------------
    Return:
        list with data
    '''
    try:
        with open("malopolska.csv", 'r') as f:
            file_data = []
            for line in f:
                data_line = line.rstrip().split('\t')
                file_data.append(data_line)

            for line in file_data:

                district = line[1]
                commune = line[2]
                name = line[4]
                type_name = line[5]

                if type_name == "powiat":
                    District(district, commune, name, type_name)
                elif type_name == "gmina miejska":
                    UrbanCommune(district, commune, name, type_name)
                elif type_name == "gmina wiejska":
                    VillageCommune(district, commune, name, type_name)
                elif type_name == "gmina miejsko-wiejska":
                    MixedCommune(district, commune, name, type_name)
                elif type_name == "obszar wiejski":
                    VillageRegion(district, commune, name, type_name)
                elif type_name == "miasto":
                    City(district, commune, name, type_name)
                elif type_name == "miasto na prawach powiatu":
                    CityDistrictRight(district, commune, name, type_name)
                elif type_name == "delegatura":
                    Delegacy(district, commune, name, type_name)
    except FileNotFoundError:
        print('Program cant find that file')
        exit()
    return file_data [1:]


def longest_city_name():
    '''
    Function that find longest city name
    --------------------------
    Return:
        None
    '''
    sorted_city = sorted(City.city_list, key=lambda x: -len(x.name))
    print_longest_name(sorted_city)


def biggest_district_by_commune():
    '''
    Function that counts communes by district, and take the biggest district
    ---------------------------
    Return:
        number that is biggest district
    '''
    biggest_district = max(Location.location_list, key=attrgetter("commune"))
    for element in District.district_list:
        if element.district == biggest_district.district:
            return biggest_district


def more_than_one_category():
    '''
    Function that search for city, that belongs to more than one category
    ----------------------------
    Return:
        None
    '''
    city_name_list = []

    for city in Location.location_list:
        city_name_list.append(city.name)

    duplicate_locations = [[k] for k, v in Counter(city_name_list).items() if v > 1]
    print_place_category(duplicate_locations)


def advanced_search():
    '''
    Function that takes input from user, and then search in list by uning it
    ----------------------------
    Return:
        None
    '''
    search = get_search()
    temporary_list = []

    for location in Location.location_list:
        if search in location.name.lower():
            temporary_list.append(location)

    if not temporary_list:
        print_error()

    else:
        sorted_temporary_list = sorted(temporary_list, key=operator.attrgetter('name', 'type_name'))
        attr_temp_list = []
        for element in sorted_temporary_list:
            attr_temp_list.append([element.name, element.type_name])

        print_table_advanced_search(attr_temp_list)
