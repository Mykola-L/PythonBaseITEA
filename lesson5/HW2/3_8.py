# 3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

import random
import time
from random import seed
from random import randint

a = 100000


def list_generator(a):
    # generate random integer values
    my_list = []  # створюю список
    # seed random number generator
    seed(1)
    # generate some integers
    for _ in range(a):
        my_list.append((random.randint(0, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список


    # # Цикл while викликає функцію багато разів
    # i = 0
    # while i < a:  # розмір списку
    #     my_list.append((random.randint(0, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список
    #     i += 1  # i = i + 1

    # return my_list

    print(my_list)



start_time = time.time()
list_generator(a)
# print("--- %s seconds ---" % (time.time() - start_time)) # час роботи функції
print("Час виконання функції: " + " %s seconds " % (time.time() - start_time)) # час роботи функції