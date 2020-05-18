import random

n = int(input('Введіть, будь-ласка, кількість цілочисельних випадкових значень '))
my_list = []  # створюю список
# Як вивести функцію print() багато разів
i = 0
while i < n:
    # print(list(range(random.randint(1, 1000))))  # переводимо range в list
    # print(random.randint(1, 1000))  # генерує випадкові числа від 1 до 1000

    my_list.append((random.randint(1, 1000)))  # додаємо випадкові числа в список
    # my_random = random.randint(50, 100) # генерує випадкові числа від 50 до 100
    # my_list.append(my_random)

    i += 1  # i = i + 1

print(my_list)
a = 0
for i in my_list:  # назва масиву по якому буде проходитися цикл for
    # i перемінна я яку ми записуємо результат повтору нашого циклу по масиву.
    # ключове слово in
    if i % 2 == 0:
        print(i)
        break
        # a = a + 1
        # print(a)
    # elif a == 0:
    #     print('Нажаль, всі цілочисельні випадкові значення непарні')
    else:
        print('Нажаль, всі цілочисельні випадкові значення непарні')

    # i = 0
    #
    #  matches = 0 # кількість співпадінь
    #
    #  while i < n:
    #      element = my_list[i] # зберігаємо в змінну елемент
    #      print(i)
    # #     if element == 2:
    # #         matches += 1 # matches = matches + 1
    # #         if matches > 2:
    # #             break # перериваємо цикл
    # #
    # #     i += 1  # i = i + 1
    # #
    # # if matches > 2:
    # #     print(f'Кількість співпадінь більше двох')