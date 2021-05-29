file = open('Files/file2.txt', 'rt', encoding='utf-8')

for line in file:
    print(line.rstrip())

file.close()
