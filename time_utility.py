"""
Contains the utility functions used to execute time-related operations and conversions
"""

import datetime

"""
convert_miles_to_timedelta()

Params: number of miles traveled over 
Returns: timedelta of that # of minutes in hh:mm:ss form

Converts miles to minutes traveled at 18 mph, then convert to timedelta form

Called in dist_utility.deliver_packages()

"""


def convert_miles_to_timedelta(miles):
    minutes = float((miles / 18) * 60)

    hh = int(minutes // 60)
    mm = int(minutes % 60)
    ss = int((minutes % 1) * 60)

    return datetime.timedelta(hours=hh, minutes=mm, seconds=ss)


"""
determine_pkg_status()

Params: hash table, time input by user, and package id to check
Returns: the status of the package at that time

Checks status of a package at a particular timr

Called in the CLI section of main.run_program()

"""


def determine_pkg_status(hash_table, time_input, pkg_id):
    # gets the time that package left hub and the time it was delivered
    leave_time = hash_table.look_up(pkg_id).leave_time
    delivered_time = hash_table.look_up(pkg_id).delivered_time

    # time representing start of the day and the end; used to verify input
    # time is within the bounds of the work day
    bod = datetime.timedelta(hours=8, minutes=0, seconds=0)
    eod = datetime.timedelta(hours=17, minutes=0, seconds=0)
    p = hash_table.look_up(pkg_id)

    if pkg_id == 9 and time_input < datetime.timedelta(hours=10, minutes=20):
        p.update_address("300 State St", "Salt Lake City", "UT", "84103")
    elif pkg_id == 9 and time_input >= datetime.timedelta(hours=10, minutes=20):
        p.update_address("410 S State St", "Salt Lake City", "UT", "84111")

    # returns 'out of bounds' if time is not within scope of workday
    if time_input > eod or time_input < bod:
        return "out of bounds"
    # returns 'HUB' if package has not left facility
    elif time_input < leave_time:
        hash_table.look_up(pkg_id).set_status("HUB")
        return "HUB"
    # if package has left facility and not been delivered, return 'Out for delivery'
    elif leave_time <= time_input < delivered_time:
        hash_table.look_up(pkg_id).set_status("Out for Delivery")
        return "Out for Delivery"
    # if delivered time is equal to or before input, return 'Delivered'
    elif delivered_time <= time_input:
        hash_table.look_up(pkg_id).set_status("Delivered")
        return "Delivered"
    # error catch-all, should never be reached
    else:
        return "something went wrong"


"""
get_status_time()

Params: status, time
Returns: string containing either the current or delivered time

Checks status of a package at a particular time

Called in the CLI section of main.run_program()

"""


def get_status_time(status, time, del_time):
    if status == "HUB" or status == "Out for Delivery":
        return f"Current time: {time} || Expected Delivery Time: {del_time}\n"
    elif status == "Delivered":
        return f"Current time: {time} || Delivered at: {del_time}\n"
    else:
        return False
