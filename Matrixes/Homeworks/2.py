from os import system

N = 15
M = 20

trees = [
    # ['дуб', 3, [int(),int()], 'д', 'Д'],
    # ['береза', 4, [int(), int()], 'б', 'Б'],
    # ['сосна', 5, [int(),int()], 'с', 'С']
]

round = 0
while True:
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

    # прорисовка обьектов
    # прорисовка деревьев
    while True:
        question = input('Ввести дерево (дуб, береза, сосна) или Enter: ')
        if question == 'дуб':
            trees.append(['дуб', 3, [int(input('Введите координаты i дуба: ')),
                                     int(input('Введите координаты j дуба: '))],
                          'д', 'Д'])
            break
        elif question == 'береза':
            trees.append(['береза', 4, [int(input('Введите координаты i березы: ')),
                                        int(input('Введите координаты j березы: '))],
                          'б', 'Б'])
            break
        elif question == 'сосна':
            trees.append(['сосна', 5, [int(input('Введите координаты i сосны: ')),
                                       int(input('Введите координаты j сосны: '))],
                          'с', 'С'])
            break
        else:
            break
    for tree in trees:
        tree_coords = tree[2]
        tree_sprite = tree[3]
        matrix[tree_coords[0]][tree_coords[1]] = tree_sprite

    # очистка экрана
    system('cls')

    # вывод матрицы на экран
    for row in matrix:
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        print(row_text[:-1] + '|')

    # инвентарь
    print('Инвентерь: ', end='')
    for tree in trees:
        print(tree[0], '-', tree[1], end=' ')
    print()

    # действие

    # рост деревьев
    for tree in trees:
        if tree[0] == 'дуб':
            if round % 3 == 0:
                tree[3] = 'Д'
        else:
            pass

    round += 1
