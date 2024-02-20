class SimpleContextManager:
    def __enter__(self):
        print("Resource is set up.")
        return "Hello from the context manager!"

    def __exit__(self, exc_type, exc_value, traceback):
        # Clean up the resource 
        print("Resource is cleaned up.")

# Using the custom context manager
with SimpleContextManager() as manager_resource:
    print(manager_resource)  

# After exiting the 'with' block, the __exit__method is automatically called

