#map(function, iterable)

#map(str, [1,2,3])

def raise_square(x):
    return x**2

numbers = [1,2,3,4,5]

squared_numbers = map(raise_square, numbers)

print(list(squared_numbers))