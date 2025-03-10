import numpy as np

matrix = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def pos(x, y, n):
    global matrix
    for i in range(9):
        if matrix[y][i] == n:
            return False
    for j in range(9):
        if matrix[j][x] == n:
            return False
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if matrix[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global matrix
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                for n in range(1, 10):
                    if pos(j, i, n):
                        matrix[i][j] = n
                        solve()
                        matrix[i][j] = 0
                return
    print(np.matrix(matrix))

solve()


