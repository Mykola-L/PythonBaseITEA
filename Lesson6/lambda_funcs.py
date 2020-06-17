# створюємо анонімну Lambda функцію, яка знаходить суму двох значень а і b
# Lambda це ключове слово, яке вказує, що зараз буде анонімна функція.
# Після ключового слова Lambda в нас йде список, перелік аргументів які буде приймати ця функція.
# через функцію передаю аргументи, які функція буде приймати на вхід
# після : вказується те, що буде повертати фукція
# слово return не застосовується
# цю функцію часто використовують для того, щоб передати її як аргумент до іншої функції.

# my_sum = lambda a, b: a + b
# # об'єкт с містить lambda
# print(my_sum(10, 40)) # так звернутися до функції. Присвоїли ім'я анонімній функції
# # аргументи а і b
#
# def my_sum(a, b):
#     return a + b
#
# print(my_sum(10, 40))

def my_func_high_level(func):
    r = func(30, 40)
    return r

result = my_func_high_level(lambda a, b: a + b)
print(result)