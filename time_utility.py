import datetime


# Takes in number of miles and divides by the rate of speed. Returns float representing # of minutes
def convert_dist_to_mins(miles):
    return float((miles / 18) * 60)


# Takes in a number of minutes and converts to a time delta with hrs, mins, and secs
def convert_mins_to_hhmmss(mins):
    hh = int(mins // 60)
    mm = int(mins % 60)
    ss = int((mins % 1) * 60)

    return datetime.timedelta(hours=hh, minutes=mm, seconds=ss)


# Takes in the hash table, input time, and the id of the package to check the status of, returns string
def determine_pkg_status(hash_table, time_input, pkg_id):
    leave_time = hash_table.look_up(pkg_id).leave_time
    delivered_time = hash_table.look_up(pkg_id).delivered_time
    bod = datetime.timedelta(hours=8, minutes=0, seconds=0)
    eod = datetime.timedelta(hours=17, minutes=0, seconds=0)

    if time_input > eod or time_input < bod:
        return "out of bounds"
    elif time_input < leave_time:
        return "HUB"
    elif leave_time <= time_input < delivered_time:
        return "Out for Delivery"
    elif delivered_time >= time_input:
        return "Delivered"
    else:
        return "something went wrong"
