from view.common_view import *
from controller.data_controller import *


def main():
    show_location()
    handle_menu()


def handle_menu():
    ''' Main loop responsible for work of
    whole program
    '''
    choose = ""
    while choose != "0":

        print_menu(["List statistics", "Display 3 cities with longest names",
         "Display county's name with the largest number of communities",
          "Display locations, that belong to more than one category",
          "Advanced search"])

        choose = get_input()
        if choose == "1":
            start_data_controller()

        elif choose == "2":
            longest_city_name()

        elif choose == "3":
            biggest_district = biggest_district_by_commune()
            print_district_with_commune(biggest_district)

        elif choose == "4":
            more_than_one_category()

        elif choose == "5":
            advanced_search()


if __name__ == '__main__':
    main()
