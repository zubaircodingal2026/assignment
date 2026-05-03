limit = int(input("enter your limit : "))
start = 1
total = 0

for i in range (start, limit + 1):
    total = total + i
    
print(" sum upto {} : {}".format(limit,total))