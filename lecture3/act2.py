amount = int(input("please enter amount withdrawn : "))

note_100 = amount //100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10

print(f"total {note_100} hundred rupees note , {note_50} fiftyrupees note and {note_10}  ten rupees notes")