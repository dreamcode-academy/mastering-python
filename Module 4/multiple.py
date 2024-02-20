
class Car:
    def __init__(self, car_make, car_model):
        self.car_make = car_make
        self.car_model = car_model
    
    def drive(self):
        print(f"Driving a car:{self.car_make} {self.car_model}")

    
class Boat:
    def __init__(self, boat_type):
        self.boat_type = boat_type
    
    def sail(self):
        print(f"Sailing a boat: {self.boat_type}")

class AmphibiousVehicle(Car, Boat):
    def __init__(self, car_make, car_model, boat_type):
        Car.__init__(self, car_make, car_model, boat_type)
        Boat.__init__(self, boat_type)

amphibious_vehicle = AmphibiousVehicle('AwesomeVehicle', 'Model A', 'Speedboat')
amphibious_vehicle.drive()
amphibious_vehicle.sail()



