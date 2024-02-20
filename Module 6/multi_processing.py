import multiprocessing
import time
'''

def cpu_intensive_task(result, i):
    # Simulating a CPU intensive task
    time.sleep(1)
    result.put(i * i)  # Using a queue for inter-process communication

if __name__ == "__main__":
    # List to store processes
    processes = []
    # Queue for inter-process communication
    result = multiprocessing.Queue()

    for i in range(5):
        process = multiprocessing.Process(target=cpu_intensive_task, args=(result, i))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    # Retrieving results
    while not result.empty():
        print(result.get())
'''


