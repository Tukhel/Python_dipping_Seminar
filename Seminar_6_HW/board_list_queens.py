# Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается
# такая расстановка ферзей на шахматной доске, в которой ни один ферзь
# не бьет другого. Другими словами, ферзи размещены таким образом, что они не
# находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно
# печатать его не надо.
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve(board, row, solutions):
    if row == len(board):
        solutions.append([(i + 1, board[i] + 1) for i in range(len(board))])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, solutions)
            board[row] = -1


def generate_boards():
    board = [-1] * 8
    solutions = []
    solve(board, 0, solutions)

    valid_solutions = []
    for solution in solutions[:4]:
        valid_solutions.append(solution)

    return valid_solutions


print(generate_boards())
