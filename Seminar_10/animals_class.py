# Задание №6.
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.
class Animal:
    def __init__(self, type_name, age):
        self.type_name = type_name
        self.age = age


class Fish(Animal):
    def __init__(self, type_name, age, max_deep):
        super().__init__(type_name, age)
        self.max_deep = max_deep

    def get_max_deep(self):
        if self.max_deep <= 10:
            return 'Мелководная рыба'
        elif 10 < self.max_deep < 100:
            return 'Средневодная рыба'
        else:
            return 'Глубоководная рыба'


class Bird(Animal):
    def __init__(self, type_name, age, wingspan):
        super().__init__(type_name, age)
        self.wingspan = wingspan

    def get_wing(self):
        return f'Размах крыла = {self.wingspan / 2}'


class Mammal(Animal):
    def __init__(self, type_name, age, weight):
        super().__init__(type_name, age)
        self.weight = weight

    def get_size(self):
        if self.weight < 50:
            return 'Мелкий зверь'
        else:
            return 'Крупный зверь'


if __name__ == '__main__':
    f1 = Fish('fish', 2, 10)
    print(f1.type_name, f1.age, f1.max_deep, f1.get_max_deep())

    b1 = Bird('bird', 5, 100)
    print(b1.type_name, b1.age, b1.wingspan, b1.get_wing())

    m1 = Mammal('mammal', '10', 100)
    print(m1.type_name, m1.age, m1.weight, m1.get_size())
