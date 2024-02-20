from collections import Counter
import random

large_items_list = [random.choice(['apple', 'banana', 'orange', 'grape', 'melon']) for _ in range(100000)]
items_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def calculate_frequencies_optimized(items):
    return Counter(items)

#print(calculate_frequencies_optimized(items_list))