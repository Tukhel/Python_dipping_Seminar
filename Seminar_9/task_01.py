# Задание №1.
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from typing import Callable


def guessing_game(guess: int, attempts: int) -> Callable:
    def wrapper():
        # nonlocal  attempts
        # nonlocal guess
        # while attempts > 0:
        #     attempts -= 1
        #     var = int(input('Угадай число от 1 до 100: '))
        #     if var == guess:
        #         return print('Вы угадали!')
        # return print('Попытки закончились')
        for i in range(attempts):
            print(f'Попытка № {i + 1}')
            var = int(input('Угадай число от 1 до 100: '))
            if var == guess:
                return print('Вы угадали!')
        return print('Попытки закончились')
    return wrapper


game_1 = guessing_game(10, 5)
if __name__ == '__main__':
    game_1()
