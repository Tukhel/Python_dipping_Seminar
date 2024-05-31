# Задание №1
# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит уникальные
# (без повтора) элементы исходного списка.
#
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
print(list(set(data)))

my_list = []
for item in data:
    if item not in my_list:
        my_list.append(item)
print(my_list)

# my_list = []
# my_list = [item for item in data if item not in my_list]
# print(my_list)
# my_list = [item if item not in my_list else 0 for item in data]

my_set = {item for item in data}  # множество
my_dict = {item: item for item in data}  # словарь
my_gen = (item for item in data)  # генератор
