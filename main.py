# Name: Max Sealey || Student ID: 010332991

import csv
import datetime
import utility

from custom_classes import Package
from custom_classes import Truck
from custom_classes import HashTable

with open('./csv_data/addresses.csv') as addresses:
    address_reader = list(csv.reader(addresses, delimiter=','))

with open('./csv_data/distances.csv') as distances:
    distance_reader = list(csv.reader(distances, delimiter=','))

with open('./csv_data/packages.csv') as pkg_data:
    package_reader = list(csv.reader(pkg_data, delimiter=','))

# def greedy_algo():

def load_packages(pkgs, table):
    for p in pkgs:
        id = int(p[0])
        address = p[1]
        city = p[2]
        state = p[3]
        zip = p[4]
        deadline = p[5]
        weight = p[6]
        notes = p[7]

        pkg = Package.Package(id, address, city, state, zip, deadline, weight, notes)
        table.insert(id, pkg)


# fill hash table with package data
hash_table = HashTable.HashTable()
load_packages(package_reader, hash_table)


truck1 = Truck.Truck(1, "HUB", datetime.timedelta(hours=8), [1, 2, 4, 6, 13, 14, 15, 16, 17, 19, 20, 21, 34, 39, 40])
truck2 = Truck.Truck(2, "HUB", datetime.timedelta(hours=9, minutes=5), [3, 5, 18, 24, 25, 26, 29, 30, 31, 36, 37, 38])
truck3 = Truck.Truck(3, "HUB", datetime.timedelta(hours=10, minutes=30), [7, 8, 9, 10, 11, 12, 22, 23, 27, 28, 32, 33, 35])




# CLI
def run_program():
    # if user doesn't enter a valid option, loops back
    valid_input = 0

    while valid_input == 0:
        res = input(
            '''
    --------------------------------------------------------------
    Welcome to the WGUPS Routing System
    --------------------------------------------------------------
    If you would like to view the delivery status of all packages at a 
    particular time, type 'all' and hit enter (case-sensitive).
    
    If you would like to get the status of a single package at a 
    particular time, type 'one' and hit enter (case-sensitive).
        
    If you would like to view the status of our delivery trucks
    and total mileage, type 'miles' and hit enter (case-sensitive). 
    
    Type 'q' and hit enter to quit.
    
    '''
        )
        # exits program
        if res == 'q':
            break

        # continues loop if option invalid
        elif res != 'all' and res != 'one' and res != 'miles':
            print("Please enter a valid input.")
            continue

        # see status of all packages
        elif res == 'all':

            valid_input = 1

        # see status of a single package
        elif res == 'one':
            time = input(
                '''
    Please enter the time at which you would like to check 
    the package status (format: HH:MM:SS).
    ''')
            valid_input = 1

        # check truck status and mileage
        else:
            valid_input = 1


run_program()
