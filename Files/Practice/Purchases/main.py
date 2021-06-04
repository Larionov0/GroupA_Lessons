SAVINGS_FILENAME = 'Data/savings.txt'


def create_init_data():
    products = []
    money = 0
    return products, money


def input_str(question, min_=None, max_=None, error_msg='Введите cлова'):
    while True:
        ans = input(question)
        if ans.isdigit():
            print(error_msg)
        else:
            if min_ is not None:
                if len(ans) < min_:
                    print(f'Мало буков! Треба {min_}')
                    continue
            if max_ is not None:
                if len(ans) > max_:
                    print(f'Багато буков! Треба {max_}')
                    continue
            return ans


def input_int(question, min_=None, max_=None, error_msg='Введите число'):
    while True:
        ans = input(question)
        if ans.isdigit():
            number = int(ans)
            if min_ is not None:
                if number < min_:
                    print('Число должно быть не меньше', min_, ', попробуйте еще раз!')
                    continue  # возвращает нас на начало цикла
            if max_ is not None:
                if number > max_:
                    print('Число должно быть не больше', max_, ', попробуйте еще раз!')
                    continue  # возвращает нас на начало цикла
            return number
        else:
            print(error_msg)


def add_product_menu(products):
    product = input_str('Введіть товар: ', min_=3, max_=40)
    products.append(product)


def delete_product_menu(products):
    product = input_str('Введіть товар: ', min_=3, max_=40)
    if product in products:
        products.remove(product)
    else:
        print('Немає такого продукту')


def main_menu(products, money):
    while True:
        print(f'--= Меню покупок =--\n'
              f'Список продуктів: {products}\n'
              f'Гроші на продукти: {money}\n'
              f'1 - додати товар\n'
              f'2 - видалити товар\n'
              f'3 - зберегти\n'
              f'4 - вихід з програми\n'
              f'5 - вивести таблицю\n'
              f'6 - змінити бюджет')
        choice = input('Ваш вибір: ')
        if choice == '1':
            add_product_menu(products)
        elif choice == '2':
            delete_product_menu(products)
        elif choice == '3':
            save_data(money, products)
        elif choice == '4':
            break
        elif choice == '5':
            pass
        elif choice == '6':
            money = input_int('Введіть нову суму: ', min_=0)


def save_data(money, products):
    file = open(SAVINGS_FILENAME, 'wt', encoding='utf-8')

    products_text = ', '.join(products)
    file.write(f"{money}\n{products_text}")

    file.close()


def load_data():
    file = open(SAVINGS_FILENAME, 'rt', encoding='utf-8')

    money = int(file.readline().rstrip())
    products = file.readline().split(', ')

    file.close()
    return products, money


def try_to_load_data():
    try:
        return load_data()
    except Exception as error:
        print(f'Дані не було підгружено через помилку:\n{error}')
        return create_init_data()


def main():
    products, money = try_to_load_data()
    main_menu(products, money)


main()
