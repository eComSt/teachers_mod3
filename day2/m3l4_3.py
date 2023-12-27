from figure import Figure
from math import pi
class Rectangle(Figure):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width
    
    def get_perimeter(self):
        return 2 * (self._length + self._width)

# abcd = Rectangle(5, 10)
# print(abcd.get_rectangle_area())

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3
    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p - self._side1) * (p - self._side2) * (p - self._side3)) ** 0.5

class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius
    def get_area(self):
        return pi * self._radius * self._radius
    def get_perimeter(self):
        return 2 * pi * self._radius

c = Circle(5)
print(c.get_area(), c.get_perimeter())