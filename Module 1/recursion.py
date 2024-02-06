# Recursive functions

def add_numbers(n):
    if n == 0:
        # base case
        return 0
    else:
        # recursive procedure
        return n + add_numbers(n-1)
    
print(add_numbers(3))

"""
add_numbers(3) returns 3 + 3 = 6
add_numbers(2) returns 2 + 1
add_numbers(1) returns 1 + 0
add_numbers(0) returns 0
"""
