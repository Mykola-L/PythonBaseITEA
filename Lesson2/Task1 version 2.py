number = float(input('Введіть, будь-ласка, число '))
number2 = number % 2
if number2 == 0:
    print(f'Ви ввели парне число {number}')
else:
    print(f'Ви ввели непарне число {number}')