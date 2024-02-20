import timeit
import random

large_items_list = [random.choice(['apple', 'banana', 'orange', 'grape', 'melon']) for _ in range(100000)]

def calculate_frequencies(items):
    frecuencies = {}
    for item in items:
        if item in frecuencies:
            frecuencies[item] += 1
        else:
            frecuencies[item] = 1
    return frecuencies

items_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

#print(calculate_frequencies(items_list))

original_time = timeit.timeit('calculate_frequencies(large_items_list)', 
                              setup='from frequencies import calculate_frequencies, large_items_list', number=10000)

optimized_time = timeit.timeit('calculate_frequencies_optimized(large_items_list)', 
                              setup='from refactored_code import calculate_frequencies_optimized, large_items_list', number=10000)

print(f"Original: {original_time}")
print(f"Opitmized: {optimized_time}")