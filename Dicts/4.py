animal1 = ['kurka', 'Ryaba', 4, [1, 2], 'k']

animal2 = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 4,
    'coords': [1, 2],
    'sprite': 'k'
}


# Add value
animal1.append(':)')
animal2['emotion'] = ':)'

print(animal2)
