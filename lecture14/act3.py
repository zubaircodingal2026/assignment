# add number from 1 upto a limit
#using function recursion

def sum_nutral_number(n):
    if n <= 0:
        return 0
    return n + sum_nutral_number( n -1)

limit = int(input("Enter limit : "))

if limit <= 0:
    print("invalid input")
else:
    print(f"result : {sum_nutral_number(limit)}")
