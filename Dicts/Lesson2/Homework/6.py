from os import system

N = 15
M = 20

total_oak_trees = 3
total_birches = 5
total_pine_trees = 2

trees = []

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
        print('\nОсталось деревьев: ', 'дуб -', total_oak_trees, 'береза -',  # Меню - количество деревьев
              total_birches, 'сосна -', total_pine_trees)

        question = input('Посадить дерево (дуб, береза, сосна) или Enter: ')  # Посадка деревьев
        if question == 'дуб' or question == 'береза' or question == 'сосна':
            i = input('Введите координаты i для посадки дерева: ')
            j = input('Введите координаты j для посадки дерева: ')
            print()

            try:  # Проверка input на int
                test_i = int(i)
                tes_j = int(j)

                if question == 'дуб' and total_oak_trees > 0:
                    trees.append(['дуб', 3, [int(i), int(j)], 'д', 'Д', 0])  # посадка дуба
                    total_oak_trees -= 1
                    break
                elif question == 'береза' and total_birches > 0:
                    trees.append(['береза', 4, [int(i), int(j)], 'б', 'Б', 0])  # посадка березы
                    total_birches -= 1
                    break
                elif question == 'сосна' and total_pine_trees > 0:
                    trees.append(['сосна', 5, [int(i), int(j)], 'с', 'С', 0])  # посадка сосны
                    total_pine_trees -= 1
                    break
                else:
                    input('Попробуй что-то другое!')
                    break
            except:
                break
        else:
            break

    for tree in trees:  # визуализация деревьев
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
    print('На поле: ', end='')
    for tree in trees:
        print(tree[0] + ',', end=' ')
    print()

    # действие

    # рост деревьев

    for tree in trees:
        if tree[5] < tree[1]:
            tree[5] += 1
        else:
            tree[3] = tree[4]

    round += 1
