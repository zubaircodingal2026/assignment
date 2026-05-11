store = []

while True:
    word = input("Enter word : ")
    print(word)
    if word =="":
        print("plase enter a valid word")
        continue
    elif word == "stop":
        break
    else:
        store.append(word)
        
for i in range(len(store)):
    print(store[i])