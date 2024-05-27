from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print(f'Угадай случайное сгенерированное число от {LOWER_LIMIT} до {UPPER_LIMIT} за {attempts} попыток')

for _ in range(attempts):
    user_position = input('Введите ваше предположение: ')
    if not user_position:
        print('Пожалуйста, введите число')
        continue
    position = int(user_position)

    if position < num:
        print('Загаданное число больше')
    elif position > num:
        print('Загаданное число меньше')
    else:
        print('Поздравляю! Вы угадали число.')
        break
else:
    print('У вас закончились попытки. Загаданное число было:', num)
