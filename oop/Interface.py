'''
Interfaces are useful for declaraing a class that has a capability that it knows
how to provide.
'''

from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class JSONify(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def toJson(self):
        pass

class Circle(Shape,JSONify):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def toJson(self):
        return "{\"" + "circle\":" + str(self.calculate_area())  + "}"


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


s1 = Circle(4)
print(s1.calculate_area())
print(s1.toJson())