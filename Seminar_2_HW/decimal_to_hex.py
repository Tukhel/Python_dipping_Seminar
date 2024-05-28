# Напишите программу, которая получает целое число num
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX = 16

num: int = int(input('Enter you number: '))
hex_chars = '0123456789ABCDEF'
result: str = ''
decimal_to_hex = hex(num)

while num > 0:
    remainder = num % HEX
    result = hex_chars[remainder] + result
    num //= HEX

print(f'Шестнадцатеричное представление числа: {result}')
print(f'Проверка результата: {decimal_to_hex}')
