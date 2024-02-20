
class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Vehicle information: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model) # Super() call
        self.wheels = 4

    def display_info(self):
        print(f'Vehicle information: {self.make} {self.model}, Wheels: {self.wheels}')
        
my_car = Car('Tesla', 'Model S')
my_car.display_info()

"""

class BaseClass:
    def __init__(self):
        self.public_attribute = "Public Attribute"
        self._protected_attribute = "Protected Attribute"

class DerivedClass(BaseClass):
    def access_attributes(self):
        print("Accessing from DerivedClass:")
        print("Public:", self.public_attribute)
        print("Protected:", self._protected_attribute)

derived_obj = DerivedClass()
derived_obj.access_attributes()


 """