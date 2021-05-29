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


def print_list_of_dicts(list_of_dicts):
    for dct in list_of_dicts:
        for key, value in dct.items():
            print(key, ':', value, '|', end='')
        print()
        print('-' * 130)


def print_store_table(store):
    print('-'*65)
    print('|%-15s|%-15s|%-15s|%-15s|' % ('Товар', "Цена", "Количество", "Производитель"))
    print('-' * 65)
    for product in store:
        row = '|%-15s|%-15f|%-15i|%-15s|' % (
            product['product_name'],
            product['product_price'],
            product['quantity_in_stock'],
            product['manufacturer']
        )
        print(row)
    print('-'*65)


def main_menu(store, manufacturers):
    while True:
        print('1. Создать товар')
        print('2. Удалить товар')
        print('3. Найти самый дешевый товар')
        print('4. Подсчитить на какую сумму товары на складе')
        print('5. Вывести все товары в виде таблицы')
        print('6. Редактирование товара')
        print('7. Просмотр производителей')

        choice = input()

        if choice == '1':  # СОЗДАНИЕ ТОВАРА
            choice_menu_1(store)

        elif choice == '2':  # УДАЛЕНИЕ ТОВАРА
            choice_menu_2(store)

        elif choice == '3':  # Найти самый дешевый товар
            choice_menu_3(store)

        elif choice == '4':  # Подсчитить на какую сумму товары на складе
            choice_menu_4(store)

        elif choice == '5':  # Вывести все товары в виде таблицы
            print_store_table(store)

        elif choice == '6':  # Редактирование товара
            choice_menu_6(store)

        elif choice == '7':  # Просмотр производителей
            choice_menu_7(store, manufacturers)


def choice_menu_1(store):
    print('********* СОЗДАНИЕ ТОВАРА **********')

    store.append({'product_name': input_str('product_name: '),
                  'product_price': int(input_int('product_price: ')),
                  'quantity_in_stock': int(input_int('quantity_in_stock: ')),
                  'manufacturer': input_str('manufacturer: ')
                  })
    print_list_of_dicts(store)


def choice_menu_2(store):
    print('********* УДАЛЕНИЕ ТОВАРА **********')
    for products in store:
        for key, value in products.items():
            if key == 'product_name':
                print(value)

    del_product = input_str('Введите продукт для удаления: ')
    i = 0
    while i < len(store):
        if del_product == store[i]['product_name']:
            del store[i]
        i += 1
    print_list_of_dicts(store)


def choice_menu_3(store):
    chape_product = ''
    chape_cost = float("inf")
    for products in store:
        for key, value in products.items():
            if key == 'product_price':
                if value < chape_cost:
                    chape_cost = value
                    chape_product = products['product_name']
    print('Дешевый товар:', chape_product, '; Цена:', chape_cost)


def choice_menu_4(store):
    all_cost = 0
    for products in store:
        all_cost += products['product_price']
    print('Общая стоимость всех товаров на складе:', all_cost)


def edit_product_menu(product):
    while True:
        print('********* РЕДАКТИРОВАНИЕ ТОВАРА **********')
        print('1. Изменить название')
        print('2. Изменить стоимость')
        print('3. Изменить количество')
        print('4. Выход из меню')

        print(product)

        product_editor = input('Выберите пункт меню: ')

        if product_editor == '1':  # Изменить название
            new_name = input('Введите новое название товара: ')
            product['product_name'] = new_name

        if product_editor == '2':  # Изменить стоимость
            new_price = input_int('Введите новую цену товара: ')
            product['product_price'] = new_price

        if product_editor == '3':  # Изменить количество
            new_quantity = input_int('Введите новое количество товара: ')
            product['quantity_in_stock'] = new_quantity

        if product_editor == '4':  # Выход из меню
            break


def choice_menu_6(store):
    i = 1
    while i < len(store) + 1:
        print(str(i) + '.', store[i - 1]['product_name'])
        i += 1

    product_index = int(input_int('Введите номер товара: ')) - 1
    edit_product_menu(store[product_index])


def choice_menu_7(store, manufacturers):
    i = 0
    while i < len(manufacturers):
        the_sum_of_all_products = 0
        the_sum_of_all_products_produced = 0
        for product in store:
            if manufacturers[i]['name'] == product['manufacturer']:
                the_sum_of_all_products_produced += 1
                the_sum_of_all_products += product['quantity_in_stock']
        manufacturers[i]['the sum of all products produced'] = the_sum_of_all_products_produced
        manufacturers[i]['the sum of all products in the shops'] = the_sum_of_all_products
        i += 1

    print_dict(manufacturers)


def create_init_data():
    manufacturers = [
        {'id': 758,
         'name': 'BULKA',
         'citys': ['Slovyansk', 'Igovsk'],
         'rating': 9},

        {'id': 365,
         'name': 'SALO',
         'citys': ['Irpin', 'Lugansk', 'Chernigov'],
         'rating': 5},

        {'id': 259,
         'name': 'OIL',
         'citys': ['Lviv', 'Jitomir', 'Harkov'],
         'rating': 7},

        {'id': 335,
         'name': 'Plastic',
         'citys': ['Gigantsk', 'Mutantsk'],
         'rating': 7},
    ]

    store = [{'product_name': 'hleb',
              'product_price': 15,
              'quantity_in_stock': 50,
              'manufacturer': 'BULKA'},

             {'product_name': 'baton',
              'product_price': 20,
              'quantity_in_stock': 35,
              'manufacturer': 'BULKA'},

             {'product_name': 'karton',
              'product_price': 20,
              'quantity_in_stock': 35,
              'manufacturer': 'BULKA'}
             ]
    return store, manufacturers


store, manufactures = create_init_data()
main_menu(store, manufactures)
