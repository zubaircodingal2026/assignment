# take input from user
rowsize = int(input("Enter thr number of rows : "))
if rowsize % 2== 0:  # conditions
    HalfDiamRow = int(rowsize / 2)
else:
    HalfDiamRow = int(rowsize / 2) +1
space = HalfDiamRow - 1
#looop for upper part
for i in range(1, HalfDiamRow + 1): #loop for rows
    for j in range(1,space +1 ): #loop for columns
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        