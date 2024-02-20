def number_generator(maximum):
    number = 1
    while number <= maximum:
        yield number
        number += 1

# Creating the generator
gen = number_generator(1000000)

# Using the generator to get numbers one at a time
for number in gen:
    # Process each number (here we'll only print some for demonstration)
    if number <= 10:  # Print only the first 10 for demonstration
        print(number)
