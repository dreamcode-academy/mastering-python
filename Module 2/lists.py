shopping_list = ['apple', 'orange', 'pear']

tasks = ['Learn Python', 'Build a project', 'Have fun']

numbers = [1, 2, 3, 4]


for i in shopping_list:
    print(i)

for x in tasks:
    print(x)




# Using braces to create a set
set_with_braces = {1, 2, 3}

# Using the set() constructor to create an empty set
empty_set = set()

# Add elements to the empty set
empty_set.add(10)
empty_set.add('eleven')

# Try to add a list to the set (which will raise an error)
# empty_set.add([12, 13])  # This would raise a TypeError

# Display the created sets
print("Set with braces:", set_with_braces)
print("Empty set:", empty_set)

