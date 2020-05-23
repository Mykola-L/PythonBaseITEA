import random

# def random_numerical_sequence(n):
#
#     sum = 0
#     for i in n:
#         sum += int(i)  # sum = sum + int(i)
#     print(sum)
#     return sum
#
#
# n = input('Введіть, будь-ласка, число ')
# random_numerical_sequence(random.randint(1, 1000)) # додаємо випадкові числа (від 1 до 1000) в список
# my_list = []  # створюю список
# my_list.append((random.randint(1, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список

my_list = []  # створюю список
# Цикл while викликає функцію багато разів
i = 0
n = 1000
while i < n:  # розмір списку
    my_list.append((random.randint(1, n)))  # додаємо випадкові числа (від 1 до 1000) в список
    i += 1  # i = i + 1
print(my_list)

#my_list.count(i) # повертає кількість елементів із значенням i
my_list2 = []

a = 0
for i in my_list:
    my_list2.append(my_list.count(i))
    i = i + 1
print(my_list2)
#return a