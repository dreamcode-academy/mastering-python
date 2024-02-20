import tkinter as tk
import threading
import time

def perform_long_task():
    time.sleep(5)
    print("Task completed")

def start_long_task():
    thread = threading.Thread(target = perform_long_task)
    thread.start()

def perform_another_task():
    time.sleep(2)
    print("Another task completed")

def start_another_task():
    thread = threading.Thread(target=perform_another_task)
    thread.start()


root = tk.Tk()
root.title("Multithreading in GUI demonstration")

start_button = tk.Button(root, text ="Start Long Task", command = start_long_task)
start_button.pack(pady=10)

start_button = tk.Button(root, text ="Start Another Task", command = start_another_task)
start_button.pack(pady=10)
root.mainloop()