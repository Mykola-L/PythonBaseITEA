import random

n = int(input('Введіть, будь-ласка, кількість цілочисельних випадкових значень '))
my_list = []  # створюю список
# Цикл while викликає функцію багато разів
# i = 0
# while i < n:  # розмір списку
#     my_list.append((random.randint(1, 1000)))  # додаємо випадкові числа (від 1 до 1000) в список
#     i < n
#     i += 1  # i = i + 1


i = 0
for i in my_list:
    my_list.append((random.randint(1, 1000))):
    i < n
    i += 1  # i = i + 1
print(i)

# print(my_list)
a = 0  # змінна, рахує кількість парних чисел
for i2 in my_list:  # my_list назва масиву по якому буде проходитися цикл for
    # i перемінна я яку ми записуємо результат повтору нашого циклу по масиву.
    if i2 % 2 == 0:  # залишок 0 від ділення на 2, визначаю парне число
        print(i2)
        a = a + 1
        # print(a)

if a == 0:
    print('Нажаль, всі цілочисельні випадкові значення непарні')