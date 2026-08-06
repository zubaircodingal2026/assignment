import random
import string


length = int(input("Enter the password length: "))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits


password = [
    random.choice(lower),
    random.choice(upper),
    random.choice(numbers)
]


all_characters = lower + upper + numbers

for i in range(length - 3):
    password.append(random.choice(all_characters))


random.shuffle(password)


final_password = "".join(password)


print("Generated Password:", final_password)