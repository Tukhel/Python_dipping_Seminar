# Задание №1.
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
from collections import deque


class Factorial:
    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, num):
        if num < 0:
            raise ValueError('Не может быть отрицательного значения')
        else:
            result = 1
            for i in range(2, num + 1):
                result *= i
            self.memory.append({num: result})

        return result

    def get_memory(self):
        return self.memory


if __name__ == '__main__':
    f1 = Factorial(3)
    f1(3)
    f1(5)
    f1(6)
    f1(7)
    f1(2)
    print(f1.get_memory())
