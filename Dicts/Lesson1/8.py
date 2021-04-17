animal1 = ['kurka', 'Ryaba', 4, [1, 2], 'k']

animal2 = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 4,
    'coords': [1, 2],
    'sprite': 'k'
}


# Iterate values
for key, value in animal2.items():
    print(key, ':', value)
