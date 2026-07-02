# Python program to calculate the product of all numbers in two tuples

# Creating the first tuple
tuple1 = (4, 3, 2, 2, -1, 18)

# Creating the second tuple
tuple2 = (2, 3, 8, 8, 3, 2, 9)

# Initializing the product variables
product1 = 1
product2 = 1

# Calculating the product of all elements in tuple1
for i in tuple1:
    product1 = product1 * i

# Calculating the product of all elements in tuple2
for j in tuple2:
    product2 = product2 * j

# Displaying the tuples
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Displaying the products
print("The product of all numbers in Tuple 1 is:", product1)
print("The product of all numbers in Tuple 2 is:", product2)