from collections import Counter
import random

#array = ["Bob", "Alex", "Bob", "John"]
#array = [1, 9, 1, 2, 2, 3, 2, 2, 2, 4, 4, 4, 6, 5]
#array = [1, 9, 1, 2, 2, 3, 2, 2, 4, 4, 4, 6, 5, 5, 5, 5, 4]

array = []  # створюю список
# Цикл while викликає функцію багато разів
i = 0
n = 10
while i < n:  # розмір списку
    array.append((random.randint(1, n)))  # додаємо випадкові числа (від 1 до 1000) в список
    i += 1  # i = i + 1
print(array)

c = Counter(array) # словник в кортежі, рахує кількість елементів в словнику
print(f'Виводимо кількість елементів які повторюються {c}')

start_dict = dict(c) # переводимо кортеж в словник
# start_dict = Counter(array)

# c
# Counter({'Bob': 2, 'Alex': 1, 'John': 1})
#
# c['Bob']
# 2
#
# c['Unknown']
# 0

print(f'Переводимо кортеж в словник, виводимо словник {start_dict}')

#a = max(c)


max_value = max(start_dict.values()) # шукаємо максимальне значення в словнику
final_dict = {k: v for k, v in start_dict.items() if v == max_value}
#c = final_dict.values() # елемент фінального словника
d = list(final_dict.keys()) # елемент фінального словника


print(f'Максимальне значення в словнику {max_value}')
print(f'Словник з максимальними значеннями {final_dict}')

#my_dict = {'key': 'value'}
my_dict_length = len(final_dict) # Довжина словника з максимальними значеннями
print(f'Довжина словника з максимальними значеннями {my_dict_length}')

if my_dict_length > 1:
    a = max(final_dict.keys()) # Максимальне число ключ в словника з максимальними значеннями
    print(f'Елемент який повторюється найчастіше, і одночасно найбільший {a}')
else:
    print(f'Елемент який повторюється найчастіше, і одночасно найбільший {d}')