# Задание №4.
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def number_of_starts(num: int):
    def deco(func):
        my_list = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                my_list.append(func(*args, **kwargs))
            return my_list

        return wrapper

    return deco


@number_of_starts(3)
def print_text(text: str):
    return print(text)


if __name__ == '__main__':
    print_text('Hello world!')
