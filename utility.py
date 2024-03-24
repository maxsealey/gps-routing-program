# Takes in list created by csv reader and address, returns the index associated with
# said address. All address values are unique.
def get_address_index(file, address):
    for i in file:
        if i[2] != address:
            continue
        return i[0]

# Takes in number of miles and divides by the rate of speed. Returns float representing # of minutes
def convert_dist_to_time(miles):
    return float((miles/18)*60)
