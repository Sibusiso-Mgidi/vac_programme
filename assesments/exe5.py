class Vehicle:
    """
    Stores a vehicle's details
    """
    def __init__(self, name, max_speed, mileage, color = "White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    """
    Stores a Bus' details
    Inherits from Vehicle class
    """
    pass

class Car(Vehicle):
    """
    Stores a Car's details
    Inherits from Vehicle class
    """
    pass

###############################################

def print_vehicle_details(vehicle):
    """
    Prints the vehicle datails to the terminal
    args:
        vehicle: a Vehicle class instance
    """
    print("Color:", vehicle.color,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
          "Vehicle Name:", vehicle.name, 
          "Speed:", vehicle.max_speed,
          "Mileage:", vehicle.mileage) 

###############################################                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

#2 Vehicle objects
bus_1 = Bus("School Volvo", 180, 12)
car_1 = Car("Audi Q5", 240, 18)

#print the 2 Vehicle objects' details
print_vehicle_details(bus_1)
print_vehicle_details(car_1)