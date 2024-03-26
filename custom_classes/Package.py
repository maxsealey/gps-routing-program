import datetime


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.leave_time = datetime.timedelta(hours=0, minutes=0, seconds=0)
        self.delivered_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                           self.state, self.zip, self.deadline,
                                                           self.weight, self.notes, self.leave_time,
                                                           self.delivered_time)

    def update_address(self, new_address, new_city, new_state, new_zip):
        self.address = new_address
        self.city = new_city
        self.state = new_state
        self.zip = new_zip

    def package_ofd(self, time):
        self.leave_time = time

    def package_delivered(self, time):
        self.delivered_time = time
