# Takes in list created by csv reader and address, returns the index associated with
# said address. All address values are unique.
def get_address_index(address_list, address):
    if address == "HUB":
        return 0

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
def greedy_find_nearest(table, distance_list, address_list, truck, start_address):
    shortest_dist = 1000.0
    next_pkgs = []
    temp = truck.pkg_load.copy()
    shortest_dist_address = ""

    while len(temp) != 0:
        for pkg in temp:
            y_address = table.look_up(pkg).address
            d_b = distance_between(distance_list, address_list, start_address, y_address)

            if shortest_dist > d_b:
                next_pkgs.clear()
                shortest_dist = float(d_b)
                next_pkgs.append(pkg)
                shortest_dist_address = y_address
            elif shortest_dist == d_b:
                if table.look_up(pkg).address == shortest_dist_address:
                    next_pkgs.append(pkg)

            temp.remove(pkg)

    return [next_pkgs, shortest_dist_address, shortest_dist]
