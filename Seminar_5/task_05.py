# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.
# my_gen = (num for num in range(0, 101) if num % 3 == 0)

fizz_buzz = (
    'FizzBuzz' if num % 3 == num % 5 == 0
    else 'Fizz' if num % 3 == 0
    else 'Buzz' if num % 5 == 0
    else num for num in range(1, 101)
)
print(*fizz_buzz, sep=', ')

# fizz_buzz = []
# for num in range(1, 101):
#     if num % 3 == num % 5 == 0:
#         num = 'FizzBuzz'
#     elif num % 3 == 0:
#         num = 'Fizz'
#     elif num % 5 == 0:
#         num = 'Buzz'
#     fizz_buzz.append(num)
# print(fizz_buzz)
