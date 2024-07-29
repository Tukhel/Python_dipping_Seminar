class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = []
        for row in self.data:
            result.append(" ".join(map(str, row)))
        return "\n".join(result)

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return self.data == other.data

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                "Matrices must have the same dimensions to be added.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must equal number of rows in the second matrix.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


# Пример использования
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)
print(matrix2)

# Показать сложение матриц
matrix3 = matrix1 + matrix2
print("Сумма матриц:")
print(matrix3)

# Показать классику умножения
matrix4 = Matrix(3, 2)
matrix4.data = [[1, 2], [3, 4], [5, 6]]
matrix5 = matrix1 * matrix4
print("Произведение матриц:")
print(matrix5)