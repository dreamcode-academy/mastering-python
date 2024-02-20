import threading
import time

# Shared resource and memory space
counter = 0
# Lock for synchronization
lock = threading.Lock()

def io_intensive_task():
    global counter
    # Simulating an I/O intensive task (CPU Usage characteristic)
    time.sleep(1)
    with lock:  # Synchronization to access the shared resource (Synchronization and Security)
        counter += 1  # Accessing shared memory space (Memory Space characteristic)

threads = []
for i in range(5):
    thread = threading.Thread(target=io_intensive_task)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Final Counter: {counter}")
