#Declare class
class student:
    country = "bangladesh"
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    #custom method
    def displayDetails(self):
        return f"I am {self.name} and I am {self.age} years old"
    
    
#create object
s1 = student("Zubaer","14")
print(s1.displayDetails(),end=',')
print("I am from"+s1.country)
    