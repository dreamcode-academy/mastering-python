'''
# super()
class Animal:
    def speak(self):
        return "This animal makes a sound"

class Dog(Animal):
    def speak(self):
        return super().speak() + " but specifically, a dog says woof"
    

new_animal = Animal()
print(new_animal.speak())

new_dog = Dog()
print(new_dog.speak())
'''
class Vehicle:
    def start_engine(self):
        return "Engine Starts"
    
    def stop_engine(self):
        return "Engine stops"


class ElectricCar(Vehicle):
     def start_engine(self):
        return "Electric motor starts silently"
     
     def stop_engine(self):
        return "Electric motor stops silently"


