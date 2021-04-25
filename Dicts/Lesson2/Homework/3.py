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


eat_fish_names = {}

for fish in fishes:
    for eat in fish['ест']:
        if eat not in eat_fish_names:
            eat_fish_names[eat] = []
        eat_fish_names[eat].append(fish['имя'])


for eat, names in eat_fish_names.items():
    print(eat, names)
