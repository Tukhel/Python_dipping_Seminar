# Задание №6.
# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

import json
import random
from pathlib import Path
from functools import wraps


def number_of_starts(num: int):
    def deco(func):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                my_list.append(func(*args, **kwargs))
            return my_list

        return wrapper

    return deco


def number_control(func):
    min_number = 1
    max_number = 100
    min_attempts = 1
    max_attempts = 10

    @wraps(func)
    def wrapper(*args, **kwargs):
        guess, attempts = args[:2]
        rnd_num = guess if min_number <= guess <= max_number else (
            random.randint(min_number, max_number))
        rnd_attempts = attempts if min_attempts <= attempts <= max_attempts else (
            random.randint(min_attempts, max_attempts))
        return func(rnd_num, rnd_attempts)

    return wrapper


def deco_json(func):
    file_name = f'{func.__name__}.json'
    data = []
    if Path(file_name).is_file():
        with open(file_name, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        json_dict = {'result': res, 'args': args, **kwargs}
        data.append(json_dict)
        with open(file_name, 'w', encoding='utf-8') as f_w:
            json.dump(data, f_w, indent=4, ensure_ascii=False)

        return res

    return wrapper


@number_of_starts(3)
@number_control
@deco_json
def guessing_game(guess: int, attempts: int):
    for i in range(attempts):
        print(f'Попытка № {i + 1}')
        var = int(input('Угадай число от 1 до 100: '))
        if var == guess:
            return print('Вы угадали!')
    return print('Попытки закончились')


if __name__ == '__main__':
    print(f'{guessing_game.__name__ = }')
    #guessing_game(150, 500)
