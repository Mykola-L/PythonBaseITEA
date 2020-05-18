import random

# n = int(input('Введіть, будь-ласка, число. Варіант 1  '))
# if my_random == n:
#     print('Вітаємо, ви ввели вірне число.')

secret_number = random.randint(50, 100)  # генерує випадкові числа від 50 до 100
print(secret_number)

i = 0
while i < 4:


    user_number = int(input('Вгадайте ціле число в діапазоні від 50 до 100 '))

    if user_number == secret_number:
        print('Вітаємо, ви ввели вірне число.')
        break
    elif user_number < secret_number:
        print(f'Нажаль, число має бути більше. У вас залишилося {3-i} спроб')
    elif user_number > secret_number:
        print(f'Нажаль, число має бути менше. У вас залишилося {3-i} спроб')



    i += 1  # i = i + 1

if i == 4:
    print('Нажаль, ви не вгадали')