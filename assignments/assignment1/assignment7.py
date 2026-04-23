char_input = input("enter a character : ")

if len(char_input) == 1:
    
    print(f"ASCII value of {char_input} is {ord(char_input)}")
else:
    print("please enter a singal character.")    