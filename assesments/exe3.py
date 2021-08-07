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

bus_1 = Bus("School Volvo", 180, 12)
print("Vehicle Name:", bus_1.name, 
      "Speed:", bus_1.max_speed,
      "Mileage:", bus_1.mileage) 
