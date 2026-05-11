num = input("Enter a number : ")

if len(num) >= 4:
    mid1 = int(num[len(num)//2 - 1])
    mid2 = int(num[len(num)//2])
    
    print("product =", mid1 * mid2)
else:
    print ("Enter a 4 or more digit number")