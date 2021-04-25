def helloer1():
    print('Hello world!')


def helloer(name):
    print('Hello,', name, '!')


def summer(n1, n2):
    s = n1 + n2
    return s


def kley(s1, s2, s3, sep):
    res_str = s1 + sep + s2 + sep + s3
    return res_str


def f(a):
    a += 1
    print(a)


def f2(name):
    print(name)


def input_int(question, error_msg='Введите число'):
    while True:
        ans = input(question)
        if ans.isdigit():
            return int(ans)
        else:
            print(error_msg)


age = input_int('Сколько вам лет: ')
print(age + 1)


k = input_int('Сколько котлет вам подать, сударь: ', 'Многоуважаемый польователь, будьте добры ввести число')

print(k)
