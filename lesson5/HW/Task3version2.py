# 3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

#import random
import time
import numpy

a = 100000



def list_generator(a):
    random_integer_array = numpy.random.randint(0, 1000, size=(1, a))  # генеруємо випадковий вкладений список
    #print(random_integer_array)

start_time = time.time()
list_generator(a)
print("Час виконання функції: " + " %s seconds " % (time.time() - start_time)) # час роботи функції