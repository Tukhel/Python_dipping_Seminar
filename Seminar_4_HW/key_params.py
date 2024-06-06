# Напишите функцию key_params, принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ - значение переданного аргумента,
# а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            my_dict[value] = key
        except TypeError:
            string_key = str(value)
            my_dict[string_key] = key
    return my_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
