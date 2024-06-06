from decimal import Decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = Decimal('15') / Decimal('1000')
MIN_REMOVAL = Decimal('30')
MAX_REMOVAL = Decimal('600')
PERCENT_DEPOSIT = Decimal('3') / Decimal('100')
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = Decimal('10') / Decimal('100')
RICHNESS_SUM = Decimal('10_000_000')

bank_account = Decimal('0')
count = 0
operations = []


def check_multiplicity(amount):
    """Проверка кратности суммы."""
    if amount % MULTIPLICITY != 0:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False
    return True


def deposit(amount):
    """Пополнение счёта."""
    global bank_account, count, operations
    if check_multiplicity(amount):
        if count > COUNTER4PERCENTAGES:
            amount += Decimal(amount) * PERCENT_DEPOSIT
            count += 1
        bank_account += Decimal(amount)
        operations.append(
            f"Пополнение счета на {amount} у.е. Итого {bank_account} у.е.")


def withdraw(amount):
    """Снятие средств."""
    global bank_account, operations
    check_multiplicity(amount)
    commission: Decimal = min(MAX_REMOVAL, max(MIN_REMOVAL, amount *
                                               PERCENT_REMOVAL))
    amount_commission: Decimal = Decimal(amount) + Decimal(commission)

    if amount_commission > bank_account:
        operations.append(
            f"Недостаточно средств. Сумма с комиссией {amount_commission} у.е. На карте {bank_account} у.е.")
    else:
        bank_account -= Decimal(amount) + commission
        operations.append(
            f"Снятие с карты {amount} у.е. Процент за снятие {commission} у.е.. Итого {bank_account} у.е.")


def exit():
    """Завершение работы."""
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        tax = Decimal(bank_account * RICHNESS_PERCENT)
        bank_account -= tax
        operations.append(f"Вычтен налог на богатство {RICHNESS_PERCENT}% в "
                          f"сумме {tax} у.е. Итого {bank_account} у.е.")
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")


deposit(10000)
withdraw(4000)
exit()

print(operations)
