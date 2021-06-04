try:
    a = 10
    print(a / 0)
    print('Цей текст ніхто не побачить')
except ZeroDivisionError:
    print('Щось пішло не так, схоже, десь відбулося ділення на нуль!')


print(':)')
