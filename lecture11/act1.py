#Character occurance
string = input("enter your word : ")
char = input("please enter your own character : ")

i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count  + 1
    i = i+1
    
print(f"{char} has appeared {count} times in '{string}")