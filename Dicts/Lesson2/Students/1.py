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

total_marks_sum = 0
total_marks_count = 0
for group_name, group in students.items():
    for student in group:
        for subject, mark in student['marks'].items():
            total_marks_count += 1
            total_marks_sum += mark

print(total_marks_sum / total_marks_count)
