# Задание №1
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def print_words(text_in):
    words = sorted(text_in.split())
    # max_len = max(len(word) for word in words)
    max_len = len(max(words, key=len))

    for i, word in enumerate(words, 1):
        # space = ' ' * (max_len - len(word) + 1)
        # print(f'{i}.{space}{word}')
        # print(f'{i:<3} {word:>{max_len}}')
        print(str(i).ljust(3), word.rjust(max_len))


text = input('Enter you text:\n')
print_words(text)
