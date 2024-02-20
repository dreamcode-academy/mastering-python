# lock, event, semaphore

import multiprocessing

import time

def worker(lock, event, semaphore, worker_id):
    event.wait()
    print(f"{worker_id} is waiting to access the resource")

    with semaphore:
        print(f"Worker {worker_id} has entered the semaphore")
        with lock:
            print(f"Worker {worker_id} is accessing the shared resource")
            time.sleep(1)
        print(f'Worker {worker_id} has finished accessing the shared resource')


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    event = multiprocessing.Event()
    semaphore = multiprocessing.Semaphore(2)

    workers = [multiprocessing.Process(target=worker, args=(lock, event, semaphore,i)) for i in range(4)]

    for w in workers:
        w.start()

    print("Main process is now sleeping for 3 seconds before setting the event")
    time.sleep(3)
    event.set()

    for w in workers:
        w.join()
