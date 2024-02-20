import timeit

def loop_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        return total
    
loop_sum(range(100))

