# Задание №1.
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_num():
    while True:
        num = input('Введите число: ')
        try:
            res = int(num)
            break
        except ValueError as e:
            try:
                res = float(num)
                break
            except ValueError as e:
                print(f'{e}. Должно быть целое или вещественное число, вы '
                      f'ввели {type(num)}')
    print(num)


if __name__ == '__main__':
    get_num()
