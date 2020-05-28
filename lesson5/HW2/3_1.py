#3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

import random

list_generator()

my_list = []  # створюю список
# Цикл while викликає функцію багато разів
    i = 0
    while i < 100000:  # розмір списку
        my_list.append((random.randint(0, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список
        i += 1  # i = i + 1
    return

    print(my_list)

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

import time
from datetime import timedelta

start_time = time.monotonic()
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))