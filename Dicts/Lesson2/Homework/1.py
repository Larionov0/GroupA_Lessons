fishes = [
    {
        'тип': 'карась',
        'имя': 'Жужик',
        'интеллект': 31,
        'ест': ["хлеб", 'белый червь', 'яблоко', "розовый червь"]
    },
    {
        'тип': 'щука',
        'имя': 'Бульба',
        'интеллект': 81,
        'ест': ['розовый червь', 'золото']
    },
    {
        'тип': 'окунь',
        'имя': 'Тэлэпайко',
        'интеллект': 65,
        'ест': ['белый червь', 'крабовые палочки']
    },
    {
        'тип': 'карась',
        'имя': 'Семён',
        'интеллект': 24,
        'ест': ["хлеб", 'белый червь', 'яблоко']
    },
    {
        'тип': 'окунь',
        'имя': 'Пират',
        'интеллект': 68,
        'ест': ["хлеб", 'белый червь', 'яблоко']
    },
    {
        'тип': 'карась',
        'имя': 'Барась',
        'интеллект': 18,
        'ест': ["хлеб", "Мивина"]
    },
    {
        'тип': 'щука',
        'имя': 'Индеец',
        'интеллект': 79,
        'ест': ["розовый червь"]
    },
    {
        'тип': 'карась',
        'имя': 'Птиц',
        'интеллект': 30,
        'ест': ["белый червь", "хлеб", "Мивина"]
    },
    {
        'тип': 'окунь',
        'имя': 'Гуччи',
        'интеллект': 52,
        'ест': ["Мивина", "крабовые палочки"]
    },
]


dct = {}
for fish in fishes:
    if fish['тип'] not in dct:
        dct[fish['тип']] = []

fish_type = ['карась', 'щука', 'окунь']
i = 0
while i < 3:
    fish_type_name = []
    fish_type_eat = []

    for fish in fishes:
        if fish['тип'] == fish_type[i]:
            fish_type_name.append(fish['имя'])
            for eat in fish['ест']:
                if eat not in fish_type_eat:
                    fish_type_eat.append(eat)

    print(fish_type[i])
    for name in fish_type_name:
        print(name, end=' ,')
    print('едят:')
    for eat in fish_type_eat:
        print(eat, end=',')
    print('\n')
    i += 1

