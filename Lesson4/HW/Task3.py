from collections import Counter
import random

array = []

i = 0
n = 10
while i < n:
    array.append((random.randint(1, n)))
    i += 1

def random_numerical_sequence(array):
    c = Counter(array)

    start_dict = dict(c)

    max_value = max(start_dict.values())
    final_dict = {k: v for k, v in start_dict.items() if v == max_value}
    d = list(final_dict.keys())

    my_dict_length = len(final_dict)

    if my_dict_length > 1:
        a = max(final_dict.keys())
        print(f'Елемент який повторюється найчастіше, і одночасно найбільший {a}')
        return a
    else:
        print(f'Елемент який повторюється найчастіше, і одночасно найбільший {d}')
        return d

random_numerical_sequence(array)