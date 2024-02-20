class Animal:
    def make_sound(self):
        print("Random sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animal_list = [Animal(), Dog(), Cat()]

for animal in animal_list:
    animal.make_sound()