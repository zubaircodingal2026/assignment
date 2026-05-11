medical_cause = input("did YOU HAVE A MEDICAL CAUSE? (yes/no) ").strip().upper()

if medical_cause == 'yes':
    print("you are allowed")
else:
    
    atten = int(input("enter the attendance of the student: "))
    
    if atten >= 75:
        print("ALLOWED")
    else:
        print("NOT ALLOWED")