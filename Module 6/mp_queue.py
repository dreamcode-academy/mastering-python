#QUEUE
import multiprocessing

def worker(queue):
    data = queue.get()
    print(f"Retreived: {data}")

if __name__=="__main__":
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target = worker, args = (queue, ))
    p.start()
    queue.put("Hello from main")
    queue.put("New message")
    queue.put("Hello")
    p.join()