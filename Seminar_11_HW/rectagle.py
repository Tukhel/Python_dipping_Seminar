class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

# Пример использования:
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")
