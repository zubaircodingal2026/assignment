
import numpy as np

print("===== Data Science Activity Using NumPy =====\n")


original_array = np.linspace(0, 9, 10, dtype=int)

print("1. Original Array:")
print(original_array)


modified_array = np.where(original_array % 2 == 1, -1, original_array)

print("\n2. Array after replacing odd numbers with -1:")
print(modified_array)

print("\nOriginal array remains unchanged:")
print(original_array)

array_2d = original_array.reshape(2, 5)

print("\n3. 2D Array (2 Rows):")
print(array_2d)


even_sum = 0

for number in original_array:
    if number % 2 == 0:
        even_sum += number

print("\n4. Sum of all even numbers:")
print(even_sum)