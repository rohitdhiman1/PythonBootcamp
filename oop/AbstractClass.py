'''
Its a common design pattern programming where you want to provide a base class that defines a template
for other classes to inherit from, with couple of restrictions:
1. You dont want consumers of your base class to be able to create instances of base class,
because its intended to be just a blueprint. You want sub classes to provide a concrete implementations of that idea.
2. There are certain methods in the base class that sub classes have to consume/implement.
'''

from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

#s1 = Shape()
#Above line would throw an error since we cannot instantiate an abstract class

s1 = Square(4)
print(s1.calculate_area())

c1 = Circle(2)
print(c1.calculate_area())
