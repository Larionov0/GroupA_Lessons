file = open('Files/file3.txt', 'rt', encoding='utf-8')

cities = []
for line in file:  # ' Киев,Одесса  ,   Харьков  \n'
    line_cities = line.rstrip().split(',')  # ['  Киев ', ...]
    for brute_city in line_cities:
        clean_city = brute_city.strip()
        cities.append(clean_city)


file.close()

print(cities)
