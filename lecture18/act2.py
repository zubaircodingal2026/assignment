print("Welcome to word search game...")
word_list = []

def displayItem():
    print("\nyour entered words are...")
    print("*"*20)
    for item in word_list:
        print(f"{item}")
        
while True:
    word = input("enter a word : ")
    word_list.append(word)
    choise = input("do you want to add again ? (yes/no)")
    if choise not in ["yes","y"]:
        displayItem()
        exit()
    else:
        continue
print("All words.....")
displayItem()
      