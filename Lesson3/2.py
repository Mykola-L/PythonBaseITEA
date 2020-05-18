import random

n = int(input('Введіть, будь-ласка, кількість цілочисельних випадкових значень '))

# Як вивести функцію print() багато разів
i = 0
while i < 10:
# print(list(range(random.randint(1, 1000))))  # переводимо range в list
    print(random.randint(1, 1000))  # генерує випадкові числа від 1 до 1000

    i += 1  # i = i + 1

# if i == n:
#     continue
