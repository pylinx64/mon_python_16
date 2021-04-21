try:
    a = 100 / 0
    if a > 10:
        print(a)
except ZeroDivisionError:
    print('Нельзя делить на ноль!!')
except TypeError:
    print('Нельзя делить на букву!!')
