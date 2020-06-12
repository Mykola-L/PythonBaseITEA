# generate random integer values - генерувати випадкові цілі значення
from numpy.random import seed
from numpy.random import randint
import math
# seed random number generator - генератор випадкових чисел насіння

a = randint(10, 20, 1) # розмі списку
print(a)
seed(1)
# generate some integers - генерувати деякі цілі числа
my_list = randint(2, 10, a)
print(my_list)

# math.sqrt(X) - квадратный корень из X.
#for
# my_list_of_square_root = [] # створюю новий список, з допомогою циклу for
#
# for i in my_list:
#     my_list_of_square_root.append(math.sqrt(i)) # додаємо в новий список квадрат послідовності
#
# print(my_list_of_square_root)

#map
def to_square_root(number):
    return math.sqrt(number)

result = map(to_square_root, my_list) # map пробігає по my_list і застосовує функцію to_square як об'єкт без виклику
print(list(result)) # переведемо map в список