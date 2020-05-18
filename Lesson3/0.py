import random
# print(random.random)
#
# n = input('Введіть, будь-ласка, кількість цілочисельних випадкових значень ')
#
# my_random = random.randint(50, 100) # генерує випадкові числа від 50 до 100
#
# print(my_random)

# print(random.seed([X], version=2))


# print(list(random.seed([1], version=2)))

# from random import randint, seed
#
# seed(1)
# # Далее даны примеры случайных чисел.
# print(randint(1, 20))  # 5
# print(randint(1, 20))  # 19

# random module is imported
# import random
#
# for i in range(5):
#     # Any number can be used in place of '0'.
#     random.seed(0)
#
#     # Generated random number will be between 1 to 1000.
#     print(random.randint(1, 1000))


# importing random module
import random

# random.seed(3)
#
# # print a random number between 1 and 1000.
# print(random.randint(1, 1000))
#
# # if you want to get the same random number again then,
# random.seed(3)
# print(random.randint(1, 1000))
#
# # If seed function is not used

# Gives totally unpredictable responses.
# print(random.randint(1, 1000))


n = int(input('Введіть, будь-ласка, кількість цілочисельних випадкових значень '))

# l = [i for i in random.randint(1, 1000)]
# print(l)


# Як вивести функцію print() багато разів
i=0
while i < 10:
   # print(list(range(random.randint(1, 1000))))  # переводимо range в list
   print(random.randint(1, 100))  # генерує випадкові числа від 1 до 1000

    i += 1  # i = i + 1



# my_random = random.randint(1, 1000) # генерує випадкові числа від 1 до 1000
# print(my_random)
#
# my_list = i
#
# a = [i]
# i = 0
# len_of_a = n
#
# while i < len_of_a:
#     a  = my_random
#     i += 1 # i = i + 1
#
#     if elem == 2:
#         continue
#     else:
#         print(elem)

# from random import randint
# l = [randint(10,80) for x in range(10)]
