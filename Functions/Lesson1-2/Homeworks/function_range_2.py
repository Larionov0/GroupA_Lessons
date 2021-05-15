def func_range(a=None, b=None, c=1):
    if a > 0 and b == None and c == 1:  # range(+a)
        i = 0
        while i < a + 1:
            print(i)
            i += 1
    elif a < 0 and b == None and c == 1:  # range(-a)
        i = 0
        while i > a - 1:
            print(a)
            a += 1
    elif a < b and c == 1:  # range (a, b, c == 1)

        while a < b + 1:
            print(a)
            a += 1
    elif a < b and c != 1 and c > 0:  # range (a, b, c > 0)
        while a < b + 1:
            print(a)
            a += c
    elif b < a and c != 1 and c < 0:  # range (a, b, c < 0)
        while b < a + 1:
            print(a)
            a += c


func_range(5)
