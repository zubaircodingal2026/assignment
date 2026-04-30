medical_cause = input("enter your medical cause(yes/no)").strip().upper()

if medical_cause =="yes":
    print("you are allowed to sit for exam")
else:
    attendance = int(input("Enter attendance : "))
    
if attendance > 75:
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam")