class Vehicle(object):
    """
    Blueprint for storing a vehicle's mileage and max_speed
    """
    def __init__(self, max_speed, mileage):
        """
        initializes Vehicle object with the given max_speed and mileage
        """
        self.max_speed = max_speed
        self.mileage = mileage
    