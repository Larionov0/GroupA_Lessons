from os import system
import random

N = 15
M = 20

hero_coords = [3, 3]  # [i, j]
hero_name = 'Bob'
hero_sprite = '+'
hero_details = 0

animals = [
    ['kurka', 'Marusya', 3, [5, 5], 'k'],
    ['kurka', 'Ryaba', 3, [6, 5], 'k'],
    ['kurka', 'Masha', 3, [5, 6], 'k'],
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
    matrix[hero_coords[0]][hero_coords[1]] = hero_sprite
    # прорисовка животных
    for animal in animals:  # ['kurka', 'Masha', 3, [5, 6], 'k']
        animal_coords = animal[3]
        animal_sprite = animal[4]
        matrix[animal_coords[0]][animal_coords[1]] = animal_sprite

    # очистка экрана
    system('cls')

    # вывод матрицы на экран
    for row in matrix:
        row_text = '|'
        for el in row:
            row_text += str(el) + ' '
        print(row_text[:-1] + '|')

    # ход игрока
    print('Герой: ', hero_name)
    print('Детали: ', hero_details)
    choice = input('WASD: ')
    if choice == 'w':
        if hero_coords[0] != 0:
            hero_coords[0] -= 1
    elif choice == 'a':
        if hero_coords[1] == 0:
            hero_coords[1] = M - 1
        else:
            hero_coords[1] -= 1
    elif choice == 's':
        if hero_coords[0] != N - 1:
            hero_coords[0] += 1
    elif choice == 'd':
        if hero_coords[1] == M - 1:
            hero_coords[1] = 0
        else:
            hero_coords[1] += 1

    # не поймал ли курицу
    i = 0
    for animal in animals:
        if animal[0] == 'kurka':
            if animal[3] == hero_coords:
                hero_details += 3
                animals.pop(i)
                break
        i += 1

    # ход животных
    for animal in animals:
        if animal[0] == 'kurka':
            kurka_coords = animal[3]
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

        elif animal[0] == 'olen':
            pass

    # не поймал ли курицу
    # тут проверяем, не пришла ли она сама к герою
    i = 0
    for animal in animals:
        if animal[0] == 'kurka':
            if animal[3] == hero_coords:
                hero_details += 3
                animals.pop(i)
                break
        i += 1

    # появление животных
    if round_ % 10 == 0:  # появление куриц
        name = random.choice(['Ryaba', 'Baba', 'Boba', 'Alyona', 'Veronika', 'Misha'])
        coords = [random.randint(0, N - 1), random.randint(0, M - 1)]
        kurka = ['kurka', name, 3, coords, 'k']
        animals.append(kurka)
    elif round_ % 40 == 0:  # появление оленей
        pass

    round_ += 1
