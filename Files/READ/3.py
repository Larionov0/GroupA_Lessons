file = open('Files/file2.txt', 'rt', encoding='utf-8')

text = file.readline()
print(text)
text = file.readline()
print(text)
text = file.read()
print(text)

file.close()
