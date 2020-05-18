#loop цикл
# i = 0
# list_size = 6
# my_list = [1, 2, 3, 4, 5, 6]
# while i < list_size:
#     print(my_list[i])
#     i += 1 # i = i + 1

# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list[-1])

# Continue and break

# numbers = (2, 2, 3, 2, 4, 5, 4, 5, 10, 20, 30, 40) # масив кортеж
# i = 0
# length_of_tuple = 12 # довжина списку
# matches = 0 # кількість співпадінь
#
# while i < length_of_tuple:
#     element = numbers[i] # зберігаємо в змінну елемент
#     print(i)
#     if element == 2:
#         matches += 1 # matches = matches + 1
#         if matches > 2:
#             break # перериваємо цикл
#
#     i += 1  # i = i + 1
#
# if matches > 2:
#     print(f'Кількість співпадінь більше двох')

a = [1, 2, 2, 2, 2, 2, 6, 4, 3]
i = 0
len_of_a = 9

while i < len_of_a:
    elem = a[i]
    i += 1 # i = i + 1

    if elem == 2:
        continue
    else:
        print(elem)


