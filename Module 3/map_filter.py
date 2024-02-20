def greater_than_two(x):
    return x>2

def raise_square(x):
    return x**2

data = [1,2,3,4,5]
result = map(raise_square, filter(greater_than_two, data))

print(list(result))