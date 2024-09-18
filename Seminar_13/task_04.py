# Задание №4.
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
from pathlib import Path


class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name = } {self.user_id = } {self.level = }'

    def __repr__(self):
        return f'User({self.name}, {self.user_id}, {self.level})'


def load_json(path):
    with open(path, 'r', encoding='utf-8') as fr:
        data = json.load(fr)

    users = set()
    for level, users_dict in data.items():
        for user_id, name in users_dict.items():
            users.add(User(name, user_id, level))

    return users


if __name__ == '__main__':
    res = load_json('users.json')
    print(res)
    for user in res:
        print(user)
