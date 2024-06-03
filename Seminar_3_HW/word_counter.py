# В большой текстовой строке text подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Слова выведите в обратном алфавитном порядке.

import re

text = """I like digging holes and hiding things inside them
When I grow old, I hope I won't forget to find them"
'Cause I've got memories and travel like gypsies in the night
I build a home and wait for someone to tear it down
Then pack it up in boxes, head for the next town running
'Cause I've got memories and travel like gypsies in the night
And a thousand times I've seen this road
A thousand times
I've got no roots, but my home was never on the ground
I've got no roots, but my home was never on the ground"""

words = re.sub(r'[^\w\s]', ' ', text).lower().split()  # нашёл на просторах
# интернета. Ещё была конструкция с isalpha, но показалась более сложной

count_word = {}
for word in words:
    if word.isalpha():
        count_word[word] = count_word.get(word, 0) + 1

sorted_words = sorted(count_word.items(), key=lambda x: (x[1], x[0]),
                      reverse=True)[:10]

print(sorted_words)
