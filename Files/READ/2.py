file = open('Files/some_file.txt', 'rt')

# Принцип работы курсора (каретки в файле)

text = file.read(4)
print(text)
text = file.read(3)
print(text)
text = file.read()
print(text)
text = file.read()
print('Last: ', text)

file.close()
