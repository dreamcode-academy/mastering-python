import numpy as np


# Example array for normalization
array_for_normalization = np.array([10, 20, 30, 40, 50])

'''

'''
normalized_array = (array_for_normalization - np.min(array_for_normalization)) / (np.max(array_for_normalization) - np.min(array_for_normalization))

print("Normalized array: ", normalized_array)

fahrenheit_array = np.array([32, 212, 122])

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

celsius_temperatures = fahrenheit_to_celsius(fahrenheit_array)

print("Celsius Temperatures: ", celsius_temperatures)