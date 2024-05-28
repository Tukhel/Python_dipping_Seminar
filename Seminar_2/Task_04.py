# Задание №4
# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from math import pi
import decimal

decimal.getcontext().prec = 10
PI = decimal.Decimal(pi)

while (d := decimal.Decimal(input('Enter diameter: '))) > 1000:
    print('Enter a number less than 1000')

circle_len = PI * d
circle_square = (PI * pow(d, 2)) / 4

print(f'{circle_len = }', f'{circle_square = }', sep='\n')
