class Vehicle:
    """
    Stores a vehicle's details and defines its methods
    """
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        """
        Returns the fare charges to customers who rent the car
        """
        return self.capacity * 100

class Bus(Vehicle): 
    """
    Stores a bus's details and defines its methods
    """
    def fare(self):
        """
        Returns the fare that is charged to customers renting the bus
        This charge also includes the a maintainence fee 
        This method overrides the parent class' fare method
        """
        return super().fare() * 1.1


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())