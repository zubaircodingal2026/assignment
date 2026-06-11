age = [10,20,30,40,50,60,70,80,90,100]

try:
    index = int(input("Enter age : "))
    print("value =",age[index])
except IndexError:
    print("error:age is out of range.")
except ValueError:
    print("Error:please enter a valid age.")
else:
    print("element accessed successfully.")