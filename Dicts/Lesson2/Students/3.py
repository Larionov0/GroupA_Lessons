students = {
    'A': [
        {
            'name': 'Alex',
            'surname': 'Bubenkov',
            'age': 16,
            'hobbies': ['football', 'fishing'],
            'city': 'Kyiv',
            'marks': {
                'Python': 11,
                'math': 10,
                'English': 8
            }
        },
        {
            'name': 'Bob',
            'surname': 'Bubchik',
            'age': 12,
            'hobbies': ['piano', 'games', 'drawing', 'eat'],
            'city': 'Lviv',
            'marks': {
                'Python': 8,
                'math': 9,
                'English': 9
            }
        },
        {
            'name': 'Olya',
            'surname': 'Olchik',
            'age': 13,
            'hobbies': ['dancing', 'piano', 'drawing'],
            'city': 'Kyiv',
            'marks': {
                'Python': 7,
                'math': 6,
                'English': 10
            }
        },
    ],
    'B': [
        {
            'name': 'Kyrylo',
            'surname': 'Kira',
            'age': 24,
            'hobbies': ['eat', 'sleep', 'anime'],
            'city': 'Kyiv',
            'marks': {
                'Python': 9,
                'math': 11,
                'English': 10
            }
        },
        {
            'name': 'Polina',
            'surname': 'Polya',
            'age': 12,
            'hobbies': ['guitar', 'anime', 'drawing'],
            'city': 'Kyiv',
            'marks': {
                'Python': 9,
                'math': 10,
                'English': 9
            }
        },
    ],
    'C': [
        {
            'name': 'Olya',
            'surname': 'Golya',
            'age': 14,
            'hobbies': ['guitar', 'eat', 'games', 'nature'],
            'city': 'Lviv',
            'marks': {
                'Python': 11,
                'math': 11,
                'English': 11
            }
        },
        {
            'name': 'Mykola',
            'surname': 'Boechko',
            'age': 15,
            'hobbies': ['games', 'anime', 'football'],
            'city': 'Lviv',
            'marks': {
                'Python': 11,
                'math': 11,
                'English': 11
            }
        },
    ]
}

max_count_of_excellent_students = 0
max_group_name = ''

for group_name, group in students.items():
    count_of_excellent_students_in_group = 0
    # считаем, сколько в текущей группе отличников
    for student in group:
        is_excellent = True
        for subject, mark in student['marks'].items():
            if mark < 10:
                is_excellent = False
                break

        if is_excellent:
            count_of_excellent_students_in_group += 1

    if count_of_excellent_students_in_group > max_count_of_excellent_students:
        max_count_of_excellent_students = count_of_excellent_students_in_group
        max_group_name = group_name
    print(group_name, count_of_excellent_students_in_group)

print('Победитель: ')
print(max_group_name)
print(max_count_of_excellent_students)
