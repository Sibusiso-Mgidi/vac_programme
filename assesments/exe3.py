class Vehicle():
    """
    Blueprint for storing a vehicle's mileage and max_speed
    """
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    """
    Blueprint for storing a Bus' details
    Bus inherits from vehicle
    """
    pass
