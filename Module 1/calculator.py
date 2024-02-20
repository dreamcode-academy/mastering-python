# Function definitions
def addition(x, y): 
    return x + y 

def subtraction(x, y): 
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: You cannot divide by zero"
 

def modulo(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: You cannot divide by zero"

# Main program
print("Mastering Python Calculator")

stop = False

while stop == False:
    try:
        option = int(input("""
            1. addition
            2. subtraction
            3. multiplication
            4. division
            5. modulo
            6. exit
            Choose an option: """))
    

        if option == 6:
            print("See you soon!")
            stop = True
            continue
        elif option not in range(1, 7):
            print("Invalid operation")
            continue

        
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        
        
        if option == 1:
            print("Addition: ", addition(x,y))
        elif option == 2:
            print("Subtraction:", subtraction(x,y))
        elif option == 3:
            print("Multiplication:", multiplication(x,y))
        elif option == 4:
            print("Division:", division(x,y))
        else:
            print("Modulo:", modulo(x,y))

    except ValueError:
        print("Error: Enter a valid number")
        continue
    
    