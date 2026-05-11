#Sum of n natural numbers
num = int(input("Enter the value of terms : "))
sum = 0
i = 1

while i<= num:
    sum += i
    i +=1
    
print(f"sum upto {num} : {sum}")