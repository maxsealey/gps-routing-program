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
        self.del_time = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                       self.state, self.zip, self.deadline,
                                                       self.weight, self.status, self.notes, self.del_time)

    # updates status upon delivery or delay (hub, out for delivery, delayed, delivered)
    def set_status(self, new_status):
        self.status = new_status

    # updates time package leaves hub
    def set_leave(self, new_leave_time):
        self.leave_time = new_leave_time

    # updates when package delivered with current time
    def set_del_time(self, new_del_time):
        self.del_time = new_del_time
