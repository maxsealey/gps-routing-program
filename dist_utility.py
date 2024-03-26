# Takes in list created by csv reader and address, returns the index associated with
# said address. All address values are unique.
import datetime
import time_utility

"""
get_address_index()

Params: list of addresses, address to search for
Returns: the id of that address

The time complexity of this function is O(n), as it
searches through the list of address
"""
def get_address_index(address_list, address):
    if address == "HUB":
        return int(0)

    for i in address_list:
        if i[2] != address:
            continue
        return int(i[0])


# Takes in two lists and two addresses. Compares list values
def distance_between(distance_list, address_list, x, y):
    x_index = get_address_index(address_list, x)
    y_index = get_address_index(address_list, y)

    first_try = distance_list[x_index][y_index]
    second_try = distance_list[y_index][x_index]

    if first_try != '':
        return float(first_try)
    else:
        return float(second_try)


# Greedy Algo: returns queue of pkg ids at next address, next address
def find_next_nearest(table, distance_list, address_list, truck, start_address):
    shortest_dist = 1000.0
    next_pkgs = []
    temp = truck.pkg_load.copy()
    shortest_dist_address = ""
    same_as_curr_loc = False

    while len(temp) != 0:
        for pkg in temp:
            y_address = table.look_up(pkg).address
            d_b = distance_between(distance_list, address_list, start_address, y_address)

            if d_b == 0.0 and same_as_curr_loc == False:
                next_pkgs.clear()
                shortest_dist = 0.0
                next_pkgs.append(pkg)
                shortest_dist_address = start_address
                same_as_curr_loc = True
                temp.remove(pkg)
                continue
            elif d_b == 0.0 and same_as_curr_loc == True:
                next_pkgs.append(pkg)
                temp.remove(pkg)
                continue
            elif d_b != 0.0 and same_as_curr_loc == True:
                temp.remove(pkg)
                continue

            if shortest_dist > d_b:
                next_pkgs.clear()
                shortest_dist = float(d_b)
                next_pkgs.append(pkg)
                shortest_dist_address = y_address
            elif shortest_dist == d_b and table.look_up(pkg).address == shortest_dist_address:
                next_pkgs.append(pkg)
            temp.remove(pkg)

    return [next_pkgs, shortest_dist_address, shortest_dist]


def deliver_packages(hash_table, distance_list, address_list, truck):
    total_miles = 0
    if 9 in truck.pkg_load and truck.leave_time >= datetime.timedelta(hours=10, minutes=20):
        hash_table.look_up(9).update_address("410 S State St", "Salt Lake City", "UT", "84111")

    for p in truck.pkg_load:
        hash_table.look_up(p).package_ofd(truck.leave_time)

    while len(truck.pkg_load) != 0:
        new_location = find_next_nearest(hash_table, distance_list, address_list, truck, truck.current_address)
        total_miles += new_location[2]
        for i in new_location[0]:
            minutes = time_utility.convert_dist_to_mins(total_miles)
            hms = truck.leave_time + time_utility.convert_mins_to_hhmmss(minutes)
            truck.pkg_load.remove(i)
            hash_table.look_up(i).package_delivered(hms)
        truck.set_address(new_location[1])

    total_miles += distance_between(distance_list, address_list, truck.current_address, "HUB")
    truck.current_address = "HUB"
    truck.set_miles(total_miles)
    t = time_utility.convert_dist_to_mins(total_miles)
    t1 = time_utility.convert_mins_to_hhmmss(t)
    print(truck.leave_time + t1)
