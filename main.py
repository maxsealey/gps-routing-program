import csv

with open('./csv_data/addresses.csv') as addresses:
    address_reader = csv.reader(addresses, delimiter=',')
    for r in address_reader:
        print(r)


with open('./csv_data/distances.csv') as distances:
    distance_reader = csv.reader(distances, delimiter=',')
    for r in distance_reader:
        print(r)

with open('./csv_data/packages.csv') as packages:
    package_reader = csv.reader(packages, delimiter=',')
    for r in package_reader:
        print(r)