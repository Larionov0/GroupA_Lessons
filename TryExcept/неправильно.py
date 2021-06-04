# неправильне використання try - except

lst = ['a', 'b', 'c', 'd', 'e', 'f']

while True:
    try:
        i = int(input('Введіть індекс: '))
        print(lst[i])
    except IndexError:
        print('Ви введи не той індекс!')
    except ValueError:
        print('Ви ввели не число')

