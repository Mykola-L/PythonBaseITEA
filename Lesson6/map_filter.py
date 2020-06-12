# # програма вираховує квадрати послідовності
# my_list = [1, 2, 3, 4, 5, 6, 7]
#
# my_list_of_squares = [] # створюю новий список, з допомогою циклу for
#
# for i in my_list:
#     my_list_of_squares.append(i ** 2) # додаємо в новий список квадрат послідовності
#
# print(my_list_of_squares)
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7]
#
# # def to_square(number):
# #     return number ** 2
#
# result = map(lambda number: number ** 2, my_list) # ми зробили простіше застосувавши lambda
# print(tuple(result)) # переведемо map в кортеж
# # print(list(result)) # переведемо map в список

# Реалізація з допомогою циклу
new_sequence = [1, 100, 3, 40, 6, 120]
# вивести список, алементи яких більші 50
greater_than_50 = []

for number in new_sequence:
    if number > 50:
        greater_than_50.append(number)
print(greater_than_50)

# filter
# замість lambda
# def is_greater_than_50(number):
#     return number > 50

result = filter(lambda n: n > 50, new_sequence)
print(list(result))