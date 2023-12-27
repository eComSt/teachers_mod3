class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width

# abcd = Rectangle(5, 10)
# print(abcd.get_rectangle_area())

class Triangle():
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def get_area(self):
        return 0.5 * self._base * self._height

# abc = Triangle(5, 10)
# print(abc.get_triangle_area())
a = Rectangle(5, 10)
b = Triangle(5, 7)
c = Rectangle(25, 1)
d = Triangle(2, 10)
fig = [a, b, c, d]
for i in fig:
    print(i.get_area())