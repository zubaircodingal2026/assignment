from abc import ABC,abstractmethod
from typing import override

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# implement Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @override
    def calculate_area(self):
        return math.pi*(self.radius**2)

# implement Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    @override
    def calculate_area(self):
        return self.side**2

# implement Circle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @override
    def calculate_area(self):
        return 0.5*self.base*self.height

shapes_list = [Circle(5), Square(6), Triangle(6,8)]

for shape in shapes_list:
    area = shape.calculate_area()
    print(f"The area of {shape.__class__.__name__} : {area:.2f}")
    

