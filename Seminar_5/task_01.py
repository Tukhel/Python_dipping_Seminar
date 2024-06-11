# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

in_input = input('Enter 4 or more numbers separated by "/" :').split('/')
res_dict = dict()
res_dict[in_input[1]], res_dict[in_input[2]] = (in_input[0],
                                                tuple(in_input[3:]))
print(res_dict)

# Альтернативное решение
one, two, three, *other = input('Какой текст преобразовать? ').split('/')
result = {
    int(two): int(one),
    int(three): tuple(map(int, other)),
}
print(f'{result = }')
