#parental class 
class ParentClass:
    #constructor
    def __init__(self, name,age, country):
        self.name = name
        self.age = age
        self.country = country
        
        #custom method
    def displayDetails(self):
        return f"{self.name} | {self.age} | {self.country}"

        
p1 = ParentClass("john",20,"china")
print(p1.displayDetails())

#inheritance derived class
class DerivedClass(ParentClass):
    def __init__(self, name,age, country,city):
        ParentClass.__init__(self,name,age,country)
        self.city = city
        
    def displayDetails(self):
        return f"{ParentClass.displayDetails(self)}, and {self.city}"

    
d1 = DerivedClass("devid",21,"USA","Dallas")
print(d1.displayDetails())