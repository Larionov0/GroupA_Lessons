names_marks = {
    'Bob': 59,
    'Alan': 13,
    'Katia': 69,
    'Gena': 79,
    'Alina': 53
}

max_mark = 0
max_name = ''
for name, mark in names_marks.items():
    if mark > max_mark:
        max_mark = mark
        max_name = name

print(max_mark)
print(max_name)
