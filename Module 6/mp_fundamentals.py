import multiprocessing

def compute_square(number):
    result = number * number
    print(f"Square of {number} is {result}")

def compute_task(data):
    print(f"Processing {data}")

if __name__ == "__main__":
    data = "Example"
    process = multiprocessing.Process(target = compute_task, args =(data,))
    process.start()
    process.join()
    
    '''
    number = 4
    square_process = multiprocessing.Process(target = compute_square, args = (number, ))
    square_process.start()
    square_process.join()
    '''

