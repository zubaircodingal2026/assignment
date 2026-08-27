from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):
    @abstractmethod
    #this method need to be implementend in its sub class
    #compulsory
    def move(self):
        pass
    
    #normal method not abstract
    def test(self):
        x = 5
        y = 10
        z = z + y
        print(z)
class snake(Animal):
    @override
    def move (self):
        print("snake crawl")
class horse(Animal):
    @override
    def move (self):
        print("horse kick back")        


class bird(Animal):
    @override
    def move(self):
        print("Bird fly")
        
        
        
# --- object creation in a for loop ---
#1.put the classes themselve into a list
animal_classes = (snake,horse,bird)

#2. loop throug through the class,instantiate them and call move()
for animal_class in animal_classes:
    animal_object = animal_class()
    #create the object(e.g.,snake(),horse())
    animal_object.move()        