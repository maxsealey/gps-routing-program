# Name: Max Sealey || Student ID: 010332991

import csv
import custom_classes.Package
import custom_classes.Truck
import custom_classes.HashTable

with open('./csv_data/addresses.csv') as addresses:
    address_reader = csv.reader(addresses, delimiter=',')

with open('./csv_data/distances.csv') as distances:
    distance_reader = csv.reader(distances, delimiter=',')

with open('./csv_data/packages.csv') as packages:
    package_reader = csv.reader(packages, delimiter=',')

hash_table = custom_classes.HashTable()


def load_packages(file, table):
    for p in file:
        id = p[0]
        address = p[1]
        city = p[2]
        state = p[3]
        zip = p[4]
        deadline = p[5]
        weight = p[6]
        notes = p[7]

    pkg = custom_classes.Package(id, address, city, state, zip, deadline, weight, notes)
    table.insert(pkg)

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
    If you would like to view the delivery status of all packages,
    type '1' and hit enter.
    
    If you would like to get the status of a single package at a 
    particular time, type '2' and hit enter.
        
    If you would like to view the status of our delivery trucks, 
    type '3' and hit enter. 
    
    Type 'q' and hit enter to quit.
    
    '''
    )
        # exits program
        if res == 'q':
            break

        # continues loop if option invalid
        elif res != '1' and res != '2' and res != '3':
            print("Please enter a valid input.")
            continue

        # see status of all packages
        elif int(res) == 1:
            valid_input = 1

        # see status of a single package
        elif int(res) == 2:
            time = input(
    '''
    Please enter the time that you would like to see the
    delivery status of each package in the format, HH:MM:SS
    ''')
            print(time)
            valid_input = 1

        # check truck status and mileage
        else:
            valid_input = 1

run_program()