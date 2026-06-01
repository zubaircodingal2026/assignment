def printFullname(firstname,lastname,greet = "hello"):
        return f"{greet},my name is {firstname} {lastname}"
    
fname = input("Enter your first name : ")
lname = input("Enter your last name : ")

print("Welcome to function of python")
print("*"*30)

print(printFullname(fname,lname, "hi"))
print(printFullname(fname,lname,))
