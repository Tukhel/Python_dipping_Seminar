# Задание №2.
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_dict(new_dict, key, default=None):
    try:
        if not isinstance(new_dict, dict):
            raise TypeError
    except TypeError:
        return 'Это не словарь'
    try:
        return new_dict[key]
    except KeyError as e:
        return default


if __name__ == '__main__':
    my_dict = {'1': 1, '2': 2, '3': 3}
    num = 23
    print(get_dict(num, '1'))
    print(get_dict(my_dict, '1'))
    print(get_dict(my_dict, '4', 4))
    print(get_dict(my_dict, 5))
