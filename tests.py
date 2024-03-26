import csv
import datetime
import dist_utility

from custom_classes import Package
from custom_classes import Truck
from custom_classes import HashTable

with open('./csv_data/packages.csv') as pkg_data:
    package_list = list(csv.reader(pkg_data, delimiter=','))

with open('./csv_data/addresses.csv') as addresses:
    address_list = list(csv.reader(addresses, delimiter=','))

with open('./csv_data/distances.csv') as distances:
    distance_list = list(csv.reader(distances, delimiter=','))

"""
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


# fill hash table with package data
hash_table = HashTable.HashTable()
load_packages(package_list, hash_table)

truck1 = Truck.Truck(1, "HUB", datetime.timedelta(hours=8),
                     [1, 2, 4, 6, 13, 14, 15, 16, 17, 19, 20, 21, 34, 39, 40])
truck2 = Truck.Truck(2, "HUB", datetime.timedelta(hours=9, minutes=5),
                     [3, 5, 18, 24, 25, 26, 29, 30, 31, 36, 37, 38])
truck3 = Truck.Truck(3, "HUB", datetime.timedelta(hours=10, minutes=30),
                     [7, 8, 9, 10, 11, 12, 22, 23, 27, 28, 32, 33, 35])

t1 = dist_utility.greedy_find_nearest(hash_table, distance_list, address_list, truck1, truck1.current_address)
t2 = dist_utility.greedy_find_nearest(hash_table, distance_list, address_list, truck2, truck2.current_address)
t3 = dist_utility.greedy_find_nearest(hash_table, distance_list, address_list, truck3, truck3.current_address)

for i in range(40):
    try:
        test = Truck.Truck(4, "HUB", datetime.timedelta(hours=8), [i + 1])
        t4 = dist_utility.greedy_find_nearest(hash_table, distance_list, address_list, test, hash_table.look_up(5).address)

        print(t4[0])
        print(t4[1])
        print(t4[2])
        print("\n")
    except:
        print("error")
        print(i + 1)
        print("\n")
"""

test_mins = 90
hms = ""
