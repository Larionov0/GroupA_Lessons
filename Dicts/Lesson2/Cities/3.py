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
        'name': 'Alexivsk',
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

max_beach_people_ratio = 0
max_name = ''

for city in cities:
    ratio = city['beaches'] / city['people_amount']
    if max_beach_people_ratio < ratio:
        max_beach_people_ratio = ratio
        max_name = city['name']

print(max_beach_people_ratio, max_name)
