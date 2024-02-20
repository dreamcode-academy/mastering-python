class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is starting.")

    def get_vehicle_info(self):
        return f"{self.make} {self.model}"

my_vehicle = Vehicle("Toyota", "Corolla")
#my_vehicle.start_engine()

print(my_vehicle.get_vehicle_info())
my_new_vehicle = Vehicle("Honda", "Civic")
print(f"My new vehicle is: {my_new_vehicle.get_vehicle_info()}")