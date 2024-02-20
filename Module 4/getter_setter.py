'''

#Getter
class MyClass:
    def __init__(self,value):
        self.__private_attribute = value
    
    @property
    def private_attribute(self):
        return self.__private_attribute
    #Setter
    @private_attribute.setter
    def private_attribute(self, new_value):
        if new_value > 0:
            self.__private_attribute = new_value
        else:
            print("The value must be positive")    
    
obj = MyClass(10)
obj.private_attribute =- 5
print(obj.private_attribute)

'''


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:

            print("Age cannot be negative")


person = Person("John",30)


person.name = "Anna"
person.age = -4
print(person.name)
print(person.age)


