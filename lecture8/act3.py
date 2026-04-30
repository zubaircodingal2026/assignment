print("Select your ride : ")
print("1. Car")
print("2. Bike")

choice1 = int(input("Enter your choice : "))
if choice1 == 1:
    print("What type of car do you want?")
    print("1. Sedan")
    print("2. SUV")
    choice2 = int(input("Enter your choice : "))
    if choice2 == 1:
        print("You selected a Sedan")
    elif choice2 == 2:
        print("You selected an SUV")
    else:
        print("Invalid choice")

elif choice1 == 2:
    print("What type of bike do you want?")
    print("1. Scooty")
    print("2. Road Bike")
    choice2 = int(input("Enter your choice : "))
    if choice2 == 1:
        print("You selected a Scooty")
    elif choice2 == 2:
        print("You selected a Road Bike")
    else:
        print("Invalid choice")

else:
    print("Invalid choice")
