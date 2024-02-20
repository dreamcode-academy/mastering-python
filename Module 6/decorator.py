


def simple_logger(func):
    def wrapper():
        print("Function is about to run!")
        func()
        print("Function has finished running")
    return wrapper

def debug_info(func):
    def wrapper():
        print(f"Running {func.__name__} ")
        return func()
    return wrapper

'''
@debug_info
def add(a,b):
    return a+b

result = add(5,3)
print(f"Result: {result}")

'''
@debug_info
@simple_logger
def greet():
    print("Hello")


greet()
