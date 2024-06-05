# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def my_func(lst_in: list[int | float], i_first: int,
            i_last: int) -> int | float:
    """
    :param lst_in:
    :param i_first:
    :param i_last:
    :return:
    """
    i_first, i_last = sorted([i_first, i_last])
    i_first = 0 if i_first < 0 else i_first
    i_last = len(lst_in) if i_last > len(lst_in) else i_last
    return sum(lst_in[i_first:i_last])


lst = [3, 4, 5, 2, 3, 1, 7, 9, 3]
print(my_func(lst, 6, 3))
