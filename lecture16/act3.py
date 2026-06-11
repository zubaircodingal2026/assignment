number = [10,20,30]

try:
    index = int(input("Enter index : "))
    print("value =",number[index])
except IndexError:
    print("error:index is out of range.")
except ValueError:
    print("Error:please enter a valid integer.")
else:
    print("element accessed successfully.")