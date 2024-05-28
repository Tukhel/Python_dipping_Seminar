# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

import fractions

frac1: str = input('Enter first fraction: ').split('/')
frac2: str = input('Enter second fraction: ').split('/')

frac1_num = int(frac1[0])
frac1_den = int(frac1[1])
f1 = fractions.Fraction(frac1_num, frac1_den)

frac2_num = int(frac2[0])
frac2_den = int(frac2[1])
f2 = fractions.Fraction(frac2_num, frac2_den)

sum_num = frac1_num * frac2_den + frac2_num * frac1_den
sum_dem = frac1_den * frac2_den

prod_num = frac1_num * frac2_num
prod_dem = frac1_den * frac2_den

print(f'Сумма дробей: {sum_num}/{sum_dem}')
print(f'Произведение дробей: {prod_num}/{prod_dem}')
print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
