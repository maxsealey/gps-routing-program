# Takes in list created by csv reader and address, returns the index associated with
# said address. All address values are unique.
def get_address_index(address_list, address):
    if address == "HUB":
        return int(0)

    for i in address_list:
        if i[2] != address:
            continue
        return int(i[0])


# Takes in number of miles and divides by the rate of speed. Returns float representing # of minutes
def convert_dist_to_mins(miles):
    return float((miles / 18) * 60)

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

    for p in truck.pkg_load:
        hash_table.look_up(p).update_package_status("Out for delivery")

    while len(truck.pkg_load) != 0:
        new_location = find_next_nearest(hash_table, distance_list, address_list, truck, truck.current_address)
        total_miles += new_location[2]
        for i in new_location[0]:
            truck.pkg_load.remove(i)
            hash_table.look_up(i).update_package_status("Delivered", convert_dist_to_mins(total_miles))
        # print(truck.pkg_load)
        truck.set_address(new_location[1])

    total_miles += distance_between(distance_list,address_list,truck.current_address,"HUB")
    truck.current_address = "HUB"
    truck.set_miles(total_miles)


