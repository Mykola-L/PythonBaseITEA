secret_number = 86

start_range = 50
end_range = 100

user_number = int(input(f'Вгадайте ціле число в діапазоні від {start_range} до {end_range} '))

if user_number == secret_number and start_range <= user_number <= end_range:
    print('Вітаємо, ви ввели вірне число.')
elif user_number != secret_number and start_range <= user_number <= end_range:
    print('Ви ввели невірне число')
    if user_number < secret_number:
        print('Число має бути більше')
    elif user_number > secret_number:
        print('Число має бути менше')
else:
    print('Число не входить в діапазон')


