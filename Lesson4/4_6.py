import numpy
import random

a = random.randint(1, 10)
print(a)
b = random.randint(11, 20) # числа, елементи масиву від a до b
print(b)
c = random.randint(2, 5) # c - кількість вкладених елементів в масиві
print(c)
d = random.randint(2, 5) # c, d розмір масиву. d - кількість елементів вкладеного масиву
print(d)


random_integer_array = numpy.random.randint(a, b, size=(c, d)) # генеруємо випадковий вкладений список
print("2-мерный массив случайных целых чисел \n", random_integer_array)

#a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(random_integer_array)):
    for j in range(len(random_integer_array[i])):
        s += random_integer_array[i][j]
print(f'Сума всіх вкладених списків {s}')
