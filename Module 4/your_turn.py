#Your task is to define a base class Animal and several subclasses such as Lion, Bird and Fish. 

class Animal:
    def move(self):
        return "This animal moves"
    
    def make_sound(self):
        return "This animal makes a sound"
    
class Fish(Animal):
    def move(self):
        return f"{super().move()} in the water"
    

new_fish = Fish()

print({new_fish.move()})