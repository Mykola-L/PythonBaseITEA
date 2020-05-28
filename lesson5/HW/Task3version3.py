# 3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

import random
import time
from random import seed

a = 100000


def list_generator(a):
    # generate random integer values
    my_list = []  # створюю список
    # seed random number generator
    seed(1)
    # generate some integers
    for _ in range(a):
        my_list.append((random.randint(0, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список


    #print(my_list)



start_time = time.time()
list_generator(a)
print("Час виконання функції: " + " %s seconds " % (time.time() - start_time)) # час роботи функції