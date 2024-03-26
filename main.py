"""
Name: Max Sealey || Student ID: 010332991
WGU C950 Final Project: GPS Routing Program
"""

import csv
import datetime
import dist_utility
import time_utility

from custom_classes import Package
from custom_classes import Truck
from custom_classes import HashTable


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

        # bandaid patch to fix formatting inconsistencies
        if address == "600 E 900 South":
            address = "600 E 900 S"
        elif address == "6351 South 900 East":
            address = "6351 S 900 E"
        elif address == "5100 South 2700 West":
            address = "5100 S 2700 W"
        elif address == "5383 South 900 East #104":
            address = "5383 S 900 E #104"

        pkg = Package.Package(id, address, city, state, zip, deadline, weight, notes)
        table.insert(id, pkg)


# CLI
def run_program():
    # Open each of the csv  and extract lists of data
    with open('./csv_data/packages.csv') as pkg_data:
        package_list = list(csv.reader(pkg_data, delimiter=','))

    with open('./csv_data/addresses.csv') as addresses:
        address_list = list(csv.reader(addresses, delimiter=','))

    with open('./csv_data/distances.csv') as distances:
        distance_list = list(csv.reader(distances, delimiter=','))

    # fill hash table with package data
    hash_table = HashTable.HashTable()
    load_packages(package_list, hash_table)

    truck1 = Truck.Truck(1, "HUB", datetime.timedelta(hours=8),
                         [1, 13, 14, 15, 16, 17, 19, 20, 21, 29, 30, 34, 37, 39, 40])
    truck2 = Truck.Truck(2, "HUB", datetime.timedelta(hours=9, minutes=5),
                         [3, 4, 5, 6, 18, 24, 25, 26, 31, 36, 38])
    truck3 = Truck.Truck(3, "HUB", datetime.timedelta(hours=10, minutes=30),
                         [2, 7, 8, 9, 10, 11, 12, 22, 23, 27, 28, 32, 33, 35])

    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck1)
    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck2)
    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck3)

    # if user doesn't enter a valid option, loops back
    valid_input = 0

    while valid_input == 0:
        res = input(
            '''
    --------------------------------------------------------------
    Welcome to the WGUPS Routing System
    --------------------------------------------------------------
    If you would like to view the delivery times of all packages, 
    type '1' and hit enter.
    
    If you would like to get the status of all packages at a 
    particular time, type '2' and hit enter.
    
    If you would like to get the status of a single package at a 
    particular time, type '3' and hit enter.
        
    If you would like to view the status of our delivery trucks
    and total mileage, type '4' and hit enter. 
    
    Type 'q' and hit enter to quit.
    
    '''
        )
        # exits program
        if res == 'q':
            break

        # continues loop if option invalid
        elif res != '1' and res != '2' and res != '3' and res != '4':
            print("Please enter a valid input.")
            continue

        # see status of all packages
        elif res == '1':
            try:
                for i in range(len(package_list)):
                    p = hash_table.look_up(i + 1)
                    print(f"Package ID: {p.id}\n"
                          f"Truck ID: {p.truck_id}\n"
                          f"Deadline: {p.deadline}\n"
                          f"Delivered to: {p.address}, {p.city}, {p.state} {p.zip}\n"
                          f"Delivered at: {p.delivered_time}\n")

                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        elif res == '2':
            try:
                time = input(
                    '''
    Please enter the time at which you would like to check 
    the package status (format: HH:MM:SS).
    ''')
                (h, m, s) = time.split(":")
                time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                for i in range(len(package_list)):
                    p = hash_table.look_up(i + 1)
                    print(f"Package ID: {p.id}\n"
                          f"Address: {p.address}, {p.city}, {p.state} {p.zip}\n"
                          f"Current Time: {time}\n"
                          f"Status: {time_utility.determine_pkg_status(hash_table, time, i + 1)}\n")
                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        # see status of a single package
        elif res == '3':
            try:
                pkg_id = int(input(
                    '''
    Please enter the id number of the package as an integer 1-40.
    '''))
                time = input(
                    '''
    Please enter the time at which you would like to check 
    the package status (format: HH:MM:SS).
    ''')
                (h, m, s) = time.split(":")
                time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print(f"Status of package {pkg_id}: {time_utility.determine_pkg_status(hash_table, time, pkg_id)}")

                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        # check truck status and mileage
        else:
            print(f"Truck ID: {truck1.truck_id}\n"
                  f"Mileage: {truck1.miles}\n\n"
                  f"Truck ID: {truck2.truck_id}\n"
                  f"Mileage: {truck2.miles}\n\n"
                  f"Truck ID: {truck3.truck_id}\n"
                  f"Mileage: {truck3.miles}\n"
                  f"--------------------------------------------\n"
                  f"Total Miles Traveled: {truck1.miles + truck2.miles + truck3.miles}")
            if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                exit()


run_program()
