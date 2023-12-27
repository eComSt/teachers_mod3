class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width
    
    def get_perimeter(self):
        return 2 * (self._length + self._width)

# abcd = Rectangle(5, 10)
# print(abcd.get_rectangle_area())

class Triangle():
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3
    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p - self._side1) * (p - self._side2) * (p - self._side3)) ** 0.5

# abc = Triangle(5, 10)
# print(abc.get_triangle_area())
a = Rectangle(5, 10)
b = Triangle(5, 7, 4)
c = Rectangle(25, 1)
d = Triangle(4, 10, 8)
fig = [a, b, c, d]
for i in fig:
    print(i.get_area(), i.get_perimeter())