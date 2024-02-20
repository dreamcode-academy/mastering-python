# Login

def log_function_execution(func):
    def wrapper():
        print(f"Function {func.__name__} started.")
        result = func()
        print(f"Function {func.__name__} finished.")
        return result
    return wrapper

@log_function_execution
def example_function():
    print("Executing the original function.")

example_function()


#Time 
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def example_function():
    # Simulate some time-consuming operation
    time.sleep(2)
    print("Executing the original function.")

example_function()


#Acess control

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Simulating a user authentication system
authenticated_user = User(username="john_doe", role="admin")

# Decorator for access control
def access_control(required_role):
    def decorator(func):
        def wrapper(user):
            if user.role == required_role:
                print(f"Access granted for {user.username}. Executing {func.__name__}.")
                result = func()
            else:
                print(f"Access denied for {user.username}. Insufficient privileges.")
                result = None
            return result
        return wrapper
    return decorator

# Applying access control to functions
@access_control(required_role="admin")
def admin_function():
    return "Admin function executed."

@access_control(required_role="user")
def user_function():
    return "User function executed."

# Attempting to execute functions with different user roles
admin_result = admin_function(authenticated_user)
user_result = user_function(authenticated_user)

print(admin_result)
print(user_result)