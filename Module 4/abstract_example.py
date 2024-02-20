# Game Character

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def move(self):
        pass

    def attack(self):
        pass

class Warrior(GameCharacter):
    def move(self):
        return "Moves by marching"
    
    def attack(self):
        return "Attack with sword"
    
class Archer(GameCharacter):
    def move(self):
        return "Moves by running"
    
    def attack(self):
        return "Attack with a bow"


blue_archer = Archer()
print(blue_archer.attack())

red_warrior = Warrior()
print(red_warrior.move()) 