# generate random integer values - генерувати випадкові цілі значення
from numpy.random import seed
from numpy.random import randint
import math
# seed random number generator - генератор випадкових чисел насіння

a = randint(10, 20, 1) # розмі списку
print(a)
seed(1)
# generate some integers - генерувати деякі цілі числа
my_list1 = randint(2, 10, a)
print(my_list1)

# в прикладі задачі з вхідної послідовністі можна знайти корінь без залишку. Я зробив послідовність схожу на приклад
my_list_of_squares = [] # створюю новий список, з допомогою циклу for

for i in my_list1:
    my_list_of_squares.append(i ** 2) # додаємо в новий список квадрат послідовності

print(my_list_of_squares)


# math.sqrt(X) - квадратный корень из X.

my_list_of_square_root = [] # створюю новий список, з допомогою циклу for

for i in my_list_of_squares:
    my_list_of_square_root.append(math.sqrt(i)) # додаємо в новий список квадрат послідовності

print(my_list_of_square_root)