# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где
# ключ — имя (друга, а) значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная
# вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {
    'Ваня': ('спички', 'нож', 'парафин', 'веревка', 'рюкзак'),
    'Вася': ('карта', 'компас', 'топор', 'нож', 'рюкзак', 'уголь'),
    'Петя': ('навигатор', 'мангал', 'гитара', 'спички', 'палатка', 'нож',
             'топор'),
    'Лена': ('косметичка', 'мобтльный', 'планшет'),
}

# Все вещи
all_things = set()
for value in hike.values():
    all_things.update(value)

print(f'All things: {all_things}')

# Вещи есть только у одного друга
unique_things = set()
dict_unique_things = {}
for friend_master, things_master in hike.items():
    cur_set = set(things_master)
    for friend_slave, things_slave in hike.items():
        if friend_master != friend_slave:
            cur_set -= set(things_slave)
    unique_things.update(cur_set)
    dict_unique_things[friend_master] = cur_set
print(f'Unique things: {unique_things}')
print(dict_unique_things)

# Вещи есть у всех друзей кроме одного и имя того, у кого данная вещь
# отсутствует

duplicate_things = all_things - unique_things
print(f'Double: {duplicate_things}')
for friend, things in hike.items():
    print(f'Friend {friend} does not have {duplicate_things - set(things)}, '
          f'but others have')

