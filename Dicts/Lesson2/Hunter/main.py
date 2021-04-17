from os import system
import random

N = 15
M = 20

hero = {
    'name': 'Bob',
    'coords': [3, 3],  # [i, j]
    'hp': 10,
    'sprite': '+',
    'details': 0
}

animals = [
    {
        'type': 'kurka',
        'name': 'Marusya',
        'hp': 3,
        'coords': [5, 5],
        'sprite': 'k'
    },
    {
        'type': 'kurka',
        'name': 'Ryaba',
        'hp': 3,
        'coords': [6, 5],
        'sprite': 'k'
    },
    {
        'type': 'kurka',
        'name': 'Masha',
        'hp': 3,
        'coords': [5, 6],
        'sprite': 'k'
    },
]

round_ = 0
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

    # прорисовка объектов
    # проприсовка Героя
    matrix[hero['coords'][0]][hero['coords'][1]] = hero['sprite']
    # прорисовка животных
    for animal in animals:
        matrix[animal['coords'][0]][animal['coords'][1]] = animal['sprite']

    # очистка экрана
    system('cls')

    # вывод матрицы на экран
    for row in matrix:
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        print(row_text[:-1] + '|')

    # ход игрока
    print('Герой: ', hero['name'])
    print('Детали: ', hero['details'])
    choice = input('WASD: ')
    if choice == 'w':
        if hero['coords'][0] != 0:
            hero['coords'][0] -= 1
    elif choice == 'a':
        if hero['coords'][1] == 0:
            hero['coords'][1] = M - 1
        else:
            hero['coords'][1] -= 1
    elif choice == 's':
        if hero['coords'][0] != N - 1:
            hero['coords'][0] += 1
    elif choice == 'd':
        if hero['coords'][1] == M - 1:
            hero['coords'][1] = 0
        else:
            hero['coords'][1] += 1

    # не поймал ли курицу
    i = 0
    for animal in animals:
        if animal['type'] == 'kurka':
            if animal['coords'] == hero['coords']:
                hero['details'] += 3
                animals.pop(i)
                break
        i += 1

    # ход животных
    for animal in animals:
        if animal['type'] == 'kurka':
            kurka_coords = animal['coords']
            direction = random.choice(['w', 'a', 's', 'd'])
            if direction == 'w':
                if kurka_coords[0] != 0:
                    kurka_coords[0] -= 1
            elif direction == 'a':
                if kurka_coords[1] == 0:
                    kurka_coords[1] = M - 1
                else:
                    kurka_coords[1] -= 1
            elif direction == 's':
                if kurka_coords[0] != N - 1:
                    kurka_coords[0] += 1
            elif direction == 'd':
                if kurka_coords[1] == M - 1:
                    kurka_coords[1] = 0
                else:
                    kurka_coords[1] += 1

        elif animal['type'] == 'olen':
            pass

    # не поймал ли курицу
    i = 0
    for animal in animals:
        if animal['type'] == 'kurka':
            if animal['coords'] == hero['coords']:
                hero['details'] += 3
                animals.pop(i)
                break
        i += 1

    # появление животных
    if round_ % 10 == 0:  # появление куриц
        kurka = {
            'type': 'kurka',
            'name': random.choice(['Ryaba', 'Baba', 'Boba', 'Alyona', 'Veronika', 'Misha']),
            'hp': 3,
            'coords': [random.randint(0, N - 1), random.randint(0, M - 1)],
            'sprite': 'k'
        }
        animals.append(kurka)
    elif round_ % 40 == 0:  # появление оленей
        pass

    round_ += 1
