file = open('Files/file2.txt', 'rt', encoding='utf-8')

lines = file.readlines()
print(lines)

file.close()
