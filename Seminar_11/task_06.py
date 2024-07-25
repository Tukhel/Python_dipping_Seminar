# Задание №6.
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        length = perimeter / 2 - width
        return Rectangle(length, width)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        length = perimeter / 2 - width
        return Rectangle(length, width)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()


if __name__ == '__main__':
    r1 = Rectangle(25, 5)
    r2 = Rectangle(10, 9)
    new_r = r1 - r2
    print(new_r.perimeter(), new_r.length, new_r.width)
    print(r1.square(), r2.square())
    print(r1 == r2)
    print(r1 != r2)
    print(r1 <= r2)
    print(r1 >= r2)
    print(r1 < r2)
    print(r1 > r2)
