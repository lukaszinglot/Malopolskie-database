from prettytable import PrettyTable
from operator import attrgetter
from tabulate import tabulate


def print_menu(menu_list):
    '''
    Function that take menu options from a file, and print it on the screen.
    ---------------------------------
    Return:
        It prints menu options
    '''
    main_just = 6
    exit_just = 10
    for options in range(0, len(menu_list)):
        print("(".rjust(main_just), options + 1, ")", (menu_list[options]))
    print("( 0 )".rjust(exit_just) + " Exit program")


def get_input(answer=''):
    '''
    Function that ask user about his answer
    ---------------------------------
    Return:
        string with your input
    '''
    return input(answer)


def print_list(list_):
    '''
    Function that print every element in list_
    ---------------------------------
    Return:
        None
    '''
    x = PrettyTable()
    x.field_names = ["MAŁOPOLSKIE", "WOJEWÓDZTWO"]
    for key, value in list_.items():
        x.add_row([value, key])
    print(x)


def print_longest_name(sorted_city):
    '''
    Function that print city with longest name
    --------------------------------------
    Return:
        None
    '''
    for city in sorted_city[0:3]:
        print(city.name)


def print_error():
    """
    Function that displays an error message
    -----------------------------------
    Returns:
        None
    """
    print('Error')


def print_table_advanced_search(attr_temp_list):
    '''
    Function that prints table with searching location
    -------------------------------------
    Return:
        None
    '''
    print(tabulate(attr_temp_list, headers=["Location", "Type"], tablefmt='pipe'))


def get_choice():
    '''
    Function that ask user about his choise(which option did he take in menu)
    ---------------------------------
    Return:
        string with your input
    '''
    return input("Your choice : ")


def print_place_category(duplicate_locations):
    '''
    Function that print table with location, that belongs to more than one category
    --------------------------------
    Return:
        None
    '''
    print(tabulate(duplicate_locations, headers=["More than 1 category locations"], tablefmt='fancy_grid'))


def get_search():
    '''
    Function that ask user about his input.
    ---------------------------------
    Return:
        None
    '''
    return (input("What do you want to find ? : ").lower())


def print_district_with_commune(biggest_district):
    '''
    Function that print district with biggest amount of commune
    ---------------------------------
    Return:
        None
    '''
    print('Powiat ' + ' --> ' + biggest_district.district )
