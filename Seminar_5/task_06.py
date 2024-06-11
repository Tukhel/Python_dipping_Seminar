# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

START_NUM = 2
END_NUM = 10

# for i in range(START_NUM, END_NUM + 1):
#     for j in range(START_NUM, END_NUM):
#         print(f"{j} x {i :>2} = {j * i:>2}", end='\t\t')
#     print()


multiplication_table = (f'{j} x {i :>2} = {j * i:>2}\n'
                        for j in range(START_NUM, END_NUM)
                        for i in range(START_NUM, END_NUM + 1)
                        )
print(*multiplication_table)
