import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    @staticmethod
    def find_sides(req):
        for width in range(int(math.sqrt(req)), 0, -1):
            if req % width == 0:
                height = req // width
                return width, height
        return req, 1

    def __add__(self, other):
        new_req = self.get_square() + other.get_square()
        width, height = Rectangle.find_sides(new_req)
        return Rectangle(width, height)

    def __mul__(self, n):
        new_req = self.get_square() * n
        width, height = Rectangle.find_sides(new_req)
        return Rectangle(width, height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'