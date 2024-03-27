"""
Contains the utility functions used to execute distance-related operations, including deliver_packages()
"""
import datetime
import time_utility

"""
get_address_index()

Params: list of addresses, address to search for
Returns: the id of that address

The time complexity of this function is O(n) as it
searches through the input addresses list, where n is the number
of addresses.
"""


def get_address_index(address_list, address):
    # Using "HUB" instead of the hub's address makes sense for readability
    if address == "HUB":
        return int(0)

    # loops through list
    for i in address_list:
        if i[2] != address:
            continue
        return int(i[0])


"""
distance_between()

Params: list of distances, list of addresses, address 1, address 2
Returns: the distance between the two addresses

The time complexity of this function is O(n), since it calls
get_address_index()
"""


def distance_between(distance_list, address_list, x, y):
    x_index = get_address_index(address_list, x)
    y_index = get_address_index(address_list, y)

    # reads in the array element at set locations
    first_try = distance_list[x_index][y_index]
    second_try = distance_list[y_index][x_index]

    # returns whichever variable has the actual distance
    if first_try != '':
        return float(first_try)
    else:
        return float(second_try)


"""
find_next_nearest()

Params: hash table of packages, list of distances, list of addresses,
truck object, address of starting point.
Returns: A list with three elements: [0] a list of the packages on
the truck to be delivered at the next nearest address, [1] the address of
the nearest/next neighbor, [2] the distance

Time Complexity: O(n^2)

"""


def find_next_nearest(table, distance_list, address_list, truck, start_address):
    shortest_dist = 1000.0
    next_pkgs = []
    shortest_dist_address = ""

    # loops through each package on the truck, which is a maximum of 16 and decreases each time
    # function is called by deliver_packages()
    for pkg in truck.pkg_load:
        # get address from hash table and use that compare with previous/starting address
        y_address = table.look_up(pkg).address
        d_b = distance_between(distance_list, address_list, start_address, y_address)

        # finds the nearest neighbor to the truck's current location and updates temp variables accordingly
        if shortest_dist > d_b:
            # clear array of packages that are no longer at the nearest location
            next_pkgs.clear()
            shortest_dist = float(d_b)
            next_pkgs.append(pkg)
            shortest_dist_address = y_address

        # prevents packages with the same distance away but different addresses from being grouped together
        elif shortest_dist == d_b and table.look_up(pkg).address == shortest_dist_address:
            next_pkgs.append(pkg)

    # [0] a list of the packages on the truck to be delivered at the next nearest address,
    # [1] the address of the nearest/next neighbor, [2] the distance from the current location
    return [next_pkgs, shortest_dist_address, shortest_dist]


"""
deliver_packages()

Params: table, distance list, address list, truck
Returns: N/A

Updates package if address is wrong. Updates package info with departure time and truck id.
While truck still has packages to be delivered, gets nearest location, increments, and removes
the package at that location.

Time Complexity: O(n^3)
"""


def deliver_packages(hash_table, distance_list, address_list, truck):
    # keeps track of the # of miles traveled for the whole route
    total_miles = 0

    # updates the address for the package with the incorrect address
    if 9 in truck.pkg_load and truck.leave_time >= datetime.timedelta(hours=10, minutes=20):
        hash_table.look_up(9).update_address("410 S State St", "Salt Lake City", "UT", "84111")

    # sets the attributes of each package with the truck id and the time of departure
    for p in truck.pkg_load:
        hash_table.look_up(p).package_ofd(truck.leave_time)
        hash_table.look_up(p).set_truck_id(truck.truck_id)

    # iterates until all packages have been delivered
    while len(truck.pkg_load) != 0:
        # get address, list of packages at that location, and the distance away of the nearest location
        new_location = find_next_nearest(hash_table, distance_list, address_list, truck, truck.current_address)
        # increments miles by the distance
        total_miles += new_location[2]
        # convert distance to travel time (timedelta form), and add to leave_time
        hms = truck.leave_time + time_utility.convert_miles_to_timedelta(total_miles)

        # remove the packages and update delivery time
        for i in new_location[0]:
            truck.pkg_load.remove(i)
            hash_table.look_up(i).package_delivered(hms)

        # truck travels to next location
        truck.set_address(new_location[1])

    # After all packages delivered, send truck back to hub and set the total mileage
    total_miles += distance_between(distance_list, address_list, truck.current_address, "HUB")
    truck.current_address = "HUB"
    truck.set_miles(total_miles)
