class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, status, leave_time, del_time, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.leave_time = leave_time
        self.del_time = del_time
        self.notes = notes
        self.truck_id = 0

    def __str__(self):
        return f'ID: {self.id}'

# loads package to the truck
    def set_truck_id(self, id):
        self.truck_id = id