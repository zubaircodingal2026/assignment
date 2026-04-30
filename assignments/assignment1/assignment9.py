age = input("enter your age(yes/no)").strip().upper()

if age =="yes":
    print("you are allowed to sit in the class ")
else:
    your_age = int(input("Enter your age : "))
    
if your_age > 20:
    print("you are not allowed to sit in class")
else:
    print("you are allowed to sit in the class")