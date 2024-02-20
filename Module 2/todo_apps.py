import json

print("To-do list application")
my_todo_list = []

# Save tasks

def save_tasks_to_file():
    try:
        with open("tasks.json", "w") as file:
            json.dump(my_todo_list, file) # from list to json
    except Exception as e:
         print(f"Error saving tasks: {e}")

# load tasks

def load_tasks_from_file():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("Error reading the tasks file. File might be corrupted.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

# Add new task

def add_task(description, duration):
    task = {"description": description, "duration": duration}
    my_todo_list.append(task)

# remove a task

def remove_task(task_id):
    if task_id >= 0 and task_id < len(my_todo_list):
        removed_task = my_todo_list.pop(task_id)
    else:
        print("Task not found")

# list all tasks

def list_tasks():
    print("Current tasks")
    for i, task in enumerate(my_todo_list):
        print(f"{i}: description: {task["description"]}, duration: {task["duration"]}")


# main

my_todo_list = load_tasks_from_file()
while True:
    print("1. List taks")
    print("2. Add task")
    print("3. Remove task")
    print("4. exit")

    choice = input("Choose an option: ")
    if choice == "1":
        list_tasks()
    elif choice == "2":
        description = input("Enter the task description: ")
        duration = input("Enter the task duration: ")
        add_task(description, duration)
    elif choice == "3":
        try:
            task_id = int(input("Enter the task id to be removed: "))
            remove_task(task_id)
        except ValueError:
            print("Please enter a valid number.") 
    elif choice == "4":
        save_tasks_to_file()
        break
    else:
        print("Invalid option, please try again")
