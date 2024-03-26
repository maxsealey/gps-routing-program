class Truck:
    def __init__(self, truck_id, current_address, leave_time, pkg_load):
        self.truck_id = truck_id
        self.current_address = current_address
        self.leave_time = leave_time
        self.pkg_load = pkg_load

        self.miles = 0

        # constants
        self.max_capacity = 16
        self.avg_spd = 18

    def __str__(self):
        return "%s, %s, %s, %s" % (self.truck_id, self.current_address,
                                           self.leave_time, self.miles)

    # sets new address upon arrival
    def set_address(self, new_address):
        self.current_address = new_address

    # update mileage
    def set_miles(self, new_miles):
        self.miles = new_miles

