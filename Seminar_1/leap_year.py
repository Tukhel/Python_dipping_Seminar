REFORM = 1582
BIG_LEAP_YEAR = 400
LARGE_NON_LEAP_YEAR = 100
SMALL_LEAP_YEAR = 4
MULTIPLE = 0

year = int(input('Enter your year: '))

if year < REFORM:
    result = 'The input year not Grigorian yet'
elif year % BIG_LEAP_YEAR == MULTIPLE:
    result = f'{year} is a leap year'
elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
    result = f'{year} is not a leap year'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    result = f'{year} is a leap year'
else:
    result = f'{year} is not a leap year'

print(result)
