from os import system
import random
import msvcrt


N = 15
M = 20


def clear():
    system('cls')


def press(question):
    print(question)
    return msvcrt.getch().decode()


def press2(question):
    return input(question)


def create_matrix(n, m, filler='-'):
    return [[filler for _ in range(m)] for _ in range(n)]


def print_matrix(matrix):
    text = ''
    for row in matrix:
        text += '|'
        for el in row:
            text += el + ' '
        text = text[:-1] + '|\n'
    print(text[:-1])


def draw_creature(field, creature):
    field[creature['coords'][0]][creature['coords'][1]] = creature['sprite']


def draw_all_objects(field, hero, animals):
    draw_creature(field, hero)
    for animal in animals:
        draw_creature(field, animal)


def creature_moves(creature, direction):
    if direction == 'w':
        if creature['coords'][0] != 0:
            creature['coords'][0] -= 1
    elif direction == 'a':
        if creature['coords'][1] == 0:
            creature['coords'][1] = M - 1
        else:
            creature['coords'][1] -= 1
    elif direction == 's':
        if creature['coords'][0] != N - 1:
            creature['coords'][0] += 1
    elif direction == 'd':
        if creature['coords'][1] == M - 1:
            creature['coords'][1] = 0
        else:
            creature['coords'][1] += 1


def is_kurka_caught(hero, animals):
    i = 0
    for animal in animals:
        if animal['type'] == 'kurka':
            if animal['coords'] == hero['coords']:
                hero['details'] += 3
                animals.pop(i)
                break
        i += 1


def player_make_move(hero, animals, field):
    clear()
    print_matrix(field)

    print('Герой: ', hero['name'])
    print('Детали: ', hero['details'])
    print('wasd - перемещение')
    print('z - выход')
    choice = press('Ваш выбор: ')
    if choice in ['w', 'a', 's', 'd']:
        creature_moves(hero, choice)
    elif choice == 'z':
        exit()


def kurka_make_move(kurka):
    direction = random.choice(['w', 'a', 's', 'd'])
    creature_moves(kurka, direction)


def olen_make_move(olen):
    pass


def animal_make_move(animal):
    if animal['type'] == 'kurka':
        kurka_make_move(animal)
    elif animal['type'] == 'olen':
        olen_make_move(animal)


def animals_make_move(animals):
    for animal in animals:
        animal_make_move(animal)


# --------- spawn check
def check_spawn_kurka(animals, round_):
    if round_ % 10 == 0:
        new_kurka = {
            'type': 'kurka',
            'name': random.choice(['Ryaba', 'Baba', 'Boba', 'Alyona', 'Veronika', 'Misha']),
            'hp': 3,
            'coords': [random.randint(0, N - 1), random.randint(0, M - 1)],
            'sprite': 'k'
        }
        animals.append(new_kurka)


def check_spawn_olen(animals, round_):
    pass


def check_spawn_animals(animals, round_):
    check_spawn_kurka(animals, round_)
    check_spawn_olen(animals, round_)
# ------------------|


def create_init_data():
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
    return hero, animals


def main():
    hero, animals = create_init_data()
    round_ = 1
    while True:
        field = create_matrix(N, M)
        draw_all_objects(field, hero, animals)

        player_make_move(hero, animals, field)
        is_kurka_caught(hero, animals)
        animals_make_move(animals)
        is_kurka_caught(hero, animals)

        check_spawn_animals(animals, round_)
        round_ += 1


main()
