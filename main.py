vegetables = []

while True:
    print('\n\nВводите названия овощей, чтобы добавлять их в список или "стоп",'
          '\nчтобы ввести букву и вывести индексы, где есть эта буква в списке')
    vegetable = input('\n')
    if vegetable == 'стоп':
        
        find_letter = input('\nВведите букву:')
        i = 0
        for veget in vegetables:
            
            if find_letter in veget:
                print('\nВ', veget,'-', i, '- в списке ,индекс:', end=' ')
                j = 0
                for letter in veget:
                    if letter == find_letter:
                        print(j, end = '; ')
                    j += 1
            i += 1
            
    else:
        vegetables += [vegetable]
        print('\n', vegetables)



