# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_duplicates = []

for item in lst:
    if lst.count(item) > 1 and item not in unique_duplicates:
        unique_duplicates.append(item)
print(unique_duplicates)
