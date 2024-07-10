# Задание №2.
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from typing import Callable
import random


def number_control(func: Callable) -> Callable:
    min_number = 1
    max_number = 100
    min_attempts = 1
    max_attempts = 10

    def wrapper(*args, **kwargs):
        guess, attempts = args[:2]
        rnd_num = guess if min_number <= guess <= max_number else (
            random.randint(min_number, max_number))
        rnd_attempts = attempts if min_attempts <= attempts <= max_attempts else (
            random.randint(min_attempts, max_attempts))
        return func(rnd_num, rnd_attempts)

    return wrapper


@number_control
def guessing_game(guess: int, attempts: int):
    for i in range(attempts):
        print(f'Попытка № {i + 1}')
        var = int(input('Угадай число от 1 до 100: '))
        if var == guess:
            return print('Вы угадали!')
    return print('Попытки закончились')


if __name__ == '__main__':
    game_1 = guessing_game(10, 5)
