from colorama import Fore, init
init(autoreset= True)

import math
num = int(input("enter the number to find SQRT : "))

def getSqrt25(num):
    result = math.sqrt(25)
    return result

print(f"Square root of {num} is : {Fore.CYAN}{getSqrt(num)}")