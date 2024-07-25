# Задание №1.
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

# Добавьте к задачам 1 и 2 строки документации для классов.

import datetime


class MyString(str):
    def __new__(cls, text, author):
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = datetime.datetime.now()
        print(text, instance.author, instance.time)
        return instance


if __name__ == '__main__':
    a = MyString('Hello', 'Andrey')
