# 3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

import random
import time

a = 100000


def list_generator(a):
    my_list = []  # створюю список
    i = 0
    while i < a:  # розмір списку
        my_list.append((random.randint(0, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список
        i += 1  # i = i + 1

    #print(my_list)



start_time = time.time()
list_generator(a)
print("Час виконання функції: " + " %s seconds " % (time.time() - start_time))
