#create class
class IOString:
    #contructor to set default value
    def __init__(self):
        self.strl = ""
        
    #function to get input from the user
    def Get_String(self):
        self.strl = input("Enter string :")
        
    # function to print the string in upper case
    def print_string(self):
        print("result is :",self.strl.upper())
        
        
#object creation
strl = IOString()

#call functions
strl.Get_String()
strl.print_string()