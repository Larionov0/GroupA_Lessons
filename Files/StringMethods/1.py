exp = input('Введите выражение с плюсами:\n')
numbers = exp.split('+')
sum = 0
for number in numbers:
    sum += int(number.strip())

print(sum)
