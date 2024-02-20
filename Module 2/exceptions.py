"""try:
    # Code that might throw an exception
except ExceptionType:
    # Code that runs if the exception occurs
    
try:
    # Operations that can generate multiple exceptions
except FileNotFoundError:
    # Handle the file not found error
except PermissionError:
    # Handle the permission error
filnally:


try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist") 

with open("example.txt", "r") as input_file:
    while True:
        try:
            data = input_file.readline()
            if not data:
                break
            print(data)
        except EOFError:
            break"""

class CustomError(Exception):
    """A custom exception for our applicatio"""
    pass

try:
    raise CustomError('An error occurred')
except CustomError as e:
    print(f'An error was caught: {e}')
