# Задание №3.
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


class Factorial:
    def __init__(self, *args):
        self.start = 1
        self.step = 1

        match len(args):
            case 1:
                self.stop = args[0]
            case 2:
                self.start, self.stop = args
            case 3:
                self.start, self.stop, self.step = args
            case _:
                raise ValueError('Too many parameters')

        # альтернативный вариант
        # match args:
        #     case (stop, ):
        #         self.stop = stop
        #     case (start, stop):
        #         self.start = start
        #         self.stop = stop
        #     case (start, stop, step):
        #         self.start = start
        #         self.stop = stop
        #         self.step = step
        #     case _:
        #         raise ValueError('Too many parameters')



    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            fact = 1
            for mult in range(2, self.start + 1):
                fact *= mult
            temp = self.start
            self.start += self.step
            return {temp: fact}
        raise StopIteration


if __name__ == '__main__':
    f1 = Factorial(1, 7, 2, 6)
    for item in f1:
        print(item)
