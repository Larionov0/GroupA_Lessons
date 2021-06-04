lst = ['a', 'b', 'c', 'd', 'e', 'f']

while True:
    i = input('Введіть індекс: ')
    if i.isdigit():
        i = int(i)
        if i > len('lst'):
            print('Невірний індекс')
        print(lst[i])
    else:
        print('Ви ввели не число')
