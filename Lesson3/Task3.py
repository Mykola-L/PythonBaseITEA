def two_numbers(a, b):
    if a == b:
        print('a дорівнює b')
    elif (a - b) == 5:
        print('a - b = 5')
    elif (b - a) == 5:
        print('b - a = 5')
    elif (a + b) == 5:
        print('b + a = 5')
        return True


two_numbers(15, 10)