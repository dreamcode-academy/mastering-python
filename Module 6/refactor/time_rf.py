
import timeit
original_time = timeit.timeit('calculate_frequencies(items_list)', 
                              setup='from frequencies import calculate_frecuencies, items_list', number=10000)

optimized_time = timeit.timeit('calculate_frequencies_optimized(items_list)', 
                              setup='from refactored_code import calculate_frecuencies_optimized, items_list', number=10000)

print(f"Original: {original_time}")
print(f"Opitmized: {optimized_time}")