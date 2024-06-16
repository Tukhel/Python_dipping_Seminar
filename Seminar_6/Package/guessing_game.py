# Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

import random
from sys import argv


def guess_number(lower_limit: int, upper_limit: int, attempts: int) -> bool:
    hidden_num = random.randint(lower_limit, upper_limit)
    for item in range(1, attempts + 1):
        print(f'Attempt = {item}')
        user_num = int(input(f'Enter a number in range {lower_limit} -'
                             f' {upper_limit}: '))
        if user_num < hidden_num:
            print('Your number is less then the target number')
        elif user_num > hidden_num:
            print('Your number is greater then the target number')
        else:
            print('You win!')
            return True
    print('You exhausted all attempts')
    return False


# Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.


if __name__ == '__main__':
    print(argv)
    # guess_number(int(argv[1]), int(argv[2]), int(argv[3]))
    # guess_number(*(int(num) for num in argv[1:]))
    name, *param = argv
    print(param)
    guess_number(*(int(num) for num in param))
