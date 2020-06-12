# def test_func():
#
#     print(' I am outer functions') # зовнішня функція
#
#     def inner_func(): # внутрішня функція
#         print('I am inner function')
#
#     def one_more_inner_func():
#         print('Hello I am one more inner function') # інша внутрішня функція
#
#     return inner_func, one_more_inner_func # повертаємо через кому дві функції
#
# functions = test_func() # передаємо функцію в список
# functions[0]() # викликаємо функцію по номеру елемента списку
# functions[1]()


# функція декоратор
def decorator(func): # функція декоратор приймає на вхід функцію яку потрібно змінити
# ім'я функції може бути будь-яке
    def wrapper(arg1):  # декоратор всередині містить іншу функцію wrapper, тут зберігається та поведінка яку ми будемо додавати до вихідної функції.
# wrapper може приймати деякі аргументи
# wrapper має приймати ту ж кількість цільових аргументів, які приймає цільова функція.
        print(arg1)
        print('decorating function')
        result = func(arg1) # цільова функція print(), не забуваємо в неї передавати аргументи
        print('Decoration ended')
        # значення цільової функції яке повертається визначається в середині wrapper
        return result # функція повертає об'єкт wrapper
# у wrapper ми вирішуємо що поверне наша функція start
    return wrapper

# функція цільова
@decorator # відмічаємо функцію декоратор, назва функції
def start(arg1):
    print('Function has been started')
    return 100

b = start(10)
print(b)
