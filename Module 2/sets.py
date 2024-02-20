# Using braces to create a set
set_with_braces = {1, 2, 3}

# Using the set() constructor to create an empty set
tasks = set()

tasks.add("Write the script for a lesson")
tasks.add("Record video for a lesson")

completed_tasks = {"Check budget", "Write the script for a lesson"}

#print(tasks.difference(completed_tasks))
#print(tasks.union(completed_tasks))
#print(tasks.intersection(completed_tasks))
print(tasks)
tasks.remove("Write the script for a lesson")
print(tasks)
