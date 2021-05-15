def input_int(question, error_msg='Введите цифры'):
    while True:
        ans = input(question)
        if ans.isdigit():
            return int(ans)
        else:
            print(error_msg)


def input_str(question, error_msg='Введите cлова'):
    while True:
        ans = input(question)
        if ans.isdigit():
            print(error_msg)
        else:
            return str(ans)


def print_dict(dict):
    for rooms, structure in dict.items():
        for room in structure:
            print(room)


def new_room(key, value):  # не рабочая
    dict = {}
    while True:
        key = input('Введите предмет комнаты или закончить ввод - "q": ')
        if key == 'q':
            return dict
        else:
            value = input('Введите количество: ')
            dict[key] = value


def append_room(dict):
    new_room = {}
    for rooms, structure in dict.items():
        for room in structure:
            for key, value in room.items():
                if key != 'предметы':
                    print('Введите', key)
                    number = input()
                    if number == 'q':
                        return dict
                    else:
                        new_room[key] = number
                else:
                    room_number_items = {}
                    while True:
                        room_items = input_str('Введите предмет комнаты или закончить ввод - "q": ')

                        if room_items == 'q':
                            break
                        else:
                            number_items = input_int('Введите количество: ')
                            room_number_items[room_items] = number_items
                    new_room[key] = room_number_items
                    dict['комнаты'].append(new_room)
                    return dict


def add_room_menu(data):
    print('/' * 15, 'Добавление комнаты', '/' * 15)
    print('Добавить комнату - "Enter"')
    add_room = input()

    if add_room == '':
        append_room(data)

        print_dict(data)


def delete_room_menu(data):
    for rooms, structure in data.items():
        for room in structure:
            print(room)
    print()
    print('"Enter" - Exit')
    delete_room = input('Выберите комнату для удаления: ')
    if delete_room.isdigit():
        for rooms, structure in data.items():
            i = 0
            while i < len(structure):
                for key, value in structure[i].items():
                    if key == 'номер' and value == int(delete_room):
                        data['комнаты'].pop(i)
                        print('Удаление прошло успешно!')

                i += 1
    else:
        print('Введите число')


def hotel_ob_menu(data):
    while True:
        print('*' * 15, 'МЕНЮ ОБУСТРОЙСТВА ОТЕЛЯ', '*' * 15)
        print('1. Добавить комнату')
        print('2. Удалить комнату')
        print('3. Выход')

        choice_hotel_arrangement = input()

        if choice_hotel_arrangement == '1':  # Добавить комнату
            add_room_menu(data)

        if choice_hotel_arrangement == '2':  # Удалить комнату
            delete_room_menu(data)

        if choice_hotel_arrangement == '3':
            break


def new_rooms_search(data):
    room_area = input('Введите минимальную площадь, которую ищете: ')
    number_of_visitors = input('Введите количество посетителей: ')
    print()
    for rooms, structure in data.items():
        for room in structure:
            if (room['длина'] * room['ширина']) > int(room_area) and (
                    room['посетителей допустимо'] - room['заселено']) > int(number_of_visitors):
                print('Вам подойдет комната:', room['номер'], ';стоимость:', room['стоимость'])


def add_guests_menu(data):
    what_number = input('Напишите какой номер ищите: ')
    number_of_guests = input('Какое у вас количество гостей: ')
    print()
    for rooms, structure in data.items():
        for room in structure:
            if room['номер'] == int(what_number) and room['заселено'] + int(number_of_guests) <= room[
                'посетителей допустимо']:
                room['заселено'] += int(number_of_guests)
                print('Заселено успешно!')

    for rooms, structure in data.items():
        for room in structure:
            print('Номер:', room['номер'], ';Заселено:', room['заселено'])


def show_statistics_menu(data):
    while True:
        print()
        print('1. Общее количество допустимых гостей и количество реальных на текущий момент')
        print('2. Суммарная площадь всех номеров в отеле')
        print('3. Список всех предметов интерьера со всех комнат и их количество')
        print('4. Суммарная стоимость всех комнат')
        print('5. назад')
        choice_stat = input()
        print()
        if choice_stat == '1':  # Общее количество допустимых гостей и количество реальных на текущий момент
            all_guest = 0
            real_guest = 0
            for rooms, structure in data.items():
                for room in structure:
                    all_guest += room['посетителей допустимо']
                    real_guest += room['заселено']
            print('В данный момент гостиница вмещает -', all_guest, 'гостей,', 'заселено-', real_guest)

        elif choice_stat == '2':  # Суммарная площадь всех номеров в отеле
            area_of_rooms = 0
            for rooms, structure in data.items():
                for room in structure:
                    area_of_rooms += room['длина'] * room['ширина']
            print('Площадь всех номеров в отеле:', area_of_rooms)

        elif choice_stat == '3':  # Список всех предметов интерьера со всех комнат и их количество
            hotel_items = {}
            for rooms, structure in data.items():
                for room in structure:
                    for item, number in room['предметы'].items():
                        if item not in hotel_items:
                            hotel_items[item] = number
                        else:
                            hotel_items[item] += number
            for item, number in hotel_items.items():
                print(item, ':', number)

        elif choice_stat == '4':  # Суммарная стоимость всех комнат
            cost_of_all_rooms = 0
            for rooms, structure in data.items():
                for room in structure:
                    cost_of_all_rooms += room['стоимость']
            print('Стоимость всех комнат:', cost_of_all_rooms)

        elif choice_stat == '5':
            break


def create_init_data():
    data = {
        'комнаты': [
            {
                'номер': 4,
                'ширина': 4.5,
                'длина': 6.3,
                'стоимость': 4000,
                'посетителей допустимо': 3,
                'заселено': 0,
                'предметы': {'шкаф B': 2, "телевизор ACA": 1, "стол дерево": 2, "стул пластик A": 5, 'кровать C': 1}
            },
            {
                'номер': 6,
                'ширина': 5.5,
                'длина': 2.3,
                'стоимость': 3000,
                'посетителей допустимо': 1,
                'заселено': 1,
                'предметы': {'шкаф B': 1, "стол пластик": 1, "стул пластик A": 1, 'кровать D': 1}
            },
            {
                'номер': 9,
                'ширина': 6.5,
                'длина': 2.5,
                'стоимость': 5000,
                'посетителей допустимо': 4,
                'заселено': 2,
                'предметы': {'шкаф B': 2, "телевизор ACA": 1, "стол дерево": 2, "стул пластик A": 1, 'кровать C': 1}
            },
        ]
    }
    return data


def main():
    data = create_init_data()

    while True:
        print('-' * 15, 'ГЛАВНОЕ МЕНЮ', '-' * 15)
        print('1. Обустройство отеля')
        print('2. Поиск доступных номеров')
        print('3. Добавить гостей')
        print('4. Статистика')
        print('5. Выход из программы')

        choice = input()
        if choice == '1':
            hotel_ob_menu(data)

        if choice == '2':  # Поиск доступных номеров
            new_rooms_search(data)

        if choice == '3':  # Добавить гостей
            add_guests_menu(data)

        if choice == '4':  # Статистика
            show_statistics_menu(data)

        if choice == '5':
            print('-' * 15, 'BYE!', '-' * 15)
            break


main()
