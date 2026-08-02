
# zip 
names = ["zubeir", "john", "rahim","karim","rifat"]
scores = [92, 85, 90,70,89]
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
