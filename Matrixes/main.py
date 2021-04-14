# создать матрицу  N x M

N = 50
M = 50

# создание матрицы
matrix = []
i = 0
while i < N:
    row = []
    j = 0
    while j < M:
        row.append('-')
        j += 1

    matrix.append(row)
    i += 1


# вывод матрицы на экран
for row in matrix:
    row_text = '|'
    for el in row:
        row_text += str(el) + ' '
    print(row_text[:-1] + '|')

