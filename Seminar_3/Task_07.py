# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение —
# частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

my_text = input("Enter you text: ").lower()
my_dict = {}
new_text = my_text.replace(" ", "")

for letter in new_text:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)
# print(*my_dict.items(), sep='\n') # Вывод вертикально

# через count
my_dict = {key: new_text.count(key) for key in set(new_text)}
print(my_dict)
