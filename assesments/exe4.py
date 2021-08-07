class Vehicle:
    """
    Stores a vehicle's mileage and max_speed
    """
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage 

    def seating_capacity(self, capacity):
        """
        args:
            capacity: the number of passengers the vehicle takes
        returns:
            a string stating what the vehicles name and its capacity
        """
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    """
    Stores a bus' details
    Inherits from Vehicle
    """

    def seating_capacity(self):
        """
        Overrides the seating capacity function of the super class
        returns:
            a string stating what the vehicles name and its capacity
        This assumes a default capacity of 50
        """
        return super().seating_capacity(50)
