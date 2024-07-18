# Задание №1.
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:
    def __init__(self, radius=10):
        self.radius = radius

    def square(self):
        return pi * (self.radius ** 2)

    def length(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    c1 = Circle(5)
    print(c1.square(), c1.length())
