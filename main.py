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

"""
load_packages()

Params: list of packages from csv file, hash table
Returns: N/A

Loops through the list of packages, assigns each attribute to a temporary
variable, creates a new Package object using that data, and inserts into the
hash table

Time Complexity: O(n)
"""


def load_packages(pkgs, table):
    # Loop through list
    for p in pkgs:
        # temp variables
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

        # Create new Package object and insert into the custom hash table
        pkg = Package.Package(id, address, city, state, zip, deadline, weight, notes)
        table.insert(id, pkg)


"""
run program()

Params: N/A
Returns: N/A

Core algorithm called to execute the program. Opens the csv files, creates the hash table,
loads the hash table with package data, creates and loads the truck, calls the function to deliver 
the packages, runs the CLI

Note to self: could be further modularized and aspects of the loading and
sorting process should be more automated

Time Complexity: Due to the 
"""


def run_program():
    # Open each of the csv files, extract lists of data and assign to variables
    with open('./csv_data/packages.csv') as pkg_data:
        package_list = list(csv.reader(pkg_data, delimiter=','))

    with open('./csv_data/addresses.csv') as addresses:
        address_list = list(csv.reader(addresses, delimiter=','))

    with open('./csv_data/distances.csv') as distances:
        distance_list = list(csv.reader(distances, delimiter=','))

    # Create the chaining hash table used to hold package data
    hash_table = HashTable.HashTable()

    # Load hash table with packages
    load_packages(package_list, hash_table)

    # Created truck objects
    truck1 = Truck.Truck(1, "HUB", datetime.timedelta(hours=8),
                         [1, 13, 14, 15, 16, 17, 19, 20, 21, 29, 30, 34, 37, 39, 40])
    truck2 = Truck.Truck(2, "HUB", datetime.timedelta(hours=9, minutes=5),
                         [3, 4, 5, 6, 18, 24, 25, 26, 31, 36, 38])
    truck3 = Truck.Truck(3, "HUB", datetime.timedelta(hours=10, minutes=30),
                         [2, 7, 8, 9, 10, 11, 12, 22, 23, 27, 28, 32, 33, 35])

    # Execute functions to deliver the packages for each truck
    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck1)
    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck2)
    dist_utility.deliver_packages(hash_table, distance_list, address_list, truck3)

    # Loops while user is operating the program
    while True:
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
        
    If you would like to view the mileage of our delivery trucks, 
    type '4' and hit enter. 
    
    Type 'q' and hit enter to quit.
    
    '''
        )
        # Exits program
        if res == 'q':
            break

        # Continues loop if input invalid, back to main menu
        elif res != '1' and res != '2' and res != '3' and res != '4':
            print("Please enter a valid input.")
            continue

        # See status of all packages; goes through all packages in the hash table; O(n^2)
        elif res == '1':
            try:
                for i in range(len(package_list)):
                    p = hash_table.look_up(i + 1)

                    print(f"Package ID: {p.id}\n"
                          f"Truck ID: {p.truck_id}\n"
                          f"Deadline: {p.deadline}\n"
                          f"Delivered to: {p.address}, {p.city}, {p.state} {p.zip}\n"
                          f"Delivered at: {p.delivered_time}\n")

                # Back to main menu or quit
                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        # View status of all packages at a certain time; O(n^2)
        elif res == '2':
            try:
                time = input(
                    '''
    Please enter the time at which you would like to check 
    the package status (format: HH:MM:SS).
    ''')
                (h, m, s) = time.split(":")
                time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        # Loop through and print data for each
                for i in range(len(package_list)):
                    p = hash_table.look_up(i + 1)

                    print(f"Package ID: {p.id}\n"
                          f"Address: {p.address}, {p.city}, {p.state} {p.zip}\n"
                          f"Current Time: {time}\n"
                          f"Status: {time_utility.determine_pkg_status(hash_table, time, i + 1)}\n")

        # Back to main menu or quit
                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        # See status of a single package at a certain time; O(n)
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

                print(f"Status of package {pkg_id}: {time_utility.determine_pkg_status(hash_table, time, pkg_id)}\n"
                      f"Delivery time: {hash_table.look_up(pkg_id).delivered_time}")

                # Back to main menu or quit
                if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                    exit()
            except ValueError:
                print("Please enter a valid input.")
                continue

        # View individual and total truck mileage
        else:
            print(f"Truck ID: {truck1.truck_id}\n"
                  f"Mileage: {truck1.miles}\n\n"
                  f"Truck ID: {truck2.truck_id}\n"
                  f"Mileage: {truck2.miles}\n\n"
                  f"Truck ID: {truck3.truck_id}\n"
                  f"Mileage: {truck3.miles}\n"
                  f"--------------------------------------------\n"
                  f"Total Miles Traveled: {round(truck1.miles + truck2.miles + truck3.miles, 2)}")

            # Back to main menu or quit
            if input("Press any key and 'enter' to continue or 'q' to quit: ") == 'q':
                exit()


run_program()
