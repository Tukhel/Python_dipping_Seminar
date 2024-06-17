# Вы работаете над разработкой программы для проверки корректности даты,
# введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная
# дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна) или
# "False" (дата некорректна) в зависимости от результата проверки.


def _is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
            return True
    return False


date = input('Введите дату в формате DD.MM.YYYY:\n')

print(is_valid_date(date))
