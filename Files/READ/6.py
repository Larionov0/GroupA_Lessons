file = open('Files/file2.txt', 'rt', encoding='utf-8')

cities = []
for line in file:  # 'Киев, Одесса, Харьков\n'
    line_cities = line.rstrip().split(', ')  # ['Киев', ...]
    cities.extend(line_cities)

file.close()

print(cities)
