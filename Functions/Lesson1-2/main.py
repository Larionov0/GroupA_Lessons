def helloer1():
    print('Hello world!')


def helloer(name):
    print('Hello,', name, '!')


def summer(n1, n2):
    s = n1 + n2
    return s


def kley(s1, s2, s3, sep):
    res_str = s1 + sep + s2 + sep + s3
    return res_str


def f(a):
    a += 1
    print(a)


def f2(name):
    print(name)


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


def double_list(numbers):
    """
    Функция принимает числовой список и возвращает другой список, который состоит из
    удвоенных чисел первого списка.
    Первый список не изменять!
    Example:
        [1, 4, 2] -> [2, 8, 4]
    """
    new_list = []
    for number in numbers:
        new_list.append(number * 2)
    return new_list


def input_str_list(header, input_question, stop=('stop', 'стоп', '-')):
    """
    Предлагает пользователю ввести список строк.
    Возвращает этот список
    :return:
    """
    print(header)
    lst = []
    while True:
        s = input(input_question)
        if s in stop:
            return lst
        if s == '':
            print('Пожалуйста, вводите что-нибудь')
            continue
        lst.append(s)


def fill_row(row=None, n=10):
    if row is None:
        row = []

    for _ in range(n):
        row.append('-')
    return row


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


def func_sum(a, *numbers, **kwargs):
    print(kwargs)

    s = 0
    for number in numbers:
        s += number
    return s


print(func_sum(3, 6, 7, 3, 8, 4, 2, g=2, lol='kek', n=True))


# age = input_int('Сколько вам лет: ', min_=12, max_=120)
# print(age + 1)
#
#
# k = input_int(question='Сколько котлет вам подать, сударь: ', error_msg='Многоуважаемый польователь, будьте добры ввести число')
# print(k)


# names = ['Bob', 'Klara', 'Alice', 'Ksenia']
# n = 1
# for name in names:
#     print(n, '-', name)
#     n += 1
#
# number = input_int('Выберите имя по номеру: ', 1, len(names))
# print(names[number - 1])

# numbers = [1, 5, 3, 7, 4]
# print(double_list(numbers))


# names = input_str_list('Пожалуйста, введите имена', 'Имя: ')
# cities = input_str_list('Вводите список городов', 'Город: ', stop=['-'])
#
# print(names)
# print(cities)

