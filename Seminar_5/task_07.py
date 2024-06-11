# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def generate_primes(num):
    start = 2
    count = 0
    while count < num:
        is_prime = True
        for i in range(2, int(start ** 0.5 + 1)):
            if start % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            yield start
        start += 1


n = 10
print(*generate_primes(n))
