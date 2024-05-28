# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

CMD_REPLENISH = 'R'
CMD_WITHDRAW = 'W'
CMD_EXIT = 'E'
MULTIPLICITY = 50
PERCENT_WITHDRAW = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_FEE = 30
MAX_FEE = 600
COUNT_OPERATION = 3
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
LUXURY_TAX = decimal.Decimal(10) / decimal.Decimal(100)
RICH_SUM = decimal.Decimal(5_000_000)

balance = decimal.Decimal(0)
transaction = 0

while True:
    cmd = input(f'Enter command:\n{CMD_REPLENISH} = replenish\n{CMD_WITHDRAW} = withdraw\n{CMD_EXIT} = exit\n')
    if cmd == CMD_EXIT:
        print(f'Balance: {balance}. Good luck.')
        break

    if balance > RICH_SUM:
        tax_amount = balance * LUXURY_TAX
        balance = balance - balance * LUXURY_TAX
        print(f'Let is subtract the wealth tax in the amount {tax_amount}. Balance: {balance}')

    if cmd in (CMD_REPLENISH, CMD_WITHDRAW):
        amount = decimal.Decimal(input(f'Enter amount multiple {MULTIPLICITY}: '))
        while amount % MULTIPLICITY:
            amount = decimal.Decimal(input(f'Wrong! Enter amount multiple {MULTIPLICITY}: '))

        if cmd == CMD_WITHDRAW:
            withdrawal_fee = amount * PERCENT_WITHDRAW
            withdrawal_fee = MIN_FEE if withdrawal_fee < MIN_FEE else \
                MAX_FEE if withdrawal_fee > MAX_FEE else withdrawal_fee
            withdrawal_amount = amount + withdrawal_fee
            if balance > withdrawal_amount:
                balance = balance - withdrawal_amount
                print(f'Transaction amount = {amount}, withdrawal commission = {withdrawal_fee}')
                print(f'Balance: {balance}')
                transaction += 1
            else:
                print(f'Insufficient funds. Balance = {balance}. Required amount = {withdrawal_amount}')
        elif cmd == CMD_REPLENISH:
            balance += amount
            print(f'Balance = {balance}')
            transaction += 1

        if transaction % COUNT_OPERATION == 0:
            bonus = balance * PERCENT_DEPOSIT
            print(f'You have performed three operation. Your bonus = {bonus}. Balance = {balance}')
