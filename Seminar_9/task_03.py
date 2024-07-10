# Задание №3.
# Напишите декоратор, который сохраняет в json файл параметры декорируемой
# функции и возвращаемый ей результат.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from pathlib import Path


def deco_json(func):
    file_name = f'{func.__name__}.json'
    data = []
    if Path(file_name).is_file():
        with open(file_name, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        json_dict = {'result': res, 'args': args, **kwargs}
        data.append(json_dict)
        with open(file_name, 'w', encoding='utf-8') as f_w:
            json.dump(data, f_w, indent=4, ensure_ascii=False)

        return res

    return wrapper


@deco_json
def sum_numbers(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    sum_numbers(10, 2, 3, 4, x=2)
    sum_numbers(10, 9999, 2, c='Hello', x=2)
