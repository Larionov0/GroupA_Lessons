cities = [
    {
        'name': 'Karyakinsk',
        'people_amount': 140000,
        'parks': 15,
        'monuments': 56,
        'beaches': 12
    },
    {
        'name': 'Lvivsk',
        'people_amount': 250000,
        'parks': 25,
        'monuments': 16,
        'beaches': 0
    },
    {
        'name': 'Aelxivsk',
        'people_amount': 45000,
        'parks': 30,
        'monuments': 102,
        'beaches': 15
    },
    {
        'name': 'Jojinsk',
        'people_amount': 100000,
        'parks': 12,
        'monuments': 89,
        'beaches': 31
    },
]

total_people = 0
for city in cities:
    total_people += city['people_amount']

print(total_people)
