#Using normal for loop
fruits = ["apple", "orange", "grapes"]
fruits_new = []
for fruit in fruits:
  if fruit != "orange":    
    fruits_new.append(fruit)
print(fruits_new)

# Using list comprehension
fruits_new2 = [ fruit for fruit in fruits if fruit != "orange"]
print(fruits_new2)

# Dictionary comprehension
prices = {"apple": 1.00, "banana": 0.50, "cherry": 2.50}

# Multiply each price by 0.90
discounted_prices = {item: round(price * 0.90, 2) for item, price in prices.items()}
print(discounted_prices)

# zip 
names = ["zubeir", "john", "David"]
scores = [92, 85, 90]
for name, score in zip(names, scores):
  print(f"{name} : {score}")

# map
prices = [10, 5, 40]
price_new = []
for price in prices:
  price += 2
  price_new.append(price)
print(price_new)
marked_up = list(map(lambda p: p + 2, prices))
print(marked_up)

# exit
while True:
  number = int(input("Enter a number : "))
  if number == 0:
    exit()
  print(number)
  choice = input("Do you want to try again ? (yes/no)")
  if choice in ['yes','y']:
    continue
  else:
    exit()
