from collections import Counter
import random

array = []

i = 0
n = 10
while i < n:
    array.append((random.randint(1, n)))
    i += 1

print(array)