# 3) Создать функцию которая генерирует список из 100 тыс. случайных элементов в диапазоне [0, 1000]
# и вывести на экран время выполнения этой функции.

# генерує випадковий список масив чисел
import numpy
import random



random_integer_array = numpy.random.randint(0, 1000, size=(1, 100000)) # генеруємо випадковий вкладений список
print(random_integer_array)