# function keyword (return)
def oddEven(num):
    if num % 2==0:
        return True
    else:
        return False
    
num = int(input("Enter a whole number : "))
result = oddEven(num)

if result:
    print("The number is even")
else:
    print("The number is odd")