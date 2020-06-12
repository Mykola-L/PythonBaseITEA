from numpy.random import seed
from numpy.random import randint
import math
from statistics import median

a = randint(10, 20, 1)
print(f'Розмір списку {a}')
seed(1)

my_list = randint(2, 10, a)
print(f'Послідовність випадкових чисел, випадкового розміру {my_list}')


def to_square_root(number):
    return math.sqrt(number)

result = map(to_square_root, my_list)

my_list_of_square_root = list(result)
print(f'Список, корінь квадратний від кожного числа послідовності {my_list_of_square_root}')

median_value_sequences = median(my_list_of_square_root)
print(f'Медіанне значення послідовності {median_value_sequences}')

def is_greater_than_median(number):
    return number > median_value_sequences

result = filter(is_greater_than_median, my_list_of_square_root)
print(f'Всі значення коренів квадратних, які є більші ніж медіанне значення {list(result)}')