#Time

import time
def timer(func):
    def wrapper():
        start = time.time()
        result = func()

        end = time.time()

        print(f"{func.__name__} ran in: {end - start} sec")
        return result
    return wrapper

@timer
def data_processing():
    print("Processing data...")
    time.sleep(3)
    print("Data processing complete")

data_processing()