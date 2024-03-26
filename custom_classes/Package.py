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
        self.status = "HUB"
        self.leave_time = 0
        self.delivered_time = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                       self.state, self.zip, self.deadline,
                                                       self.weight, self.status, self.notes, self.del_time)

    def update_package_status(self, new_status, new_time=0):
        self.status = new_status
        self.delivered_time = new_time
