number = int(input('Введіть, будь-ласка, значення в метрах '))
unit = input('Введіть, будь-ласка, одиницю виміру (mm, sm, km) ')
#print(unit)
if unit == 'mm':
    print(f'Значення в міліметрах {number * 1000}')
elif unit == 'sm':
        print(f'Значення в сантиметрах {number * 100}')
elif unit == 'km':
        print(f'Значення в кілометрах {number / 1000}')
else:
    print('Ви ввели невірні дані')

