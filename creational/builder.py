"""
Separates object construction from its representation
Example: Multi course dinner
"""

class Vehicle(object):

    type = None
    wheels = None
    doors = None
    seats = None

    def view(self):
        print(
            "This vehicle is a " +
            self.type +
            " with; " +
            str(self.wheels) +
            " wheels, " +
            str(self.doors) +
            " doors, and " +
            str(self.seats) +
            " seats."
            )


class CarBuilder(Vehicle):

    def __init__(self):
        self.vehicle = Vehicle

    def set_type(self):
        self.vehicle.type = "Car"

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5


class BikeBuilder(Vehicle):

    def __init__(self):
        self.vehicle = Vehicle

    def set_type(self):
        self.vehicle.type = "Bike"

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2


class VehicleBuilder(object):
    def __init__(self, cls):
        self.cls = cls()
        self.cls.set_type()
        self.cls.make_wheels()
        self.cls.make_doors()
        self.cls.make_seats()
        self.cls.view()


if __name__ == "__main__":

    obj = VehicleBuilder(CarBuilder)
    obj = VehicleBuilder(BikeBuilder)
