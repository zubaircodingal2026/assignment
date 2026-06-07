#bill calculator
def totalbill(billamount, tip):
    if tip == 0:
        tip = 2
    else:
        total_amount = billamount + (billamount*tip/100)
        total_amount = round(total_amount, 2)
        return total_amount
    
print("Welcome to bill calculator app...")
print("*"*30)

amount_rupees = float(input("\nEnter total amount : "))
            
tip = float(input("Enter the amount of tip you want to give"))
print(f"total payable amount : {totalbill(amount_rupees,tip)}")           
            