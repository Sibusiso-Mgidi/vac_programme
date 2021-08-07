class Vehicle:
    """
    Stores a vehicle's details
    """
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    """
    Stores a bus' details
    Inherits from the Vehicle class
    """
    pass

School_bus = Bus("School Volvo", 12, 50)
#Print the class that School_bus belongs to
print(type(School_bus))