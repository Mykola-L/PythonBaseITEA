number = int(input('Введіть, будь-ласка, число '))
number2 = number % 2
if number2 == 1:
    print(f'Ви ввели непарне число {number}')
else:
    print(f'Ви ввели парне число {number}')