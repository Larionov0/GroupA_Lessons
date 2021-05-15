from os import system
import random
import msvcrt
import time


N = 15
M = 20


def clear():
    system('cls')


def press(question):
    print(question)
    return msvcrt.getch().decode()


def press2(question):
    return input(question)


def choice_letter(question, letters, error_message='У вас нету такого варианта'):
    while True:
        letter = press(question)
        if letter in letters:
            return letter
        else:
            print(error_message)


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


def draw_all_objects(field, hero, animals, items):
    draw_creature(field, hero)
    for animal in animals:
        draw_creature(field, animal)
    for item in items:
        draw_creature(field, item)


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


def is_item_caught(hero, items):
    i = 0
    for item in items:
        if item['type'] == 'details':
            if item['coords'] == hero['coords']:
                hero['details'] += item['amount']
                items.pop(i)
                break
        i += 1


def player_make_move(hero, animals, field, items):
    clear()
    print_matrix(field)

    print('Герой: ', hero['name'])
    print('Детали: ', hero['details'])
    print('wasd - перемещение')
    print('x - выстрел')
    print('z - выход')
    choice = press('Ваш выбор: ')
    if choice in ['w', 'a', 's', 'd']:
        creature_moves(hero, choice)
    elif choice == 'x':
        player_shoot_menu(hero, animals, items)
    elif choice == 'z':
        exit()


def player_shoot_menu(hero, animals, items):
    if hero['main_weapon']:
        w_type = hero['main_weapon']['type']
        if w_type == 'bow':
            bow_shoot(hero, animals, items)
        elif w_type == 'slingshot':
            pass


def bow_shoot(hero, animals, items):
    dir = choice_letter('Куда страляем? ', 'wasdq')
    if dir == 'q':
        return
    else:
        arrow = {
            'type': 'arrow',
            'sprite': 'x',
            'energy': hero['main_weapon']['range'],
            'damage': hero['main_weapon']['damage'],
            'coords': hero['coords'].copy(),
            'direction': dir
        }
        arrow_fly(hero, arrow, animals, items)


def arrow_fly(hero, arrow, animals, items):
    while arrow['energy'] != 0:
        creature_moves(arrow, arrow['direction'])

        field = create_matrix(N, M)
        draw_all_objects(field, hero, animals, items)
        draw_creature(field, arrow)
        clear()
        print_matrix(field)

        for animal in animals:
            if animal['coords'] == arrow['coords']:
                animal_gets_damage(animal, arrow['damage'], animals, items)
                return
        arrow['energy'] -= 1
        time.sleep(0.5)


def kurka_make_move(kurka):
    direction = random.choice(['w', 'a', 's', 'd'])
    creature_moves(kurka, direction)


def animal_gets_damage(animal, damage, animals, items):
    animal['hp'] -= damage
    if animal['hp'] <= 0:
        animal_dies(animal, animals, items)


def animal_dies(animal, animals, items):
    if animal['type'] == 'kurka':
        kurka_dies(animal, animals, items)


def kurka_dies(kurka, animals, items):
    items.append(
        {
            'type': 'details',
            'sprite': '#',
            'coords': kurka['coords'].copy(),
            'amount': 3
        }
    )
    animals.remove(kurka)


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
        'details': 0,
        'main_weapon': {
            'type': 'bow',
            'range': 4,
            'damage': 3,
            'durability': 10,
            'price': 30
        }
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

    items = [
        {
            'type': 'details',
            'sprite': '#',
            'coords': [1, 7],
            'amount': 2
        }
    ]

    return hero, animals, items


def main():
    hero, animals, items = create_init_data()
    round_ = 1
    while True:
        field = create_matrix(N, M)
        draw_all_objects(field, hero, animals, items)

        player_make_move(hero, animals, field, items)
        is_item_caught(hero, items)
        is_kurka_caught(hero, animals)
        animals_make_move(animals)
        is_kurka_caught(hero, animals)

        check_spawn_animals(animals, round_)
        round_ += 1


main()
