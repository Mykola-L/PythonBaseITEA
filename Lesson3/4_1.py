import random

my_random = random.randint(50, 100) # генерує випадкові числа від 50 до 100
print(my_random)


n = int(input('Введіть, будь-ласка, число. Варіант 1  '))
if  my_random == n:
    print('Вітаємо, ви ввели вірне число.')

secret_number = 86
user_number = int(input('Вгадайте ціле число в діапазоні від 50 до 100 '))

if user_number == secret_number:
    print('Вітаємо, ви ввели вірне число.')
elif user_number < secret_number:
    print('Нажаль, число має бути більше')
else:
    print('Нажаль, ви не вгадали')

