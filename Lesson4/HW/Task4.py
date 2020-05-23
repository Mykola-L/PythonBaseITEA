import numpy
import random

a = random.randint(1, 10)
b = random.randint(11, 20)
c = random.randint(2, 5)
d = random.randint(2, 5)

random_integer_array = numpy.random.randint(a, b, size=(c, d))

s = 0
for i in range(len(random_integer_array)):
    for j in range(len(random_integer_array[i])):
        s += random_integer_array[i][j]
print(f'Сума всіх вкладених списків {s}')