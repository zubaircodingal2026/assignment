# prime number chack
num = int(input("Enter a number to chack : "))

if num <= 1 :
    print("please enter a valid number")
else:
    is_prime = True
    for i in range(2,num):
        if num % i ==0:
            is_prime = False
            break
    if is_prime:
        print("it is a prime number")
    else:  
        print("it is not a prime number")
