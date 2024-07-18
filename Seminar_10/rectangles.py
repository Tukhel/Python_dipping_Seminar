# Задание №2.
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a

    def square(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * (self.a + self.b)


if __name__ == '__main__':
    r1 = Rectangle(5)
    print(r1.square(), r1.perimetr())
