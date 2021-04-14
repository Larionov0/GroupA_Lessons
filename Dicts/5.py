animal1 = ['kurka', 'Ryaba', 4, [1, 2], 'k']

animal2 = {
    'type': 'kurka',
    'name': 'Ryaba',
    'hp': 4,
    'coords': [1, 2],
    'sprite': 'k'
}

# Delete value
animal1.pop(-1)
value = animal2.pop('sprite')

print(animal2)
print(value)
