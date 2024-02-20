def factorial(n):
    result = 1
    for i in range(1, n+1):
        print(f"Iteration: {i}, current result: {result}")
        result *= i
    
    return result

print(factorial(4))

# factorial -> 4! = 4 *3 *2 * 1 = 24