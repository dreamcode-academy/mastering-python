# decorator
'''
def register(func):
    def wrapper(*args, **kwargs):
        print('Before execution')
        print(f"Positional arguments: {args}")
        print(f"Named arguments: {kwargs}")
        result = func(*args, **kwargs)
        print('After execution')
        return result
    return wrapper

@register
def greet(name, age=None):
    greeting_str = f"Hello, {name}"
    if age:
        greeting_str += f", you are {age} years old"

    print(greeting_str)

greet("Alice", age=25)

'''

class Vehicle:
    def __init__(self, *args, **kwargs):
        print("Vehicle initialized with args: ", args)
        print("Vehicle initialized with kwargs: ", kwargs)

    
class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Car initialized with additional parameters: ",args, kwargs )
car = Car("Model X", color = "Blue", year=2020)      