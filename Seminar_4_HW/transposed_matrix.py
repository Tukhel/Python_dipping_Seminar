# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в
# аргументы matrix, и возвращает транспонированную матрицу.

def transposed_matrix(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    return transposed


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
print(transposed_matrix(matrix = [[1,2], [3,4]]))
