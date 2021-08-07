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

#Prints true if School_bus is an instance of Vehicle
print(isinstance(School_bus, Vehicle))