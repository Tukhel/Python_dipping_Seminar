# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def my_func():
    glob = globals()
    dict_new = {}
    for key, value in glob.items():
        if key.endswith('s') and key != 's':
            dict_new[key[:-1]] = value
            glob[key] = None
    glob.update(dict_new)


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

print(globals())
my_func()
print(globals())
