""" file modes: 
 r to read
 w to write
 a to append
 r+ to write and read"""
#open()
#file = open('example.txt', 'w')
#file.write("Hello World!")
#file.close()

#read()
"""file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()"""

#write()
with open('example.txt', 'w') as file:

    file.write("Adding a new line")

file = open('example.txt', 'a')
file.write("\nAdding a second line")
#close()