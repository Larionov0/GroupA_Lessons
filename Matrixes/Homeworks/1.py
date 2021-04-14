matrix = [
    [9, 1, 3, 5],
    [2, 6, 7, 11],
    [0, 3, 7, 4]
    ]

i = int(input())

j = 0
while j < len(matrix[0]):
    matrix[i][j] = (float('inf'))
    j += 1
#
# print(matrix)

for row in matrix:  #вывод матрицы на экран
    for el in row:
        print(el, end = ' ')
    print()